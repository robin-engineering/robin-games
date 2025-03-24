import sys
import time
import os

# ANSI color codes
PURPLE = '\033[95m'  # Robin's brand purple
RED = '\033[91m'     # For the dots
RESET = '\033[0m'    # Reset color

def clear_screen():
    """Clear the terminal screen"""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')

def check_reset(user_input):
    """Check if the user wants to reset the game"""
    if user_input.lower() == "reset":
        clear_screen()
        start_game()
        return True
    return False

def type_text(text, delay=0.01):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # New line after text

def print_separator():
    print("\n" + "="*50 + "\n")

def print_title():
    clear_screen()
    
    title = f"""
    {RED}══════════════════════════════════════════════════════════════════════════════════════════════════════
    
          {RED}█████  █{RED}████                                                                                 
         {RED}██████  █{RED}█████              {PURPLE}███████████                    ████            ████               
          {RED}█████  █{RED}████               {PURPLE}██████████████                 ████            ████              
    {RED}███                  ███         {PURPLE}███████████████                ████            ████              
   {RED}█████    ████████    █████        {PURPLE}█████      █████               ████                               
   {RED}██████  ██████████  ██████        {PURPLE}█████      █████  ██████████   ██████████████  ████  ████████████ 
    {RED}       ██████████                {PURPLE}███████████████  █████████████ ███████████████ ████  █████████████
    {RED}████   ██████████   ████         {PURPLE}███████████████ █████    █████ ██████    █████ ████  █████    ████
   {RED}██████  ██████████  ██████        {PURPLE}█████████████   ████      ████ █████      ████ ████  ████     ████
   {RED}█████    █████████   █████        {PURPLE}█████    █████  █████     ████ █████     █████ ████  ████     ████
    {RED}███                  ███         {PURPLE}█████    ██████ ██████████████ ███████████████ ████  ████     ████
          {RED}█████  █{RED}████               {PURPLE}█████     ██████  ███████████  ██████████████  ████  ████     ████
         {RED}██████  █{RED}█████              {PURPLE}█████      █████    ██████     ████  █████     ████  ████     ████
          {RED}█████  █{RED}████                                                                                 
                                                                   
                                                    W O R K P L A C E   A D V E N T U R E             
                                                                   
    ══════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
    """
    print(title)
    time.sleep(1)  # Pause for dramatic effect

def print_welcome():
    type_text("Welcome to an interactive adventure where you'll experience the modern workplace!")
    type_text("You'll explore how Robin's platform transforms the way people work together.")
    type_text("\nThis game will show you two different workplace experiences:")
    type_text("- A workplace enhanced by Robin's technology")
    type_text("- The traditional way of managing office life")
    type_text("\nYour choices will shape your workplace journey...")

