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
    

def player_fleet_status():
    """
    Function that can be called anytime to display the current status of the player's fleet
    """
    print(f"We currently have {player_ships['battleships']} battleships")
    print(f"We currently have {player_ships['battlecruisers']} battlecruisers")
    print(f"We currently have {player_ships['heavy cruisers']} heavy cruisers")
    print(f"We currently have {player_ships['light cruisers']} light cruisers")
    print(f"We currently have {player_ships['destroyers']} destroyers")
    print(f"Given the current number of ships, we currently have {total_firepower} turrets")
    print(f"We currently have {total_crew} crew")
    print(f"We currently have {marines} marines")


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat - heavily armoured and heavily armed.')
    print(f"Both Alliance and Syndicate battleships have {ship_firepower['battleship']} particle beam turrets\n")
    print('Battlecruisers are the cavalry of space combat - faster, but less heavily armoured and armed that battleships')
    print(f"Both Alliance and Syndicate battlecruisers have {ship_firepower['battlecruiser']} turrets\n")
    print('Heavy Cruisers are the largest escorts')
    print(f"Heavy cruisers have {ship_firepower['heavy cruiser']} turrets\n")
    print('Light cruisers are mid-weight escorts')
    print(f"Light cruisers have {ship_firepower['light cruiser']} turrets\n")
    print('Destroyers are the lightest, least capable escorts, but can be effective in large numbers.')
    print(f"Destroyers have {ship_firepower['destroyer']} turrets\n")
    print('Crew are used for operating ships.')
    print("Marines are used for boarding enemy ships and conducting ground assaults.")


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
