# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

player_ships = {
    'battleships': 20,
    'battlecruisers': 25,
    'heavy cruisers': 50,
    'light cruisers': 75,
    'destroyers': 150,
}

player_losses = {
    'battleships': 0,
    'battlecruisers': 0,
    'heavy cruisers': 0,
    'light cruisers': 0,
    'destroyers': 0
}

ship_firepower = {
    'battleship': 20,
    'battlecruiser': 15,
    'heavy cruiser': 8,
    'light cruiser': 5,
    'destroyer': 2,
}

ship_crew = {
    'battleship': 2000,
    'battlecruiser': 1500,
    'heavy cruiser': 500,
    'light cruiser': 300,
    'destroyer': 100,
}

total_firepower = (
    (player_ships['battleships'] * ship_firepower['battleship'])
    + (player_ships['battlecruisers'] * ship_firepower['battlecruiser'])
    + (player_ships['heavy cruisers'] * ship_firepower['heavy cruiser'])
    + (player_ships['light cruisers'] * ship_firepower['light cruiser'])
    + (player_ships['destroyers'] * ship_firepower['destroyer'])
)

total_crew = (
    (player_ships['battleships'] * ship_crew['battleship'])
    + (player_ships['battlecruisers'] * ship_crew['battlecruiser'])
    + (player_ships['heavy cruisers'] * ship_crew['heavy cruiser'])
    + (player_ships['light cruisers'] * ship_crew['light cruiser'])
    + (player_ships['destroyers'] * ship_crew['destroyer'])
)

marines = (
    (player_ships['battleships'] * 40)
    + (player_ships['battlecruisers'] * 40)
)

mines = (
    (player_ships['battleships'] * 10)
    + (player_ships['battlecruisers'] * 6)
)

missiles = (
    (player_ships['battleships'] * 20)
    + (player_ships['battlecruisers'] * 15)
    + (player_ships['heavy cruisers'] * 5)
)

fleet_assets = {
    'Marines': marines,
    'Mines': mines,
    'Missiles': missiles
}

experience = 1


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
        'battlecruisers': 4,
        'heavy cruisers': 12,
        'light cruisers': 20,
        'destroyers': 50
    }

    print(f'Admiral {player_name}, sensors have detected a group of enemy warships at the jump point!')
    print('The tactical suite is updating now - this group looks small')

    for key, value in enemy_group_one.items():
        print(f'The enemy have {value} {key}')
    print('Based on that, I assess this is a scouting unit')
    print('Admiral, if we choose, we should be able to take them easily!')
    print('Admiral, what are you orders?')
    engage_decision_mission_one = input('Press y to engage the enemy, or n to find worthier prey:\n')
    if engage_decision_mission_one == 'y':
        print('You: We engage! All hands - battle stations!')
        print('Roth: How should we approach this engagement?')
        print('You: We have several options')

    elif engage_decision_mission_one == 'n':
        print('You: This is not worth our time. Disengage')

    

def player_fleet_status():
    """
    Function that can be called anytime to display the current status of the player's fleet
    """
    for key, value in player_ships.items():
        print(f'We currently have {value} {key}')
    print(f"Given the current number of ships, we currently have {total_firepower} turrets")
    print(f"We currently have {total_crew} crew")
    for key, value in fleet_assets.items():
        print((f'We currently have {value} {key}'))


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat - heavily armoured and heavily armed')
    print(f"Battleships have {ship_firepower['battleship']} particle beam turrets")
    print('Battleships carry a large number of missiles and mines\n')
    print('Battlecruisers are the cavalry of space combat - faster, but are less heavily armoured and armed that battleships')
    print(f"Battlecruisers have {ship_firepower['battlecruiser']} turrets")
    print('Battlecruisers carry a large number of missiles and mines\n')
    print("Battleships and battlecruisers carry the fleets' Marines\n")
    print('Heavy Cruisers are the largest escorts')
    print(f"Heavy cruisers have {ship_firepower['heavy cruiser']} turrets")
    print('Heavy cruisers also carry a small number of missiles\n')
    print('Light cruisers are mid-weight escorts')
    print(f"Light cruisers have {ship_firepower['light cruiser']} turrets\n")
    print('Destroyers are the lightest, least capable escorts, but can be effective in large numbers')
    print(f"Destroyers have {ship_firepower['destroyer']} turrets\n")
    print('Crew are used for operating ships')
    print("Marines are used for boarding enemy ships and conducting ground assaults")


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
