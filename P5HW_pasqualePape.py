
# Pasquale pape
# 11/18/2024
# P5_HW
# use functions to create a game with characters

import random
import time

def create_character():
    """
    Create a character with user-input attributes.
    
    :return: Dictionary representing the character
    """
    name = input("Enter a name: ")
    health = int(input("Enter health: "))
    attack = int(input("Enter attack: "))
    max_health = health
    character = {
        "name": name,
        "health": health,
        "max_health": max_health,  # Store original health separately
        "attack": attack,
        "healing_uses": 1  # Added healing uses limit
    }
    return character

def display_character(character):
    """
    Display all character attributes.
    
    :param character: Character dictionary
    """
    print(f"Character: {character['name']}")

    
    for key, value in character.items():
        print(f"{key}: {value}")
    print()

def battle(attacker, victim):
    """
    Simulate a battle where the victim takes random damage.
    
    :param attacker: Attacking character
    :param victim: Defending character
    :return: Updated victim 
    """
    print(f"\n{attacker['name']} is attacking {victim['name']}")
    time.sleep(1)
    
    damage = random.randint(0, attacker['attack'])
    victim['health'] -= damage
    
    print(f"{attacker['name']} did {damage} damage to {victim['name']}")
    print(f"{victim['name']} now has {victim['health']} health\n")
    
    return victim

def heal_character(character):
    """
    Heal a character to full health if healing uses are available.
    
    :param character: Character to heal
    :return: Boolean indicating if healing was successful
    """
    if character['healing_uses'] > 0:
        character['health'] = character['max_health']
        character['healing_uses'] -= 1
        print(f"{character['name']} healed to full health!")
        return character
    else:
        print(f"{character['name']} has no healing uses left!")
        return character


def check_character_life(char1, char2):
    """

    Check if either character has died and handle game state.
    
    :param char1: First character
    :param char2: Second character
    :return: Tuple of (continue_game, winner)
    """
    if char1['health'] <= 0 and char2['health'] <= 0:
        print("Both characters have died!")
        return False, None
    
    if char1['health'] <= 0:
        print(f"{char1['name']} has died!")
        return False, char2
    
    if char2['health'] <= 0:
        print(f"{char2['name']} has died!")
        return False, char1
    
    return True, None

def game_menu(char1, char2):
    """
    Main game action selection menu.
    
    :param char1: First character
    :param char2: Second character
    """
    while True:
        # Check if either character died
        game_continues, winner = check_character_life(char1, char2)
        if not game_continues:
            if winner:
                print(f"{winner['name']} wins!")
            end_game = input("Game over. Play again? (y/n): ").lower()
            if end_game != 'y':
                break
            return  # Exit function to restart game
        
        # Display menu
        print("\nChoose an action:")
        print("1: Battle")
        print("2: Heal Character")
        print("3: Show Stats")
        print("4: Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Battle sequence
            char2 = battle(char1, char2)
            if char2['health'] > 0:
                char1 = battle(char2, char1)
        
        elif choice == '2':
            # Healing
            heal_choice = input(f"Who to heal? 1: {char1['name']}, 2: {char2['name']}: ")
            if heal_choice == '1':
                char1 = heal_character(char1)
            elif heal_choice == '2':

                char2 = heal_character(char2)
        
        elif choice == '3':
            # Show character stats
            display_character(char1)
            display_character(char2)
        
        elif choice == '4':
            # Quit game
            print("Exiting game...")
            break

def main():
    """
    Main game initialization and loop.
    """
    print("Welcome to the Character Battle Game!")
    
    while True:
        # Create characters
        print("\nCreate first character: ")
        char1 = create_character()
        print("\nCreate second character: ")
        char2 = create_character()
        
        # Start game menu
        game_menu(char1, char2)
        
        # Ask to play again
        play_again = input("Do you want to start a new game? (y/n): ").lower()
        if play_again != 'y':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
