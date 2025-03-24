import random
import time
import sys
import os

# ANSI color codes
PURPLE = '\033[95m'
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# ANSI control sequences
CLEAR_SCREEN = '\033[2J'  # Clear entire screen
CURSOR_HOME = '\033[H'    # Move cursor to home position

class Player:
    def __init__(self):
        self.name = "Workplace Hero"
        self.hp = 150
        self.max_hp = 150
        self.energy = 90
        self.max_energy = 90
        self.mana = 0  # Start with no mana
        self.max_mana = 100
        self.has_magic = False  # Unlock after first level up
        self.base_damage = 10
        self.inventory = {
            "Cup of Coffee": 2,
            "Slice of Pizza": 2,
            "Al's Sandwich": 0,
            "Diet Coke": 0,
            "Sweetgreen Salad": 0,
            "Shot of Whiskey": 0,
        }

class Enemy:
    def __init__(self, name, hp, attacks):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attacks = attacks

class Ally:
    def __init__(self, name):
        self.name = name
        self.base_damage = 10
        self.attacks = []

def type_text(text, delay=0.01):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    """Clear the terminal screen"""
    # Instead of using os.system, use ANSI escape sequences
    sys.stdout.write(CLEAR_SCREEN)
    sys.stdout.write(CURSOR_HOME)
    sys.stdout.flush()

def print_health_bar(name, hp, max_hp, color=GREEN):
    """Display a health bar for the given entity"""
    bar_length = 30
    fill = int(bar_length * (hp / max_hp))
    bar = f"{color}{'█' * fill}{RED}{'█' * (bar_length - fill)}{RESET}"
    # Pad the name to ensure consistent alignment
    padded_name = f"{name + ':':20}"  # Pad to 20 characters
    return f"{padded_name} {bar} {hp}/{max_hp}"

def print_combat_status(player, enemy, allies=None):
    """Display the current combat status"""
    print("\n" + "="*80)
    # Print player's stats
    print(print_health_bar(player.name, player.hp, player.max_hp, BLUE))
    print(f"{'Energy:':20} {YELLOW}{'█' * (player.energy // 3)}{RESET} {player.energy}/{player.max_energy}")
    if player.has_magic:
        print(f"{'AI Mana:':20} {PURPLE}{'█' * (player.mana // 3)}{RESET} {player.mana}/{player.max_mana}")
    
    # Print allies if present
    if allies:
        print("\nAllies:")
        for ally in allies:
            print(f"{'':4}• {PURPLE}{ally.name}{RESET} (Base DMG: {ally.base_damage})")
    
    # Empty line for spacing
    print()
    # Print enemy's stats
    print(print_health_bar(enemy.name, enemy.hp, enemy.max_hp, GREEN))
    print("="*80 + "\n")

def use_item(player):
    """Handle item usage"""
    if not any(player.inventory.values()):
        type_text("Your inventory is empty!")
        return False

    print("\nInventory:")
    for item, count in player.inventory.items():
        if count > 0:
            print(f"- {item} (x{count})")

    choice = input("\nWhich item would you like to use? (or 'back' to return): ")
    
    if choice.lower() == 'back':
        return False

    if choice in player.inventory and player.inventory[choice] > 0:
        if choice == "Cup of Coffee":
            player.energy = min(100, player.energy + 40)
            type_text("\nYou drink a cup of coffee and feel energized!")
            player.inventory[choice] -= 1
            return 0
        elif choice == "Slice of Pizza":
            healing = 40
            player.hp = min(player.max_hp, player.hp + healing)
            type_text(f"\nYou eat a slice of pizza, healing {healing} HP!")
            player.inventory[choice] -= 1
            return 0
    else:
        type_text("Invalid item choice!")
        return False

