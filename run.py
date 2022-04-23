# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

# print(random.randint(1, 10))

player_ships = {
    'battleships': 20,
    'cruisers': 50,
    'escorts': 150,
}

player_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

enemy_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

ship_firepower = {
    'battleship': 20,
    'cruiser': 10,
    'escort': 5,
}


tactical_library = {
    'approach 1': 'attack 25% of the enemy',
    'approach 2': 'attack 50% of the enemy',
    'approach 3': 'attack 66% of the enemy',
    'approach 4': 'attack all of the enemy'
}

player_total_firepower = (
    (player_ships['battleships'] * ship_firepower['battleship'])
    + (player_ships['cruisers'] * ship_firepower['cruiser'])
    + (player_ships['escorts'] * ship_firepower['escort'])
)


def new_game(player_name):
    """
    Starts a new game
    """
    print(f'Good morning Admiral {player_name}, I am Captain Roth, your staff officer')
    print('Welcome aboard the battleship Indomitable, Admiral')
    print('The Indomitable is your command ship')
    print('From here, you can see the status of the fleet and make tactical decisions in battle')
    print('do you want to see the status of the fleet now?')
    fleet_status_decision = input('Please press y to see fleet status or n to move on:\n') # gonna need some input checking here
    if fleet_status_decision == 'y':
        player_fleet_status()
    else:
        print('Very well Admiral')
    print('Do you want to see a breakdown of the capabilities of component of the fleet?')
    fleet_capabilities_decision = input('Please press y to see what each part of your fleet is capable of, or n to move on\n')
    if fleet_capabilities_decision == 'y':
        ship_capabilities()
    else:
        print('Indeed - a good naval officer should know the capabilities of their ships by heart')
    mission_one(player_name)


def mission_one(player_name):
    """
    Mission one - light combat, simple decisions, intended as an introduction to the game
    """
    enemy_group_one = {
        'battleships': 4,
        'cruisers': 15,
        'escorts': 50
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_one)

    print(f'Admiral {player_name}, sensors have detected a group of enemy warships at the jump point!')
    print('The tactical suite is updating now - this group looks small')

    for key, value in enemy_group_one.items():
        print(f'The enemy have {value} {key}')
    print(f'The enemy have {enemy_firepower} turrets')
    print('Based on that, I assess this is a scouting unit')
    print('Admiral, if we choose, we should be able to take them easily!')
    print('Admiral, what are you orders?')
    engage_decision_mission_one = input('Press y to engage the enemy, or n to find worthier prey:\n')
    if engage_decision_mission_one == 'y':
        print('You: We engage! All hands - battle stations!')
        print('Roth: How should we approach this engagement?')
        print('You: We have several options')
        for key, value in tactical_library.items():
            print(f'{key} - We can {value}')
        print('Roth: What will we do?')
            


    elif engage_decision_mission_one == 'n':
        print('You: This is not worth our time. Disengage')

    

def player_fleet_status():
    """
    Function that can be called anytime to display the current status of the player's fleet
    """
    for key, value in player_ships.items():
        print(f'We currently have {value} {key}')
    print(f"Given the current number of ships, we currently have {player_total_firepower} turrets")


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat - heavily armoured and heavily armed')
    print(f"Battleships have {ship_firepower['battleship']} particle beam turrets")
    print('Cruisers are midweight combatants')
    print(f"Cruisers have {ship_firepower['cruiser']} turrets")
    print('Escorts are light screening ships, effective in numbers')
    print(f"Escorts have {ship_firepower['escort']} turrets\n")


def firepower_comparator(player_total_firepower, enemy_total_firepower):
    """
    Called each time player fleet and enemy fleet fight. Compares firepower ratings to determine outcome
    """


def enemy_firepower_calculator(enemy_strength):
    """
    function to calculate the firepower rating of an enemy fleet
    """
    battleship_firepower = 20
    cruiser_firepower = 10
    escort_firepower = 5

    enemy_firepower = ((enemy_strength['battleships'] * battleship_firepower)
                        + (enemy_strength['cruisers'] * cruiser_firepower)
                        + (enemy_strength['escorts'] * escort_firepower))
    return enemy_firepower



def main():
    """
    Contains main program functions
    """
    print('Welcome to Fleet Command, a space battle simulator game')
    player_name = input('Please enter your name:\n')
    print(f'Greetings Admiral {player_name}\n')
    print('The Alliance, a confederation of democratically-ruled star-systems, has been at war with the autocratic Syndicate Worlds for 20 years\n')
    print('The war shows no sign of ending, as both sides are locked in a stalemate\n')
    print('You are a promising young naval officer, and you have just been given command of a fleet\n')
    print('The Syndicate Worlds have gathered a mighty fleet, and have attacked at multiple points\n')
    print(f'{player_name}, you have been charged with defending the Alliance\n')

    new_game(player_name)


main()
