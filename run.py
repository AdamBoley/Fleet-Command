# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math
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

enemy_bypassed = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

ship_firepower = {
    'battleship': 20,
    'cruiser': 10,
    'escort': 5,
}


tactical_library = {
    '1': 'attack 25% of the enemy',
    '2': 'attack 50% of the enemy',
    '3': 'attack 75% of the enemy',
    '4': 'attack all of the enemy'
}

player_firepower = (
    (player_ships['battleships'] * ship_firepower['battleship'])
    + (player_ships['cruisers'] * ship_firepower['cruiser'])
    + (player_ships['escorts'] * ship_firepower['escort'])
)

player_name = ''
flagship_name = ''


def new_game():
    """
    Starts a new game
    """
    global player_name
    global flagship_name
    player_name = input('Please enter your name:\n')
    flagship_name = input('Please enter the name of your flagship:\n')
    print(f'Roth: Good morning Admiral {player_name}')
    print('Roth: I am Captain Roth, your staff officer')
    print(f'Roth: Welcome aboard the battleship {flagship_name}, Admiral')
    print(f'Roth: The {flagship_name} is your command ship')
    print('Roth: From here you can issue orders to your fleet in battle')
    print('Roth: I will keep you updated with pertinent information')
    print('Roth: Do you want to see the status of the fleet now?')
    fleet_status_decision = input('Please press y to see fleet status or n to move on:\n') # gonna need some input checking here
    if fleet_status_decision == 'y':
        player_fleet_status()
    else:
        print('Roth: Very well Admiral')
    print('Do you want to see the capabilities of component of the fleet?')
    fleet_capabilities_decision = input('Please press y to see what each part of your fleet is capable of, or n to move on\n')
    if fleet_capabilities_decision == 'y':
        ship_capabilities()
    else:
        print('Indeed - a good naval officer should know the capabilities of their ships by heart')
    mission_one()


def mission_one():
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
    print(f'The enemy ships have a total of {enemy_firepower} turrets')
    print('Based on that, I assess this is a scouting unit')
    
    firepower_difference = firepower_comparator(player_firepower, enemy_firepower)
    print(f'Roth: We have {firepower_difference} more turrets than they do')
    
    print('Admiral, if we choose, we should be able to take them easily!')
    print('Admiral, shall we engage?')
    engage_decision_mission_one = input('Press y to engage the enemy, or n to find worthier prey:\n')
    if engage_decision_mission_one == 'y':
        print('You: We engage! All hands - battle stations!')
        fight_battle(enemy_firepower, player_firepower, enemy_group_one)
        
    elif engage_decision_mission_one == 'n':
        print('You: This is not worth our time. Disengage')
    
    mission_two()


def mission_two():
    """
    Mission Two - heavier combat, requires the player to use their
    experience from Mission One to win
    """
    print('Roth: Arriving at Salamis in 3....2...1')
    print('Roth: Looks like the enemy is here in strength, Admiral')
    enemy_group_two = {
        'battleships': 12,
        'cruisers': 30,
        'escorts': 100
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_two)
    for key, value in enemy_group_two.items():
        print(f'The enemy group has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')
    print('Roth: This will be a tough battle, Admiral')
    print('Roth: Shall we engage?')
    engage_decision_mission_two = input('press y to engage, or n to disengage:\n')
    if engage_decision_mission_two == 'y':
        print('You: Indeed we shall, we cannot allow a force of this strength to roam free')
        fight_battle(enemy_firepower, player_firepower, enemy_group_two)
    elif engage_decision_mission_two == 'n':
        print('You: I think not - follow-on forces should be able to handle them')


def update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor):
    """
    Called from fight_engagement function
    updates enemy_group_strength dictionary with ships destroyed in the firing run
    Returns updated enemy_group_strength to fight_engagement
    """
    enemy_group_strength = {
        'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * firepower_factor)),
        'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * firepower_factor)),
        'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * firepower_factor))
    }
    return enemy_group_strength


def update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor):
    """
    Called from fight_engagement function
    Updates global enemy_losses dictionary with ships destroyed in the firing run
    Returns updated enemy_losses dictionary
    """
    enemy_losses = {
        'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * firepower_factor),
        'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * firepower_factor),
        'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * firepower_factor)
    }
    return enemy_losses


