from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, disconnect
import office_combat
import robin_adventure
import sys
from io import StringIO
import threading
import queue
import os

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Global session tracking
active_sessions = {}

class WebOutput:
    def __init__(self, socket, session_id):
        self.socket = socket
        self.session_id = session_id
        self.buffer = ""
    
    def write(self, text):
        # Check if session is still active
        if self.session_id not in active_sessions:
            return
            
        # Check for clear screen sequence
        if '\033[2J' in text:
            # Send special clear command to terminal
            self.socket.emit('terminal_command', {'command': 'clear'})
            # Remove the clear screen sequence from the text
            text = text.replace('\033[2J', '')
        if '\033[H' in text:
            # Remove cursor home sequence as it's handled by clear
            text = text.replace('\033[H', '')
        
        # Replace single newlines with \r\n for proper terminal line breaks
        text = text.replace('\n', '\r\n')
        if text:  # Only emit if there's text to send
            self.socket.emit('terminal_output', {'data': text})
    
    def flush(self):
        if self.buffer and self.session_id in active_sessions:
            self.socket.emit('terminal_output', {'data': self.buffer})
            self.buffer = ""

class WebInput:
    def __init__(self, session_id):
        self.session_id = session_id
        self.queue = queue.Queue()
    
    def readline(self):
        if self.session_id not in active_sessions:
            raise Exception("Session terminated")
        socketio.emit('request_input')
        # Get input from queue and strip any whitespace
        return self.queue.get().strip() + '\n'

@app.route('/')
def index():
    return render_template('terminal.html')

@socketio.on('connect')
def handle_connect():
    session_id = request.sid
    game = request.args.get('game', 'combat')  # Default to combat if not specified
    active_sessions[session_id] = {
        'thread': None,
        'input_queue': WebInput(session_id),
        'game': game
    }
    print(f'Client connected: {session_id} for {game}')

@socketio.on('disconnect')
def handle_disconnect():
    session_id = request.sid
    cleanup_session(session_id)
    print(f'Client disconnected: {session_id}')

def cleanup_session(session_id):
    if session_id in active_sessions:
        # Stop the game thread if it's running
        session = active_sessions[session_id]
        if session['thread'] and session['thread'].is_alive():
            # The thread will terminate naturally when it checks session_id
            pass
        del active_sessions[session_id]

@socketio.on('user_input')
def handle_user_input(data):
    session_id = request.sid
    if session_id in active_sessions:
        active_sessions[session_id]['input_queue'].queue.put(data['input'])

@socketio.on('start_game')
def handle_start_game(data):
    session_id = request.sid
    if session_id not in active_sessions:
        return
        
    game = data.get('game', 'combat')  # Default to combat if not specified
    
    def run_game():
        try:
            # Redirect stdout to our custom output
            old_stdout = sys.stdout
            old_stdin = sys.stdin
            sys.stdout = WebOutput(socketio, session_id)
            sys.stdin = active_sessions[session_id]['input_queue']
            
            try:
                if game == 'combat':
                    office_combat.start_combat_game()
                else:
                    robin_adventure.start_game()
            except Exception as e:
                if session_id in active_sessions:  # Only show error if session still active
                    socketio.emit('terminal_output', {'data': f'\r\nGame ended: {str(e)}\r\n'})
            finally:
                sys.stdout = old_stdout
                sys.stdin = old_stdin
                cleanup_session(session_id)
        except Exception as e:
            print(f"Error in game thread: {e}")
    
    # Clean up any existing thread
    if active_sessions[session_id]['thread'] and active_sessions[session_id]['thread'].is_alive():
        cleanup_session(session_id)
        active_sessions[session_id] = {
            'thread': None,
            'input_queue': WebInput(session_id),
            'game': game
        }
    
    # Start new game thread
    thread = threading.Thread(target=run_game)
    thread.daemon = True
    active_sessions[session_id]['thread'] = thread
    thread.start()

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    socketio.run(app, debug=False, host='0.0.0.0', port=port) 