def select_player_action(player, enemy):
    """Handle the player's action selection"""
    type_text("\nYour turn! What would you like to do?")
    print("1. Use Robin Tools")
    print("2. Use Non-Robin Tools")
    print("3. Use Item")
    if player.has_magic:
        print("4. Cast Robin AI Magic")
        print("5. Rest (Recover Energy)")
    else:
        print("4. Rest (Recover Energy)")

    max_choice = 5 if player.has_magic else 4
    choice = input(f"\nEnter your choice (1-{max_choice}): ")

    if choice == "1":
        if player.energy >= 20:
            attacks = [
                {"name": "`Desk Booking Blitz`", "damage": random.randint(15, 25) + player.base_damage, 
                 "description": "You unleash a wave of perfectly organized desk assignments!"},
                {"name": "`Visitor Victory`", "damage": random.randint(20, 30) + player.base_damage, 
                 "description": "You coordinate all visitor access with perfect precision!"},
                {"name": "`Workplace Analytics Wave`", "damage": random.randint(25, 35) + player.base_damage, 
                 "description": "You bombard chaos with data-driven insights!"},
                {"name": "`Meeting Room Manager`", "damage": random.randint(18, 28) + player.base_damage, 
                 "description": "You coordinate all meeting spaces with ruthless efficiency!"}
            ]
            
            attack = random.choice(attacks)
            bonus_damage = player.energy // 30
            total_damage = attack["damage"] + bonus_damage
            energy_cost = random.randint(15, 20)
            player.energy -= energy_cost
            return ("attack", attack["description"], attack["name"], total_damage, energy_cost)
        else:
            type_text("\nNot enough energy! Try resting or using an item.")
            return select_player_action(player, enemy)
    elif choice == "2":
        if player.energy >= 30:
            # Non-Robin tools cost more energy and do less damage
            attacks = [
                {"name": "Excel Spreadsheet", "damage": random.randint(3, 7) + (player.base_damage // 3), 
                 "description": "You frantically update a complex spreadsheet!"},
                {"name": "Email Chain", "damage": random.randint(5, 9) + (player.base_damage // 3), 
                 "description": "You start a lengthy email thread!"},
                {"name": "Sticky Notes", "damage": random.randint(4, 6) + (player.base_damage // 3), 
                 "description": "You plaster the walls with sticky note reminders!"},
                {"name": "Paper Calendar", "damage": random.randint(5, 8) + (player.base_damage // 3), 
                 "description": "You flip through a paper calendar looking for conflicts!"},
                {"name": "Whiteboard Diagram", "damage": random.randint(6, 10) + (player.base_damage // 3), 
                 "description": "You draw a complicated seating chart on the whiteboard!"}
            ]
            
            attack = random.choice(attacks)
            energy_cost = random.randint(25, 30)
            player.energy -= energy_cost
            return ("attack", attack["description"], attack["name"], attack["damage"], energy_cost)
        else:
            type_text("\nNot enough energy! Try resting or using an item.")
            return select_player_action(player, enemy)
    elif choice == "3":
        if not any(player.inventory.values()):
            type_text("Your inventory is empty!")
            return select_player_action(player, enemy)

        # Create numbered list of available items
        available_items = []
        print("\nInventory:")
        item_num = 1
        for item, count in player.inventory.items():
            if count > 0:
                print(f"{item_num}. {item} (x{count})")
                available_items.append(item)
                item_num += 1
        print(f"{item_num}. Back")

        item_choice = input(f"\nSelect item (1-{item_num}): ")
        
        try:
            choice_num = int(item_choice)
            if choice_num == item_num:  # Selected "Back"
                return select_player_action(player, enemy)
            if 1 <= choice_num < item_num:
                selected_item = available_items[choice_num - 1]
                player.inventory[selected_item] -= 1
                
                if selected_item == "Cup of Coffee":
                    player.energy = min(player.max_energy, player.energy + 40)
                    return ("item_effect", "\nYou drink a cup of coffee and feel energized!", None, 0, 0)
                elif selected_item == "Slice of Pizza":
                    healing = 40
                    player.hp = min(player.max_hp, player.hp + healing)
                    return ("item_heal", f"\nYou eat a slice of pizza, healing {GREEN}{healing}{RESET} HP!", None, 0, 0)
                elif selected_item == "Al's Sandwich":
                    healing = 60
                    energy_gain = 60
                    player.hp = min(player.max_hp, player.hp + healing)
                    player.energy = min(player.max_energy, player.energy + energy_gain)
                    return ("item_heal", f"\nYou eat Al's famous sandwich, healing {GREEN}{healing}{RESET} HP and gaining {energy_gain} energy!", None, 0, 0)
                elif selected_item == "Diet Coke":
                    energy_gain = 15
                    player.energy = min(player.max_energy, player.energy + energy_gain)
                    return ("item_effect", f"\nYou chug a Diet Coke, gaining {energy_gain} energy!", None, 0, 0)
                elif selected_item == "Sweetgreen Salad":
                    healing = 50
                    player.hp = min(player.max_hp, player.hp + healing)
                    return ("item_heal", f"\nYou eat a healthy Sweetgreen salad, healing {GREEN}{healing}{RESET} HP!", None, 0, 0)
                elif selected_item == "Shot of Whiskey":
                    damage = 10
                    energy_gain = 60
                    player.hp = max(1, player.hp - damage)
                    player.energy = min(player.max_energy, player.energy + energy_gain)
                    return ("item_heal", f"\nYou take a shot of whiskey, losing {RED}{damage}{RESET} HP but gaining {energy_gain} energy!", None, 0, 0)
            else:
                type_text("Invalid choice! Try again.")
                return select_player_action(player, enemy)
        except ValueError:
            type_text("Invalid choice! Try again.")
            return select_player_action(player, enemy)
    elif choice == "4" and player.has_magic:
        if player.mana >= 30:
            spells = [
                {"name": "`Automatic Desk Booking`", "damage": random.randint(30, 45), "mana_cost": random.randint(10, 15),
                 "description": "Your users are automatically assigned the desks they want!"},
                {"name": "`Talk to your Data`", "damage": random.randint(35, 50), "mana_cost": random.randint(14, 20),
                 "description": "You use an intuitive chat interface to get actionable insights!"},
                {"name": "`Smart Space Suggestions`", "damage": random.randint(40, 55), "mana_cost": random.randint(10, 22),
                 "description": "You get recommendations for the best spaces to use!"},
                {"name": "`Smart Desk Suggestions`", "damage": random.randint(45, 60), "mana_cost": random.randint(7, 30),
                 "description": "You get recommendations for the best desks to sit at!"}
            ]
            
            spell = random.choice(spells)
            player.mana -= spell["mana_cost"]
            return ("magic", spell["description"], spell["name"], spell["damage"], 0)  # 0 for energy cost
        else:
            type_text("\nNot enough mana! Try resting or waiting for mana regeneration.")
            return select_player_action(player, enemy)
    elif choice == "5" if player.has_magic else choice == "4":
        energy_gain = random.randint(30, 50)
        mana_gain = random.randint(20, 35) if player.has_magic else 0
        player.energy = min(player.max_energy, player.energy + energy_gain)
        player.mana = min(player.max_mana, player.mana + mana_gain)
        return ("rest", f"\nYou take a moment to rest, recovering {energy_gain} energy" + 
                (f" and {mana_gain} mana" if player.has_magic else "") + ".", None, 0, 0)
    else:
        type_text("Invalid choice! Try again.")
        return select_player_action(player, enemy)

def enemy_turn(enemy):
    """Handle the enemy's turn"""
    attack = random.choice(enemy.attacks)
    type_text(f"\n{enemy.name} {attack['description']}")
    return attack['damage']

def ally_turn(ally, enemy):
    """Handle the ally's turn"""
    attack = random.choice(ally.attacks)
    total_damage = attack['damage'] + ally.base_damage
    type_text(f"\n{ally.name} {attack['description']}")
    type_text(f"{ally.name}'s {attack['name']} deals {RED}{total_damage}{RESET} damage!")
    return total_damage

def create_ally(allies_count):
    """Create a new ally with a unique role"""
    # List of positive adjectives for allies
    positive_adjectives = [
        "Brilliant",
        "Innovative",
        "Dynamic",
        "Strategic",
        "Proactive",
        "Visionary",
        "Resourceful",
        "Expert",
        "Masterful",
        "Skilled",
        "Experienced",
        "Dedicated",
        "Enthusiastic",
        "Passionate",
        "Determined"
    ]
    
    ally_types = [
        {
            "name": "Robin Admin",
            "base_damage": 5,
            "attacks": [
                {"name": "Space Optimization", "damage": random.randint(5, 15),
                 "description": "optimizes the office layout for maximum efficiency!"},
                {"name": "Analytics Insight", "damage": random.randint(8, 18),
                 "description": "uses workplace data to target inefficiencies!"},
                {"name": "Platform Integration", "damage": random.randint(10, 20),
                 "description": "leverages Robin's full platform capabilities!"},
                {"name": "Workplace Report", "damage": random.randint(7, 17),
                 "description": "unleashes powerful workplace analytics!"},
                {"name": "System Update", "damage": random.randint(9, 19),
                 "description": "deploys critical platform improvements!"}
            ]
        },
        {
            "name": "Workplace Champion",
            "base_damage": 7,
            "attacks": [
                {"name": "Team Coordination", "damage": random.randint(6, 16),
                 "description": "perfectly synchronizes team schedules!"},
                {"name": "Resource Allocation", "damage": random.randint(8, 18),
                 "description": "maximizes workplace resource usage!"},
                {"name": "Culture Boost", "damage": random.randint(10, 20),
                 "description": "energizes the workplace community!"},
                {"name": "Change Management", "damage": random.randint(7, 17),
                 "description": "guides the team through workplace evolution!"},
                {"name": "Best Practices", "damage": random.randint(9, 19),
                 "description": "implements proven workplace strategies!"}
            ]
        },
        {
            "name": "Office Manager",
            "base_damage": 8,
            "attacks": [
                {"name": "Visitor Experience", "damage": random.randint(8, 18),
                 "description": "creates a seamless guest experience!"},
                {"name": "Service Coordination", "damage": random.randint(10, 20),
                 "description": "orchestrates all workplace services!"},
                {"name": "Space Planning", "damage": random.randint(12, 22),
                 "description": "optimizes every square foot of the office!"},
                {"name": "Facility Management", "damage": random.randint(9, 19),
                 "description": "maintains perfect workplace conditions!"},
                {"name": "Experience Management", "damage": random.randint(11, 21),
                 "description": "ensures employees have a great experience!"}
            ]
        }
    ]
    
    # Get a new ally type based on current allies count
    ally_type = ally_types[allies_count % len(ally_types)]
    
    # Add a random positive adjective to the name
    adjective = random.choice(positive_adjectives)
    modified_name = f"{adjective} {ally_type['name']}"
    
    ally = Ally(modified_name)
    ally.base_damage = ally_type["base_damage"]
    ally.attacks = ally_type["attacks"]
    return ally

def combat_round(player, enemy, allies=None, enemies_defeated=0):
    """Handle a single round of combat"""
    clear_screen()
    print_combat_status(player, enemy, allies)
    
    # Get player's intended action
    action_type, description, name, damage, energy_cost = select_player_action(player, enemy)
    
    # Enemy's turn
    enemy_damage = enemy_turn(enemy)
    player.hp -= enemy_damage
    type_text(f"You take {RED}{enemy_damage}{RESET} damage!")
    
    if player.hp <= 0:
        return False
    
    time.sleep(.6)
    
    # Resolve player's action
    print()
    type_text(description)
    if action_type in ["attack", "item_attack"]:
        if energy_cost:
            type_text(f"Your {name} deals {RED}{damage}{RESET} damage and uses {YELLOW}{energy_cost}{RESET} energy!")
        else:
            type_text(f"Your {name} deals {RED}{damage}{RESET} damage!")
        enemy.hp -= damage
    elif action_type == "magic":
        mana_cost = player.max_mana - player.mana  # Calculate mana used from the spell
        type_text(f"Your {name} deals {RED}{damage}{RESET} damage and uses {PURPLE}{mana_cost}{RESET} mana!")
        enemy.hp -= damage
    
    # Allies' turns
    if allies and enemy.hp > 0:
        for ally in allies:
            if enemy.hp > 0:  # Check if enemy still alive
                time.sleep(.6)
                ally_damage = ally_turn(ally, enemy)
                enemy.hp -= ally_damage
    
    if enemy.hp <= 0:
        print("\n" + "="*80)
        type_text(f"{PURPLE}✨ VICTORY! ✨{RESET}")
        type_text(f"The {RED}{enemy.name}{RESET} has been defeated!")
        type_text(f"{GREEN}Order has been restored to {'another' if enemies_defeated > 0 else 'the'} workplace!{RESET}")
        print("="*80)
        time.sleep(.5)
        return True
    
    time.sleep(1)
    # Wait for any key press to continue
    type_text("\nPress Enter to continue...")
    input().strip()  # Strip whitespace from input
    return False

def create_enemy(enemies_defeated):
    """Create an enemy with scaled difficulty based on enemies defeated"""
    # Scale up enemy stats based on enemies defeated
    hp_scale = 100 + (enemies_defeated * 30)  # Each victory adds 30 HP
    damage_scale = enemies_defeated * 4  # Each victory adds 4 to damage
    
    # List of adverbs describing how the office is inefficient
    adverbs = [
        "Chaotically",
        "Hopelessly",
        "Catastrophically",
        "Ridiculously",
        "Hilariously",
        "Absurdly",
        "Comically",
        "Tragically",
        "Spectacularly",
        "Outrageously",
        "Impossibly",
        "Devastatingly",
        "Bizarrely",
        "Mysteriously",
        "Dramatically"
    ]
    
    # Randomly choose between one or two adverbs
    num_adverbs = random.randint(1, 2)
    current_adverbs = random.sample(adverbs, num_adverbs)
    
    # Combine adverbs with spaces
    adverb_string = ", ".join(current_adverbs) + " "
    
    enemies = [
        {
            "name": f"{adverb_string}Inefficient Office",
            "hp": hp_scale,
            "attacks": [
                {"description": "confuses visitors with no instructions!", "damage": random.randint(22, 30) + damage_scale},
                {"description": "creates mass seating confusion!", "damage": random.randint(16, 25) + damage_scale},
                {"description": "loses track of a catering request!", "damage": random.randint(27, 35) + damage_scale},
                {"description": "starts a territorial meeting room dispute!", "damage": random.randint(22, 30) + damage_scale},
                {"description": "operates blindly with no workplace data!", "damage": random.randint(24, 33) + damage_scale},
                {"description": "causes parking lot pandemonium!", "damage": random.randint(20, 27) + damage_scale},
                {"description": "struggles with outdated floor plans!", "damage": random.randint(20, 30) + damage_scale},
                {"description": "has way too few meeting rooms and way too many desks!", "damage": random.randint(24, 30) + damage_scale},
                {"description": "schedules maintenance during peak hours!", "damage": random.randint(20, 31) + damage_scale},
                {"description": "doesn't listen to their employees' feedback!", "damage": random.randint(25, 35) + damage_scale}
            ]
        }
    ]
    
    enemy_template = random.choice(enemies)
    return Enemy(
        enemy_template["name"],
        enemy_template["hp"],
        enemy_template["attacks"]
    )

def print_combat_title():
    clear_screen()
    
    title = f"""

    {RED}══════════════════════════════════════════════════════════════════════════════════════════════════════
    
          {PURPLE}███████████                    ████            ████                  {RED}██████╗  ██╗   ██╗███████╗██╗     
          {PURPLE}██████████████                 ████            ████                  {RED}██╔══██╗ ██║   ██║██╔════╝██║     
          {PURPLE}███████████████                ████            ████                  {RED}██║  ██║ ██║   ██║█████╗  ██║     
          {PURPLE}█████      █████               ████                                  {RED}██║  ██║ ██║   ██║██╔══╝  ██║     
          {PURPLE}█████      █████  ██████████   ██████████████  ████  ████████████    {RED}██████╔╝ ╚██████╔╝███████╗███████╗
          {PURPLE}███████████████  █████████████ ███████████████ ████  █████████████   {RED}╚═════╝   ╚═════╝ ╚══════╝╚══════╝
          {PURPLE}███████████████ █████    █████ ██████    █████ ████  █████    ████  
          {PURPLE}█████████████   ████      ████ █████      ████ ████  ████     ████       {RED}O F F I C E
          {PURPLE}█████    █████  █████     ████ █████     █████ ████  ████     ████  
          {PURPLE}█████    ██████ ██████████████ ███████████████ ████  ████     ████       {RED}W A R R I O R
          {PURPLE}█████     ██████  ███████████  ██████████████  ████  ████     ████  
          {PURPLE}█████      █████    ██████     ████  █████     ████  ████     ████  
                                                                                 
    ══════════════════════════════════════════════════════════════════════════════════════════════════════{RESET}
    """
    print(title)
    time.sleep(1)  # Pause for dramatic effect

def start_combat_game():
    """Main game loop"""
    print_combat_title()
    type_text(f"{PURPLE}Welcome to ROBIN: OFFICE WARRIOR!{RESET}")
    type_text("You've entered a parallel universe where office inefficiencies have come to life!")
    type_text("Armed with Robin's workplace platform, you must restore order to the chaos.")
    
    player = Player()
    enemies_defeated = 0
    allies = []
    
    while player.hp > 0:
        enemy = create_enemy(enemies_defeated)
        type_text(f"\nA wild {enemy.name} appears!")
        type_text("\nPress Enter to begin combat...")
        input().strip()  # Strip whitespace from input
        
        while True:
            if combat_round(player, enemy, allies, enemies_defeated):
                enemies_defeated += 1
                
                # Add a new ally after each victory
                new_ally = create_ally(len(allies))
                type_text(f"\n{PURPLE}A {new_ally.name} appears to join your quest!{RESET}")
                type_text("They will help you fight against office inefficiencies!")
                allies.append(new_ally)
                
                # Reward player
                player.hp = min(player.max_hp, player.hp + 40)
                player.energy = min(100, player.energy + 40)
                
                item1 = random.choice(list(player.inventory.keys()))
                player.inventory[item1] += 1
                print()
                type_text(f"You found a {item1}!")
                
                if random.random() < 0.7:  # 70% chance for second item
                    item2 = random.choice(list(player.inventory.keys()))
                    player.inventory[item2] += 1
                    type_text(f"You also found a {item2}!")

                if random.random() < 0.4:  # 40% chance for third item
                    item3 = random.choice(list(player.inventory.keys()))
                    player.inventory[item3] += 1
                    type_text(f"You also found a {item3}!")
                
                break
            
            if player.hp <= 0:
                print("\n" + "="*80)
                type_text(f"{RED}💀 GAME OVER 💀{RESET}")
                type_text(f"The {RED}{enemy.name}{RESET} has overwhelmed you!")
                type_text(f"{RED}Chaos reigns in the workplace once more...{RESET}")
                type_text(f"{RED}You might want to try a different strategy...{RESET}")
                print(f"\n{PURPLE}But your efforts were not in vain:{RESET}")
                type_text(f"You defeated {GREEN}{enemies_defeated}{RESET} office inefficiencies!")
                print("="*80)
                return
        
        if enemies_defeated % 2 == 0:
            type_text(f"\n{GREEN}Level Up!{RESET}")
            player.max_hp += 20
            player.hp = player.max_hp
            player.base_damage += 5
            
            # Unlock magic after first level up
            if enemies_defeated == 2 and not player.has_magic:
                type_text(f"\n{PURPLE}✨ You have unlocked Robin AI Magic! ✨{RESET}")
                type_text("You can now use powerful AI-driven spells in combat!")
                player.has_magic = True
                player.mana = player.max_mana  # Start with full mana
            
            # Level up all allies too
            for ally in allies:
                ally.base_damage += 5
        
        type_text("\nContinue fighting? (y/n): ")
        choice = input().strip().lower()
        if choice != 'y':
            type_text(f"\nYou defeated {enemies_defeated} office inefficiencies!")
            type_text("Thanks for playing ROBIN: OFFICE WARRIOR!")
            return

if __name__ == "__main__":
    start_combat_game() 