def update_player_ships(effective_enemy_firepower, losses_factor):
    """
    Called from fight_engagement function
    Updates global player_ships dictionary with losses sustained in the firing run
    Returns updated player_ships dictionary
    """
    global player_ships
    player_ships = {
        'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * losses_factor),
        'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * losses_factor),
        'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * losses_factor)
    }
    if player_ships['battleships'] < 0:
        player_ships = {
            'battleships': 0,
            'cruisers': player_ships['cruisers'],
            'escorts': player_ships['escorts']
        }
    if player_ships['cruisers'] < 0:
        player_ships = {
            'battleships': player_ships['battleships'],
            'cruisers': 0,
            'escorts': player_ships['escorts']
        }
    if player_ships['escorts'] < 0:
        player_ships = {
            'battleships': player_ships['battleships'],
            'cruisers': player_ships['cruisers'],
            'escorts': 0
        }

    return player_ships


def update_player_losses(effective_enemy_firepower, losses_factor):
    """
    Called from fight_engagement function
    Updates global player_losses dictionary with losses sustained in the firing run
    Returns updated player_losses dictionary
    """
    global player_losses
    player_losses = {
        'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * losses_factor),
        'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * losses_factor),
        'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * losses_factor)
    }
    return player_losses


def fight_battle(enemy_firepower, player_firepower, enemy_group_strength):
    """
    Function that is called when the player decides to fight an enemy in a mission
    """
    print('Roth: How shall we engage?')

    def fight_engagement(enemy_firepower, player_firepower, enemy_group_strength):
        """
        A long, complex function that is called for each firing run
        """
        global enemy_losses
        global player_ships
        global player_losses

        for key, value in enemy_group_strength.items():
            print(f'The enemy have {value} {key}')

        print('You: we have several options:')
        for key, value in tactical_library.items():
            print(f'{key} - We can {value}')
        
        tactic = input('Type a number from 1 to 4 to select your tactic:\n')
        if tactic == '1':
            print('You: We will aim to hit 25% of them in our firing run')
            print('Roth: A sound plan - maximum concentration of force')
            target_factor = 0.25
            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)

            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = calculate_effective_enemy_firepower(effective_enemy_strength)

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')
            
            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge!')
                print('Roth: Most of the targeted enemy ships are destroyed!')
                firepower_factor = 0.90
                losses_factor = 0.01

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)
                
            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable')
                print('Roth: Many of the targeted enemy ships are destroyed')
                firepower_factor = 0.80
                losses_factor = 0.02

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor')
                print('Roth: A moderate number of enemy ships are destroyed')
                firepower_factor = 0.70
                losses_factor = 0.03

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)
        
        elif tactic == '2':
            print('You: We will hit half of their ships in our firing run')
            target_factor = 0.50
            
            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)

            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = calculate_effective_enemy_firepower(effective_enemy_strength)

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge!')
                print('Roth: Many enemy ships destroyed!')

                firepower_factor = 0.70
                losses_factor = 0.05

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable')
                print('Roth: A good number of enemy ships are destroyed')

                firepower_factor = 0.60
                losses_factor = 0.10

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)
                
            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor')
                print('Roth: About half of the targeted enemy ships are down')

                firepower_factor = 0.50
                losses_factor = 0.15

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)
        
        elif tactic == '3':
            print('You: We will aim to hit three-quarters of them in our firing run')
            target_factor = 0.75
            
            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)

            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = calculate_effective_enemy_firepower(effective_enemy_strength)

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge!')
                print('Roth: Many enemy ships destroyed')
                firepower_factor = 0.60
                losses_factor = 0.10

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable')
                print('Roth: A good number enemy ships are destroyed')

                firepower_factor = 0.50
                losses_factor = 0.15

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)


            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor')
                print('Roth: A moderate number of enemy ships are destroyed')

                firepower_factor = 0.40
                losses_factor = 0.20

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)
        
        elif tactic == '4':
            print('You: Maximum attack! Target all enemy ships!')
            target_factor = 1
            
            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)

            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = calculate_effective_enemy_firepower(effective_enemy_strength)

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge!')
                print('Roth: A moderate number of enemy ships destroyed')

                firepower_factor = 0.40
                losses_factor = 0.20

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable')
                print('Roth: One-third of the enemy-ships are destroyed')
                firepower_factor = 0.30
                losses_factor = 0.30

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor')
                print('Roth: One-fifth of the enemy ships are destroyed')

                firepower_factor = 0.20
                losses_factor = 0.30

                enemy_group_strength = update_enemy_group_strength(effective_enemy_strength, enemy_group_strength, firepower_factor)
                
                enemy_losses = update_enemy_losses(enemy_losses, effective_enemy_strength, firepower_factor)
                
                player_ships = update_player_ships(effective_enemy_firepower, losses_factor)
                
                player_losses = update_player_losses(effective_enemy_firepower, losses_factor)

        for key, value in enemy_group_strength.items():
            print(f'The enemy now has {value} {key}')
            
        for key, value in player_ships.items():
            print(f'We now have {value} {key}')
        
        """
        for key, value in enemy_losses.items():
            print(f'The enemy have lost {value} {key} in total')
        
        for key, value in player_losses.items():
            print(f'We have lost {value} {key} in total')
        
        INCLUDED FOR CHECKING PURPOSES ONLY
        """

        if player_ships['battleships'] == 0 and player_ships['cruisers'] == 0 and player_ships['escorts'] == 0:
            print('Roth: Shields failing Admiral!')
            print('Roth: Multiple hull breaches!')
            print('Roth: The reactor is melting down!')
            print('Roth: Oh Sh......')
            print('Your tactical decisions have led to the destruction of your fleet')
            new_game_decision = input('Would you like to try again?\n')
            if new_game_decision =='y':
                new_game()
            elif new_game_decision == 'n':
                main()

        elif enemy_group_strength['battleships'] > 0 or enemy_group_strength['cruisers'] > 0 or enemy_group_strength['escorts'] > 0:
            print('Roth: The enemy group has still active ships Admiral!')
            print('Roth: Shall we re-engage?')
            reengage_decision = input('Press y to re-engage the enemy, or n to leave them for follow-on forces:\n')
            if reengage_decision == 'y':
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            elif reengage_decision == 'n':
                print('You: We have done enough damage, and I do not want to risk our ships further')
                enemy_bypassed = update_enemy_bypassed(enemy_group_strength)
                """
                for key, value in enemy_bypassed.items():
                    print(f'We have bypassed {value} {key}')
                """
        
        elif enemy_group_strength['battleships'] == 0 and enemy_group_strength['cruisers'] == 0 and enemy_group_strength['escorts'] == 0:
            print('Roth: We have destroyed all enemy ships, Admiral')
            print('Roth: We are clear to move on')
        
    fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)