def start_game():
    print_title()
    print_welcome()
    print_separator()
    type_text("First, choose your role:")
    type_text("\n1. Employee - Experience how Robin can help you navigate the workplace")
    type_text("2. Office Administrator - See how Robin can help manage the workplace")
    type_text("\nAt any time, type 'reset' to restart the game.")
    
    choice = input("\nSelect your role (1/2): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        start_employee_path()
    elif choice == "2":
        start_admin_path()
    elif choice.lower() == "x":
        from office_combat import start_combat_game
        start_combat_game()
    else:
        type_text("Invalid choice. Please try again.")
        start_game()

def start_employee_path():
    clear_screen()
    print_separator()
    type_text("You just received an important company announcement:")
    type_text("\n'BigTechCo is implementing a new hybrid work policy starting next week.")
    type_text("All employees will be required to work from the office 2 days per week.'")
    
    type_text("\nThoughts race through your mind:")
    type_text("- When should you go in?")
    type_text("- Where will you sit?")
    type_text("- Will your teammates be there?")
    type_text("- How will you coordinate schedules?")
    
    type_text("\nYou're an employee at BigTechCo, and today you'll experience two parallel universes:")
    type_text("One where your company uses Robin, and one where they don't.")
    type_text("Your choices will show you the difference Robin makes in navigating the return to office.")
    
    print_separator()
    choose_universe()

def start_admin_path():
    clear_screen()
    print_separator()
    type_text("As the Office Administrator at BigTechCo, you've just received word from leadership:")
    type_text("\n'We're implementing a hybrid work policy starting next week.")
    type_text("All employees will be required to work from the office 2 days per week.'")
    
    type_text("\nAs the workplace team lead, you need to:")
    type_text("- Coordinate desk and room arrangements for 500+ employees")
    type_text("- Ensure meeting spaces are properly equipped")
    type_text("- Track office capacity and usage patterns")
    type_text("- Help teams coordinate their in-office schedules")
    
    type_text("\nYou're responsible for making this transition smooth for everyone.")
    type_text("Today, you'll experience two approaches to managing this change:")
    type_text("1. Using Robin's powerful workplace platform")
    type_text("2. Trying to coordinate everything manually")
    
    choice = input("\nSelect your experience (1/2, or type 'reset' to restart): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        admin_first_choice()
    elif choice == "2":
        admin_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        start_admin_path()

def admin_first_choice():
    clear_screen()
    print_separator()
    type_text("It's Monday morning. What would you like to focus on?")
    type_text("1. Review workplace analytics and usage data")
    type_text("2. Configure desk and room booking policies")
    type_text("3. Manage visitor access and scheduling")
    
    choice = input("\nWhat would you like to do? (1/2/3, or type 'reset' to restart): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        admin_analytics()
    elif choice == "2":
        admin_policies()
    elif choice == "3":
        admin_visitors()
    else:
        type_text("Invalid choice. Please try again.")
        admin_first_choice()

def admin_analytics():
    print_separator()
    type_text("Robin's analytics dashboard shows:")
    type_text("1. View desk utilization rates across floors")
    type_text("2. Check meeting room booking patterns")
    type_text("3. Analyze peak office attendance days")
    
    choice = input("\nWhat would you like to review? (1/2/3): ")
    
    if choice == "1":
        type_text("\nThe dashboard shows:")
        type_text("- 75% average desk utilization on Tuesdays and Wednesdays")
        type_text("- Lower usage near the elevator (noise concerns reported)")
        type_text("- Standing desks have highest booking rates")
        type_text("\nBased on this data, you can:")
        type_text("- Recommend quiet zones near high-traffic areas")
        type_text("- Plan to add more standing desks in next office update")
    elif choice == "2":
        type_text("\nMeeting room analytics reveal:")
        type_text("- Small pods (2-4 people) are most in demand")
        type_text("- Video conferencing rooms peak at 10am and 3pm")
        type_text("- Several rooms are underutilized due to AV issues")
        type_text("\nThis helps you:")
        type_text("- Prioritize AV equipment maintenance")
        type_text("- Consider converting larger rooms to smaller spaces")
    elif choice == "3":
        type_text("\nAttendance patterns show:")
        type_text("- Tuesday-Thursday are peak office days")
        type_text("- 70% of employees use hybrid schedules")
        type_text("- Team collaboration spaces most used mid-week")
        type_text("\nThis data helps optimize:")
        type_text("- HVAC scheduling")
        type_text("- Catering services")
        type_text("- Cleaning crew scheduling")
    
    admin_second_choice()

def admin_policies():
    print_separator()
    type_text("You can update workplace policies in Robin:")
    type_text("1. Modify desk booking rules")
    type_text("2. Update meeting room settings")
    type_text("3. Configure floor plan layouts")
    
    choice = input("\nWhat would you like to modify? (1/2/3): ")
    
    if choice == "1":
        type_text("\nDesk booking policy options:")
        type_text("- Set advance booking windows")
        type_text("- Enable/disable desk sharing")
        type_text("- Configure check-in requirements")
        type_text("\nThese tools help:")
        type_text("- Ensure fair access to popular spaces")
        type_text("- Maintain accurate utilization data")
        type_text("- Support flexible seating arrangements")
    elif choice == "2":
        type_text("\nMeeting room configurations:")
        type_text("- Set booking duration limits")
        type_text("- Configure room capacities")
        type_text("- Manage catering service integrations")
        type_text("\nThis ensures:")
        type_text("- Efficient resource utilization")
        type_text("- Appropriate room assignments")
        type_text("- Streamlined meeting services")
    elif choice == "3":
        type_text("\nFloor plan management in Robin:")
        type_text("- Drag and drop desks to new locations")
        type_text("- Add or remove collaboration spaces")
        type_text("- Update room types and capacities")
        type_text("\nThis helps you:")
        type_text("- Quickly adapt to changing needs")
        type_text("- Optimize space utilization")
        type_text("- Keep employees informed of changes")
    
    admin_second_choice()

def admin_visitors():
    print_separator()
    type_text("Robin's visitor management system shows:")
    type_text("1. Review upcoming visitor schedule")
    type_text("2. Configure visitor access policies")
    type_text("3. Manage host notifications")
    
    choice = input("\nWhat would you like to manage? (1/2/3): ")
    
    if choice == "1":
        type_text("\nUpcoming visitors this week:")
        type_text("- 5 client meetings with automated check-in scheduled")
        type_text("- 3 vendor presentations with room assignments")
        type_text("- 2 interview candidates with host coordination")
        type_text("\nRobin automatically:")
        type_text("- Sends welcome emails with directions")
        type_text("- Coordinates security access")
        type_text("- Notifies hosts of arrival")
    elif choice == "2":
        type_text("\nVisitor policy options:")
        type_text("- Set advance registration requirements")
        type_text("- Configure security checkpoint procedures")
        type_text("- Customize visitor badge settings")
        type_text("\nThis ensures:")
        type_text("- Streamlined check-in process")
        type_text("- Consistent security protocols")
        type_text("- Professional visitor experience")
    elif choice == "3":
        type_text("\nHost notification settings:")
        type_text("- Configure arrival alerts")
        type_text("- Set up automated welcome messages")
        type_text("- Manage check-in instructions")
        type_text("\nBenefits include:")
        type_text("- Improved host preparedness")
        type_text("- Reduced lobby wait times")
        type_text("- Enhanced visitor experience")
    
    admin_second_choice()

def admin_second_choice():
    print_separator()
    type_text("Based on your review, you can now:")
    type_text("1. Generate reports for leadership")
    type_text("2. Plan workplace improvements")
    type_text("3. Update employee communications")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nAfter implementing Robin:")
        type_text("- Employee satisfaction increased by 85%")
        type_text("- Time spent on administrative tasks reduced by 60%")
        type_text("- Meeting room utilization improved by 40%")
        type_text("- Workplace conflicts decreased significantly")
        type_text("\nYour office has become a model of modern workplace efficiency!")
        
        type_text("\nThanks for exploring Robin's administrative features!")
        type_text("You've seen how Robin helps workplace teams:")
        type_text("- Make data-driven decisions")
        type_text("- Optimize resource utilization")
        type_text("- Improve employee experience")
        type_text("- Streamline office management")
        play_again()
    else:
        type_text("Invalid choice. Please try again.")
        admin_second_choice()

def choose_universe():
    type_text("It's 8:00 AM Tuesday morning, and you're getting ready to go into the office.")
    type_text("1. Use Robin to plan your workday")
    type_text("2. Try to navigate the office without Robin")
    
    choice = input("\nWhat would you like to do? (1/2, or type 'reset' to restart): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        first_choice_with_robin()
    elif choice == "2":
        first_choice_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        choose_universe()

def first_choice_with_robin():
    clear_screen()
    type_text("It's 8:00 AM, and you're planning your day from home.")
    type_text("Opening the Robin app, you can:")
    type_text("1. Check office occupancy for today")
    type_text("2. See which teammates will be in")
    type_text("3. View available desks near your team")
    
    choice = input("\nWhat would you like to do? (1/2/3, or type 'reset' to restart): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        check_occupancy()
    elif choice == "2":
        check_teammates()
    elif choice == "3":
        view_desks()
    else:
        type_text("Invalid choice. Please try again.")
        first_choice_with_robin()

def check_occupancy():
    print_separator()
    type_text("The Robin app shows today's office stats:")
    type_text("- Current office occupancy: 45%")
    type_text("- Plenty of desk availability on all floors")
    type_text("\nKnowing this, you can:")
    type_text("1. Book a desk for the full day")
    type_text("2. Schedule a team lunch since most are in")
    type_text("3. Reserve a meeting room for afternoon collaboration")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nGreat planning! You've optimized your office day before leaving home.")
        book_desk()
    elif choice == "2":
        type_text("\nPerfect timing for team building!")
        schedule_team_lunch()
    elif choice == "3":
        type_text("\nSmart to book early while rooms are available!")
        reserve_meeting_room()
    else:
        type_text("Invalid choice. Please try again.")
        check_occupancy()

def schedule_team_lunch():
    print_separator()
    type_text("Let's schedule a team lunch!")
    type_text("First, you'll need a space. Robin shows:")
    type_text("1. The Cafe Area (casual, up to 15 people)")
    type_text("2. Meeting Room with Catering Setup (formal, up to 12 people)")
    type_text("3. Outdoor Terrace (weather permitting, up to 20 people)")
    
    choice = input("\nWhere would you like to host lunch? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nGreat choice! Now let's arrange catering.")
        arrange_catering()
    else:
        type_text("Invalid choice. Please try again.")
        schedule_team_lunch()

def arrange_catering():
    print_separator()
    type_text("Robin's catering service integration shows available options:")
    type_text("1. Local Sandwich Shop (variety platters)")
    type_text("2. Mediterranean Kitchen (individual bowls)")
    type_text("3. Sushi Bar (mixed rolls and boxes)")
    
    choice = input("\nWhat type of catering would you like? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nPerfect! Robin will:")
        type_text("- Reserve the space for your team")
        type_text("- Send calendar invites to all participants")
        type_text("- Create your catering request")
        type_text("- Notify facilities about setup needs")
        type_text("\nYour team lunch is all set!")
        second_choice()
    else:
        type_text("Invalid choice. Please try again.")
        arrange_catering()

def check_teammates():
    print_separator()
    type_text("Robin shows your team's office plans:")
    type_text("- 7 teammates will be in the office today")
    type_text("- Most are sitting in the East Wing")
    type_text("- Team standup scheduled for 10am")
    
    type_text("\nYou can:")
    type_text("1. Book a desk near your team")
    type_text("2. Reserve a room for an impromptu team sync")
    type_text("3. Schedule collaborative work time")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nPerfect! You've coordinated your day with your team before arriving.")
        book_desk()
    elif choice == "2":
        type_text("\nGreat idea! Let's find a space for the team to meet.")
        reserve_meeting_room()
    elif choice == "3":
        type_text("\nExcellent! Planning ahead for team collaboration.")
        reserve_meeting_room()
    else:
        type_text("Invalid choice. Please try again.")
        check_teammates()

def view_desks():
    print_separator()
    type_text("The floor plan shows available desks:")
    type_text("- Several spots open in the team neighborhood")
    type_text("- Standing desks available by the windows")
    type_text("- Quiet focus areas have good availability")
    
    type_text("\nYou can:")
    type_text("1. Reserve your favorite spot now")
    type_text("2. Book a desk near today's meetings")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nExcellent! You've secured your ideal workspace before commuting.")
        book_desk()
    elif choice == "2":
        type_text("\nSmart thinking! Let's check the meeting schedule first.")
        reserve_meeting_room()
    else:
        type_text("Invalid choice. Please try again.")
        view_desks()

def first_choice_without_robin():
    clear_screen()
    print_separator()
    type_text("Without Robin, you're starting your day with uncertainty:")
    type_text("1. Head straight to the office and hope for the best")
    type_text("2. Text a few colleagues to ask if they're coming in")
    type_text("3. Try to remember which desks were free yesterday")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if check_reset(choice):
        return
    elif choice == "1":
        type_text("\nYou arrive at the office with no advance planning...")
        desk_without_robin()
    elif choice == "2":
        type_text("\nOnly two colleagues respond. One thinks they might come in later...")
        desk_without_robin()
    elif choice == "3":
        type_text("\nYou recall some empty desks, but have no way to know if they're available today...")
        desk_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        first_choice_without_robin()

def book_desk():
    print_separator()
    type_text("You open the desk booking interface.")
    type_text("You see a digital floor plan with available desks highlighted in green.")
    type_text("You notice:")
    type_text("1. A quiet desk near the window")
    type_text("2. A desk in the collaborative area")
    type_text("3. A standing desk in the focus zone")
    
    choice = input("\nWhich desk would you like to book? (1/2/3): ")
    
    if choice == "1":
        type_text("\nGreat choice! You've booked a quiet desk with a view.")
        type_text("The natural light will help you stay focused throughout the day.")
        second_choice()
    elif choice == "2":
        type_text("\nPerfect! You'll be close to your team for easy collaboration.")
        type_text("The desk comes with a monitor and docking station.")
        second_choice()
    elif choice == "3":
        type_text("\nExcellent! The standing desk will help you stay active.")
        type_text("This area has a strict quiet policy for maximum focus.")
        second_choice()
    else:
        type_text("Invalid choice. Please try again.")
        book_desk()

def reserve_meeting_room():
    print_separator()
    type_text("The Robin app shows available meeting rooms:")
    type_text("1. Brainstorm Room (4 people, whiteboard wall)")
    type_text("2. Video Conference Room (8 people, AV equipment)")
    type_text("3. Focus Pod (2 people, perfect for quick syncs)")
    
    choice = input("\nWhich room would you like to reserve? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nRoom successfully booked!")
        second_choice()
    else:
        type_text("Invalid choice. Please try again.")
        reserve_meeting_room()

def second_choice():
    print_separator()
    type_text("You're on the train heading to the office.")
    type_text("You can:")
    type_text("1. Check in to your desk via the Robin mobile app")
    type_text("2. Play Candy Crush to pass the time")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nUsing the Robin app, you:")
        type_text("- Confirm your desk check-in")
        type_text("- See your upcoming meetings for the day")
        type_text("- Get notified that your catering order is confirmed")
        type_text("- Receive turn-by-turn directions to your desk")
        type_text("\nYou arrive at the office ready to start your productive day!")
        office_feedback()
    elif choice == "2":
        type_text("\nAfter enjoying your game, you arrive at the office:")
        type_text("- Your phone connects to the office WiFi")
        type_text("- Robin automatically checks you in to your desk")
        type_text("- A notification welcomes you to the office")
        type_text("- Your desk location appears on your phone")
        type_text("\nRobin's automated check-in makes arrival seamless,")
        type_text("even when you're focused on beating that tough Candy Crush level!")
        office_feedback()
    else:
        type_text("Invalid choice. Please try again.")
        second_choice()

def office_feedback():
    print_separator()
    type_text("At the end of your workday, Robin asks about your office experience:")
    type_text("1. Great - Everything worked perfectly!")
    type_text("2. OK - Most things went well")
    type_text("3. Bad - Had some issues")
    
    choice = input("\nHow was your visit? (1/2/3): ")
    
    if choice == "1":
        type_text("\nThanks for your feedback! Robin noted that you had a great experience:")
        type_text("- Your desk was ready when you arrived")
        type_text("- All your meetings ran smoothly")
        type_text("- The catering service was on time")
        type_text("This helps us maintain high workplace satisfaction!")
    elif choice == "2":
        type_text("\nThanks for your feedback! Robin will:")
        type_text("- Review your desk and room bookings")
        type_text("- Check if any services were delayed")
        type_text("- Look for ways to improve your next visit")
        type_text("Your input helps us make the workplace better!")
    elif choice == "3":
        type_text("\nWe're sorry to hear that! Robin will:")
        type_text("- Analyze what went wrong")
        type_text("- Schedule maintenance checks if needed")
        type_text("- Adjust service coordination")
        type_text("- Follow up to ensure your next visit is better")
        type_text("Thank you for helping us improve!")
    else:
        type_text("Invalid choice. Please try again.")
        office_feedback()
        return

    type_text("\nThanks for exploring Robin's workplace platform!")
    type_text("You've experienced just a few of the ways Robin helps teams")
    type_text("work better together in the hybrid workplace.")
    play_again()

def play_again():
    choice = input("\nWould you like to play again? (y/n, or type 'reset' to restart now): ")
    if check_reset(choice):
        return
    elif choice.lower() == 'y':
        print_separator()
        start_game()
    elif choice.lower() == 'n':
        type_text("\nThanks for playing! Have a great day!")
    else:
        type_text("Invalid choice. Please try again.")
        play_again()

def desk_without_robin():
    print_separator()
    type_text("You walk around the office looking for an available desk.")
    type_text("After 15 minutes of searching, you find:")
    type_text("1. A desk that looks empty but has someone's belongings on it")
    type_text("2. A desk in a quiet area with a 'Reserved' sticky note")
    type_text("3. Keep searching for another desk")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice in ["1", "2"]:
        type_text("\nOh no! The desk's owner returns and explains it's actually taken.")
        type_text("You've lost 30 minutes of productive time searching for a desk.")
        type_text("With Robin, you could have seen real-time desk availability")
        type_text("and booked your space before even arriving at the office.")
        second_choice_without_robin()
    elif choice == "3":
        type_text("\nAfter another 20 minutes, you finally find an available desk.")
        type_text("You've lost 35 minutes of productive time that could have been saved")
        type_text("by using Robin's desk booking system.")
        second_choice_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        desk_without_robin()

def meeting_without_robin():
    print_separator()
    type_text("You need to find a meeting room, but without Robin:")
    type_text("1. Walk around checking each room's availability")
    type_text("2. Ask colleagues if they know of any free rooms")
    type_text("3. Try to hold the meeting in the open office area")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nAfter checking 5 rooms, you find they're all occupied.")
        type_text("Some have no meetings but people are using them without bookings.")
        type_text("Your team is getting frustrated waiting for updates.")
    elif choice == "2":
        type_text("\nNo one seems to know which rooms are actually available.")
        type_text("Two people suggest different rooms, but both turn out to be booked.")
    elif choice == "3":
        type_text("\nThe open office area is too noisy for an effective meeting.")
        type_text("Several team members can't hear each other clearly.")
    
    type_text("\nWith Robin, you could have:")
    type_text("- Seen real-time room availability")
    type_text("- Booked a suitable room instantly")
    type_text("- Sent automatic invites to your team")
    second_choice_without_robin()

def amenities_without_robin():
    print_separator()
    type_text("Without Robin's amenity tracking:")
    type_text("1. Walk to the coffee bar to check the line")
    type_text("2. Try each phone booth to find an available one")
    type_text("3. Ask around about the wellness room schedule")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nYou walk to the coffee bar and find 8 people in line.")
        type_text("You've wasted a trip - with Robin, you would have known the wait time.")
    elif choice == "2":
        type_text("\nAfter checking 4 phone booths, you finally find an available one,")
        type_text("but you've missed the first 5 minutes of your call.")
    elif choice == "3":
        type_text("\nNo one seems to know the wellness room schedule.")
        type_text("You find it occupied with no indication of when it will be free.")
    
    type_text("\nRobin would have shown you real-time availability")
    type_text("and allowed you to reserve amenities in advance.")
    second_choice_without_robin()

def second_choice_without_robin():
    print_separator()
    type_text("It's afternoon, and without Robin:")
    type_text("1. Try to find a quiet space for an important client call")
    type_text("2. Coordinate a last-minute team brainstorm")
    type_text("3. Look for specific colleagues in the office")
    
    choice = input("\nWhat would you like to do? (1/2/3): ")
    
    if choice == "1":
        type_text("\nYou wander the office looking for a quiet spot:")
        type_text("- All phone booths are occupied with no booking system")
        type_text("- You try a meeting room but get kicked out mid-call")
        type_text("- End up taking the call from your car in the parking lot")
        type_text("- Client comments on the unprofessional background noise")
    elif choice == "2":
        type_text("\nTrying to organize an impromptu meeting is chaotic:")
        type_text("- No way to know which teammates are in the office")
        type_text("- Spend 20 minutes looking for an available room")
        type_text("- Half the team can't find where you finally settled")
        type_text("- Lose valuable brainstorming time to logistics")
    elif choice == "3":
        type_text("\nSearching for colleagues becomes a scavenger hunt:")
        type_text("- Walk every floor looking for team members")
        type_text("- Send mass emails asking where people are sitting")
        type_text("- Miss an important conversation with your manager")
        type_text("- Waste an hour just trying to connect with people")
    else:
        type_text("Invalid choice. Please try again.")
        second_choice_without_robin()
        return

    type_text("\nThese workplace challenges show why Robin is essential:")
    type_text("- Eliminates time wasted searching for spaces")
    type_text("- Makes it easy to find and connect with colleagues")
    type_text("- Ensures resources are available when you need them")
    type_text("- Creates a more productive work environment")
    play_again()

def admin_without_robin():
    print_separator()
    type_text("Without Robin, you start your Monday managing the office using:")
    type_text("1. Spreadsheets for desk assignments")
    type_text("2. A shared calendar for meeting rooms")
    type_text("3. Email threads for meeting service requests")
    
    choice = input("\nWhat would you like to handle first? (1/2/3): ")
    
    if choice == "1":
        manual_desk_management()
    elif choice == "2":
        manual_room_management()
    elif choice == "3":
        manual_service_requests()
    else:
        type_text("Invalid choice. Please try again.")
        admin_without_robin()

def manual_desk_management():
    print_separator()
    type_text("You open your desk assignment spreadsheet and find:")
    type_text("- 15 new desk requests from employees")
    type_text("- 3 double-bookings from yesterday")
    type_text("- 5 complaints about reserved desks being taken")
    
    type_text("\nYou need to:")
    type_text("1. Manually cross-reference all booking requests")
    type_text("2. Send individual emails to resolve conflicts")
    type_text("3. Update the floor plan printouts")
    
    choice = input("\nWhat will you tackle first? (1/2/3): ")
    
    if choice == "1":
        type_text("\nSpending your morning with multiple spreadsheets open:")
        type_text("- Cross-checking every request against existing bookings")
        type_text("- Trying to spot patterns in desk preferences")
        type_text("- Realizing some data is already outdated")
    elif choice == "2":
        type_text("\nYour inbox is getting more crowded by the minute:")
        type_text("- Writing detailed explanations for each conflict")
        type_text("- Receiving frustrated replies about the delay")
    elif choice == "3":
        type_text("\nPrinting and posting new floor plans:")
        type_text("- The printer is having issues")
        type_text("- You have to walk around the office, pasting up new plans")
        type_text("- New change requests came in while you were away")
    else:
        type_text("Invalid choice. Please try again.")
        manual_desk_management()
        return
        
    type_text("\nAfter two hours of administrative work:")
    type_text("- You've only processed 60% of the requests")
    type_text("- Three new conflicts have emerged")
    type_text("- Employees are getting frustrated with the wait")
    type_text("\nWith Robin, this would be:")
    type_text("- Automated desk booking system")
    type_text("- Real-time availability updates")
    type_text("- Self-service for employees")
    admin_second_choice_without_robin()

def manual_room_management():
    print_separator()
    type_text("Looking at the shared calendar system:")
    type_text("- Multiple rooms booked for the same meeting")
    type_text("- No way to track actual room usage")
    type_text("- Confusion about room capacities and equipment")
    
    type_text("\nYou need to:")
    type_text("1. Call each meeting organizer to confirm needs")
    type_text("2. Walk through the office to check actual usage")
    type_text("3. Update the room feature lists")
    
    choice = input("\nWhat's your priority? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nAfter several hours:")
        type_text("- Found 40% of rooms booked but unused")
        type_text("- Discovered missing equipment in three rooms")
        type_text("- Received complaints about double-bookings")
        type_text("\nRobin would provide:")
        type_text("- Automatic room release for no-shows")
        type_text("- Equipment tracking and maintenance alerts")
        type_text("- Clear visibility of room features and capacity")
        admin_second_choice_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        manual_room_management()

def manual_service_requests():
    print_separator()
    type_text("Your inbox is flooded with meeting service requests:")
    type_text("- Multiple catering orders for overlapping times")
    type_text("- AV setup requests for different rooms")
    type_text("- Room configuration changes needed")
    
    type_text("\nYou attempt to:")
    type_text("1. Create a spreadsheet to track all service requests")
    type_text("2. Forward requests to various service providers")
    type_text("3. Try to coordinate with the facilities team")
    
    choice = input("\nHow will you proceed? (1/2/3): ")
    
    if choice in ["1", "2", "3"]:
        type_text("\nBy end of day:")
        type_text("- Catering deliveries went to wrong rooms")
        type_text("- AV setup delayed several meetings")
        type_text("- Room layouts weren't ready in time")
        type_text("\nRobin would enable:")
        type_text("- Automated service request coordination")
        type_text("- Real-time status updates to all parties")
        type_text("- Integrated scheduling of services with room bookings")
        admin_second_choice_without_robin()
    else:
        type_text("Invalid choice. Please try again.")
        manual_service_requests()

def admin_second_choice_without_robin():
    print_separator()
    type_text("As the day ends, you realize managing without Robin means:")
    type_text("1. Hours spent on manual administrative tasks")
    type_text("2. Reduced visibility into workplace usage")
    type_text("3. Frustrated employees and inefficient processes")
    
    choice = input("\nWhat's your biggest concern? (1/2/3): ")
    
    if choice == "1":
        type_text("\nYour day has been consumed by:")
        type_text("- Updating multiple spreadsheets")
        type_text("- Responding to endless email chains")
        type_text("- Manually coordinating service requests")
        type_text("- Double-checking every booking for conflicts")
    elif choice == "2":
        type_text("\nWithout proper tracking, you're struggling with:")
        type_text("- Unknown peak usage times")
        type_text("- Unclear space utilization rates")
        type_text("- No data for future planning")
        type_text("- Difficulty justifying resource needs")
    elif choice == "3":
        type_text("\nThe lack of automation has led to:")
        type_text("- Booking conflicts and double-bookings")
        type_text("- Delayed responses to employee requests")
        type_text("- Confusion about space availability")
        type_text("- Time wasted on preventable issues")
    else:
        type_text("Invalid choice. Please try again.")
        admin_second_choice_without_robin()
        return

    type_text("\nThe contrast is clear. Robin would provide:")
    type_text("- Automated workplace management")
    type_text("- Real-time analytics and insights")
    type_text("- Enhanced employee experience")
    type_text("- Significant time savings for administrators")
    play_again()

if __name__ == "__main__":
    start_game() 