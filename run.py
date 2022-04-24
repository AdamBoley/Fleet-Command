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

ship_firepower = {
    'battleship': 20,
    'cruiser': 10,
    'escort': 5,
}


tactical_library = {
    '1': 'attack 25% of the enemy',
    '2': 'attack 50% of the enemy',
    '3': 'attack 66% of the enemy',
    '4': 'attack all of the enemy'
}

player_firepower = (
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
            effective_enemy_strength = {
                'battleships': math.ceil(enemy_group_strength['battleships'] / 4),
                'cruisers': math.ceil(enemy_group_strength['cruisers'] / 4),
                'escorts': math.ceil(enemy_group_strength['escorts'] / 4)
            }
            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')
            
            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge! Almost all of the targetted enemy ships are destroyed!')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.90)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.90)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.90))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.90),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.90),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.90)
                }
                
                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.01),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.01),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.01)
                }
                                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.01),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.01),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.01)
                }

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable. A large number of the targeted enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.80)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.80)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.80))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.80),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.80),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.80)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.02),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.02),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.02)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.02),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.02),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.02)
                }

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor. A moderate number of enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.70)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.70)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.70))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.70),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.70),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.70)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.03),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.03),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.03)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.03),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.03),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.03)
                }
            
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
        
        elif tactic == '2':
            print('You: We will aim to hit half of their ships in our firing run')
            
            effective_enemy_strength = {
                'battleships': math.ceil(enemy_group_strength['battleships'] / 2),
                'cruisers': math.ceil(enemy_group_strength['cruisers'] / 2),
                'escorts': math.ceil(enemy_group_strength['escorts'] / 2)
            }
            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge! Almost all of the targetted enemy ships are destroyed!')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.70)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.70)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.70))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.70),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.70),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.70)
                }
                
                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.05),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.05),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.05)
                }
                                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.05),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.05),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.05)
                }

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable. A large number of the targeted enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.60)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.60)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.60))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.60),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.60),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.60)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.10),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.10),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.10)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.10),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.10),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.10)
                }

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor. A moderate number of enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.50)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.50)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.50))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.50),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.50),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.50)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.15),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.15),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.15)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.15),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.15),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.15)
                }
            
            for key, value in enemy_group_strength.items():
                print(f'The enemy now has {value} {key}')
            
            for key, value in player_ships.items():
                print(f'We now have {value} {key}')
        
        elif tactic == '3':
            print('You: We will aim to hit two-thirds of them in our firing run')
            
            effective_enemy_strength = {
                'battleships': math.ceil(enemy_group_strength['battleships'] * 0.66),
                'cruisers': math.ceil(enemy_group_strength['cruisers'] * 0.66),
                'escorts': math.ceil(enemy_group_strength['escorts'] * 0.66)
            }
            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge! Almost all of the targetted enemy ships are destroyed!')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.60)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.60)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.60))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.50),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.50),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.50)
                }
                
                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.10),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.10),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.10)
                }
                                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.10),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.10),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.10)
                }

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable. A large number of the targeted enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.50)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.50)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.50))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.50),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.50),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.50)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.15),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.15),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.15)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.15),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.15),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.15)
                }

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor. A moderate number of enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.40)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.40)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.40))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.40),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.40),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.40)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.20),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.20),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.20)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.20),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.20),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.20)
                }
            
            for key, value in enemy_group_strength.items():
                print(f'The enemy now has {value} {key}')
            
            for key, value in player_ships.items():
                print(f'We now have {value} {key}')
        
        elif tactic == '4':
            print('You: Maximum attack! Target all enemy ships!')
            
            effective_enemy_strength = {
                'battleships': (enemy_group_strength['battleships']),
                'cruisers': (enemy_group_strength['cruisers']),
                'escorts': (enemy_group_strength['escorts'])
            }
            for key, value in effective_enemy_strength.items():
                print(f'Roth: We will be facing {value} {key}')

            effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))

            print(f'Roth: We will face {effective_enemy_firepower} enemy turrets')
            effective_firepower_difference = firepower_comparator(player_firepower, effective_enemy_firepower)
            print(f'Roth: With this tactic, we will have {effective_firepower_difference} more turrets than the enemy')
            print('Roth: Engaging per your orders Admiral!')

            if effective_firepower_difference > 1000:
                print('Roth: Our local firepower advantage was huge! Almost all of the targeted enemy ships are destroyed!')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.40)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.40)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.40))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.40),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.40),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.40)
                }
                
                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.20),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.20),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.20)
                }
                                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.20),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.2),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.20)
                }

            elif effective_firepower_difference >= 500:
                print('Roth: Our local firepower advantage was considerable. A large number of the targeted enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.30)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.30)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.30))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.30),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.30),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.30)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.25),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.25),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.25)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.25),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.25),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.25)
                }

            elif effective_firepower_difference < 500:
                print('Roth: Our local firepower advantage was minor. A moderate number of enemy ships are destroyed')
                enemy_group_strength = {
                   'battleships': (enemy_group_strength['battleships'] - math.ceil(effective_enemy_strength['battleships'] * 0.20)),
                   'cruisers': (enemy_group_strength['cruisers'] - math.ceil(effective_enemy_strength['cruisers'] * 0.20)),
                   'escorts': (enemy_group_strength['escorts'] - math.ceil(effective_enemy_strength['escorts'] * 0.20))
                }

                enemy_losses = {
                    'battleships': enemy_losses['battleships'] + math.ceil(effective_enemy_strength['battleships'] * 0.20),
                    'cruisers': enemy_losses['cruisers'] + math.ceil(effective_enemy_strength['cruisers'] * 0.20),
                    'escorts': enemy_losses['escorts'] + math.ceil(effective_enemy_strength['escorts'] * 0.20)
                }

                player_ships = {
                    'battleships': player_ships['battleships'] - math.floor((effective_enemy_firepower / 5) * 0.30),
                    'cruisers': player_ships['cruisers'] - math.ceil((effective_enemy_firepower / 2) * 0.30),
                    'escorts': player_ships['escorts'] - math.ceil(effective_enemy_firepower * 0.3)
                }
                
                player_losses = {
                    'battleships': player_losses['battleships'] + math.floor((effective_enemy_firepower / 5) * 0.3),
                    'cruisers': player_losses['cruisers'] + math.ceil((effective_enemy_firepower / 2) * 0.3),
                    'escorts': player_losses['escorts'] + math.ceil(effective_enemy_firepower * 0.3)
                }
            
            for key, value in enemy_group_strength.items():
                print(f'The enemy now has {value} {key}')
            
            for key, value in player_ships.items():
                print(f'We now have {value} {key}')

        if enemy_group_strength['battleships'] > 0 or enemy_group_strength['cruisers'] > 0 or enemy_group_strength['escorts'] > 0:
            print('Roth: The enemy group has still active ships Admiral!')
            print('Roth: Shall we re-engage?')
            reengage_decision = input('Press y to re-engage the enemy, or n to leave them for follow-on forces:\n')
            if reengage_decision == 'y':
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            elif reengage_decision == 'n':
                print('You: We have done enough damage, and I do not want to risk our ships further')
        
        elif enemy_group_strength['battleships'] == 0 and enemy_group_strength['cruisers'] == 0 and enemy_group_strength['escorts'] == 0:
            print('Roth: We have destroyed all enemy ships, Admiral')
            print('We are clear to move on')

    fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)



def firepower_comparator(player_firepower, enemy_firepower):
    """
    Called each time player fleet and enemy fleet fight. Compares firepower ratings to determine outcome
    """
    firepower_difference = player_firepower - enemy_firepower
    return firepower_difference


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
    player_name = input('Please enter your name:\n')
    print(f'Greetings Admiral {player_name}\n')
    print('The Alliance, a confederation of democratically-ruled star-systems, has been at war with the autocratic Syndicate Worlds for 20 years\n')
    print('The war shows no sign of ending, as both sides are locked in a stalemate\n')
    print('You are a promising young naval officer, and you have just been given command of a fleet\n')
    print('The Syndicate Worlds have gathered a mighty fleet, and have attacked at multiple points\n')
    print(f'{player_name}, you have been charged with defending the Alliance\n')

    new_game(player_name)


main()