def firepower_comparator(player_firepower, enemy_firepower):
    """
    Called each time player fleet and enemy fleet fight. Compares firepower ratings to determine outcome
    """
    firepower_difference = player_firepower - enemy_firepower
    return firepower_difference


def calculate_effective_enemy_firepower(effective_enemy_strength):
    effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))
    return effective_enemy_firepower


def calculate_effective_enemy_strength(enemy_group_strength, target_factor):
    effective_enemy_strength = {
        'battleships': math.ceil(enemy_group_strength['battleships'] * target_factor),
        'cruisers': math.ceil(enemy_group_strength['cruisers'] * target_factor),
        'escorts': math.ceil(enemy_group_strength['escorts'] * target_factor)
    }
    return effective_enemy_strength


def enemy_firepower_calculator(enemy_strength):
    """
    function to calculate the firepower rating of an enemy fleet
    """
    battleship_firepower = 20
    cruiser_firepower = 10
    escort_firepower = 5
    # possibly refactor this to use the firepower dictionary
    # Can you multiply the values of two dictionaries?
    enemy_firepower = ((enemy_strength['battleships'] * battleship_firepower)
                        + (enemy_strength['cruisers'] * cruiser_firepower)
                        + (enemy_strength['escorts'] * escort_firepower))
    return enemy_firepower


def update_enemy_bypassed(enemy_group_strength):
    """
    Updates global enemy_bypassed dictionary
    Keeps track of the number of enemy ships that have 
    been bypassed
    """
    global enemy_bypassed
    enemy_bypassed = {
        'battleships': enemy_group_strength['battleships'],
        'cruisers': enemy_group_strength['cruisers'],
        'escorts': enemy_group_strength['escorts']
    }
    return enemy_bypassed


def player_fleet_status():
    """
    Function that can be called anytime to display the current status of the player's fleet
    """
    for key, value in player_ships.items():
        print(f'We currently have {value} {key}')
    print(f"Given the current number of ships, we currently have {player_firepower} turrets")


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






def main():
    """
    Contains main program functions
    """
    print('Welcome to Fleet Command, a space battle simulator game')
    
    print('The Alliance, a confederation of democratically-ruled star-systems, has been at war with the autocratic Syndicate Worlds for 20 years\n')
    print('The war shows no sign of ending, as both sides are locked in a stalemate\n')
    print('Do you want to start a new game?')
    new_game_decision = input('Press y to start the game:\n')
    if new_game_decision == 'y':
        print('You are a promising young naval officer, and you have just been given command of a fleet\n')
        print('The Syndicate Worlds have gathered a mighty fleet, and have attacked at multiple points\n')
        print('You have been charged with defending the Alliance\n')

        new_game()
    


main()
