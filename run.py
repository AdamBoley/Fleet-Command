# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


# Player fleet strength variable:
player_battleships = 20
player_battlecruisers = 25
player_heavy_cruisers = 50
player_light_cruisers = 75
player_destroyers = 150



battleship_firepower = 20
battlecruiser_firepower = 15
heavy_cruiser_firepower = 8
light_cruiser_firepower = 5
destroyer_firepower = 2

total_firepower = ((player_battleships * battleship_firepower)
                    + (player_battlecruisers * battlecruiser_firepower)
                    + (player_heavy_cruisers * heavy_cruiser_firepower)
                    + (player_light_cruisers * light_cruiser_firepower)
                    + (player_destroyers * destroyer_firepower))

battleship_crew = 2000
battlecruiser_crew = 1500
heavy_cruiser_crew = 500
light_cruiser_crew = 300
destroyer_crew = 100

total_crew = ((player_battleships * battleship_crew)
                + (player_battlecruisers * battlecruiser_crew)
                + (player_heavy_cruisers * heavy_cruiser_crew)
                + (player_light_cruisers * light_cruiser_crew)
                + (player_destroyers * destroyer_crew))

marines = (40 * (player_battlecruisers + player_battleships))


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
    print(f'We currently have {player_battleships} battleships')
    print(f'We currently have {player_battlecruisers} battlecruisers')
    print(f'We currently have {player_heavy_cruisers} heavy cruisers')
    print(f'We currently have {player_light_cruisers} light cruisers')
    print(f'We currently have {player_destroyers} destroyers')
    print(f'Given the current number of ships, we currently have {total_firepower} turrets')
    print(f'We currently have {total_crew} crew')
    print(f'We currently have {marines} marines')


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat - heavily armoured and heavily armed.')
    print(f'Both Alliance and Syndicate battleships have {battleship_firepower} particle beam turrets\n')
    print('Battlecruisers are the cavalry of space combat - faster, but less heavily armoured and armed that battleships')
    print(f'Both Alliance and Syndicate battlecruisers have {battlecruiser_firepower} turrets\n')
    print('Heavy Cruisers are the largest escorts')
    print(f'Heavy cruisers have {heavy_cruiser_firepower} turrets\n')
    print('Light cruisers are mid-weight escorts')
    print(f'Light cruisers have {light_cruiser_firepower} turrets\n')
    print('Destroyers are the lightest, least capable escorts, but can be effective in large numbers.')
    print(f'Destroyers have {destroyer_firepower} turrets\n')
    print('Crew are used for operating ships.')
    print('Marines are used for boarding enemy ships and conducting ground assaults.')


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
