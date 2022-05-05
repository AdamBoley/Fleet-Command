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

player_local_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

player_battle_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

enemy_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

enemy_local_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

enemy_battle_losses = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
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

ship_crew = {
    'battleship': 2000,
    'cruiser': 1000,
    'escort': 200
}

minimum_ship_crew = {
    'battleship': int(ship_crew['battleship'] * 0.80),
    'cruiser': int(ship_crew['cruiser'] * 0.80),
    'escort': int(ship_crew['escort'] * 0.80)
}

player_experience = 1.0

recovered_crew = {
    'battleship': int(ship_crew['battleship'] * 0.60),
    'cruiser': int(ship_crew['cruiser'] * 0.50),
    'escort': int(ship_crew['escort'] * 0.40)
}

total_crew = (
    ship_crew['battleship'] * player_ships['battleships']
    + ship_crew['cruiser'] * player_ships['cruisers']
    + ship_crew['escort'] * player_ships['escorts']
)

excess_crew = (
    total_crew - (
        minimum_ship_crew['battleship'] * player_ships['battleships']
        + minimum_ship_crew['cruiser'] * player_ships['cruisers']
        + minimum_ship_crew['escort'] * player_ships['escorts']
    )
)

missile_volleys = 3

missile_launchers = {
    'battleships': 4,
    'cruisers': 2,
    'escorts': 1
}

mine_stocks = 3

mine_layers = {
    'battleships': 2,
    'cruisers': 1
}

tactical_library = {
    '1': 'attack 25% of the enemy',
    '2': 'attack 50% of the enemy',
    '3': 'attack 75% of the enemy',
    '4': 'attack all of the enemy',
    '5': 'launch a missile barrage',
    '6': 'lay a stealth mine-field'
}

boarding_tactics = {
    '1': 'We can board a battleship',
    '2': 'We can board a cruiser',
    '3': 'We can board an escort',
    '4': 'We can stop boarding enemy ships',
    '5': 'We can board all of the enemy ships at once'
}

marines = (
    (player_ships['battleships'] * 40)
    + (player_ships['cruisers'] * 20)
)

marine_experience = 1.0

marine_experience_gains = {
    'battleship': 0.05,
    'cruiser': 0.03,
    'escort': 0.01
}

boarded_ships = {
    'battleship': 0,
    'cruiser': 0,
    'escort': 0
}

player_name = ''
flagship_name = ''
player_supplies = 100


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
    fleet_status_decision = input('Please press y to see fleet status or n to move on:\n')  # gonna need some input checking here
    if fleet_status_decision == 'y':
        player_fleet_status()
    else:
        print('Roth: Very well Admiral')
    print('Roth: Do you want to see the capabilities of our ships?')
    fleet_capabilities_decision = input('Please press y to see what each part of your fleet is capable of, or n to move on\n')
    if fleet_capabilities_decision == 'y':
        ship_capabilities()
    else:
        print('Indeed - a good naval officer should know the capabilities of their ships by heart')
    print('Roth: I wonder, Admiral, could you tell me what tactics we can use?')
    explain_tactics = input('Press y to get an explanation of what tactics you can employ, or n to move on:\n')
    if explain_tactics == 'y':
        print('You: Of course, Captain')
        tactics()
    elif explain_tactics == 'n':
        print('You: You will just have to watch and learn Roth.')
    print('Roth: Now that is done, I will brief you, Admiral')
    print('Roth: The Syndicate Worlds have launched major attacks at multiple points along the frontier. '
    + 'Our fleet has been assembled to stop the enemy and plug the holes in our lines. '
    + 'Other Alliance forces are assembling behind us, and will be able to stop any enemy ships that slip past us. '
    + 'That said, high command wants does not want our forces bogged down chasing enemy groups unncessessarily. '
    + 'They are already planning a counter-punch, and they want as many ships for that as they can get. '
    + 'So, we should try to avoid leaving strong enemy groups behind us. '
    + 'However, our follow-on forces might appreciate some target practice. '
    + 'I have some reports that allied forces are engaging the enemy in other systems. '
    + 'It is possible that if we help them out, they could reinforce us.\n')
    print("You: Thank you Captain - let's go save the Alliance!")
    mission_one()


def mission_one():
    """
    Mission one
    light combat with no real consequences
    intended as an introduction to the game
    """
    print('\n  BEGIN MISSION ONE  \n')
    global player_experience
    enemy_group_one = {
        'battleships': 4,
        'cruisers': 8,
        'escorts': 20
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_one)
    player_firepower = calculate_player_firepower(player_ships)
    print('This is the first mission - you can expect light combat with no real consequences to your actions, so experiment and get a feel for the game.\n')
    print(f'Roth: Admiral {player_name}, sensors have detected a group of enemy warships at the jump point from Salamis!')
    print('Roth: The tactical suite is updating now - this group looks small')
    for key, value in enemy_group_one.items():
        print(f'Roth: The enemy have {value} {key}')
    print(f'Roth: The enemy ships have a total of {enemy_firepower} turrets')
    print('Roth: Based on that, I assess this is a scouting unit')
    
    firepower_difference = firepower_comparator(player_firepower, enemy_firepower)
    print(f'Roth: We have {firepower_difference} more turrets than they do')
    
    print('Roth: Admiral, if we choose, we should be able to take them easily!')
    print('Roth: Admiral, shall we engage?')
    engage_decision_mission_one = input('Press y to engage the enemy, or n to find worthier prey:\n')
    if engage_decision_mission_one == 'y':
        print('You: We engage! All hands - battle stations!')
        fight_battle(enemy_firepower, enemy_group_one)
        player_experience += 0.1
        print('Roth: Congratulations Admiral - the gunnery crews are already notching their barrels.')
    elif engage_decision_mission_one == 'n':
        print('You: This is not worth our time. Disengage and leave them for follow-on forces.')
        print('Roth: Discretion is the better part of valour, Admiral')
        update_enemy_bypassed(enemy_group_one)
    
    print('Roth: Admiral, that enemy group came from the neighbouring system of Salamis. '
        + 'Given their size, they were almost certain detached from a larger group. ')
    print('You: I concur - we can expect heavy resistance at Salamis. '
        + 'All hands, stand down and prepare for FTL. '
        + 'Roth, lay course for Salamis.')
    mission_two()


def mission_two():
    """
    Mission Two - heavier combat, requires the player to use their
    experience from Mission One to win
    """
    global player_experience
    print('\n  BEGIN MISSION TWO  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    fleet_status_decision = input('Please press y to see fleet status or n to begin the mission:\n')  # gonna need some input checking here
    if fleet_status_decision == 'y':
        player_fleet_status()
    else:
        print('Roth: Very well Admiral')
    print('Roth: Arriving at Salamis in 3....2...1')
    print('Roth: Looks like the enemy is here in strength, Admiral, as predicted. ')
    enemy_group_two = {
        'battleships': 12,
        'cruisers': 30,
        'escorts': 100
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_two)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_two.items():
        print(f'The enemy group has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(player_firepower, enemy_firepower)
    print(f'Roth: We have {firepower_difference} more turrets than they do')

    print('Roth: This will be a tough battle, Admiral')
    print('Roth: Shall we engage?')
    engage_decision_mission_two = input('press y to engage, or n to disengage:\n')
    if engage_decision_mission_two == 'y':
        print('You: Indeed we shall, we cannot allow a force of this strength to roam free')
        fight_battle(enemy_firepower, enemy_group_two)
        player_experience += 0.1
    elif engage_decision_mission_two == 'n':
        print('You: I think not - follow-on forces should be able to handle them')
        update_enemy_bypassed(enemy_group_two)


def update_enemy(effective_enemy_strength, enemy_group_strength, firepower_factor, enemy_losses, player_experience):
    """
    Updates enemy_group_strength dictionary
    Updates global enemy_losses dictionary
    Returns updated enemy_group_strength dictionary to fight_engagement
    """
    #  4x repetition here - refactor into variables
    global enemy_local_losses
    global enemy_battle_losses
    enemy_battleship_losses = math.ceil(effective_enemy_strength['battleships'] * firepower_factor * player_experience)
    enemy_cruiser_losses = math.ceil(effective_enemy_strength['cruisers'] * firepower_factor * player_experience)
    enemy_escort_losses = math.ceil(effective_enemy_strength['escorts'] * firepower_factor * player_experience)

    enemy_group_strength = {
        'battleships': (enemy_group_strength['battleships'] - enemy_battleship_losses),
        'cruisers': (enemy_group_strength['cruisers'] - enemy_cruiser_losses),
        'escorts': (enemy_group_strength['escorts'] - enemy_escort_losses)
    }

    enemy_losses = {
        'battleships': enemy_losses['battleships'] + enemy_battleship_losses,
        'cruisers': enemy_losses['cruisers'] + enemy_cruiser_losses,
        'escorts': enemy_losses['escorts'] + enemy_escort_losses
    }

    enemy_local_losses = {
        'battleships': enemy_battleship_losses,
        'cruisers': enemy_cruiser_losses,
        'escorts': enemy_escort_losses
    }

    enemy_battle_losses = {
        'battleships': enemy_battle_losses['battleships'] + enemy_battleship_losses,
        'cruisers': enemy_battle_losses['cruisers'] + enemy_cruiser_losses,
        'escorts': enemy_battle_losses['escorts'] + enemy_escort_losses
    }

    return enemy_group_strength


def update_player(losses_factor):
    """
    Updates global player_losses dictionary
    Updates global player_ships dictionary
    Checks if player_ships dictionary contains negative values,
    and corrects to 0 if so
    Returns updated player_ships dictionary
    """
    #  4x repetition here - refactor into variables
    global player_ships
    global player_losses
    global player_local_losses
    global player_battle_losses

    player_battleship_losses = math.floor(player_ships['battleships'] * losses_factor)
    player_cruiser_losses = math.floor(player_ships['cruisers'] * losses_factor)
    player_escort_losses = math.ceil(player_ships['escorts'] * losses_factor)

    player_losses = {
        'battleships': player_losses['battleships'] + player_battleship_losses,
        'cruisers': player_losses['cruisers'] + player_cruiser_losses,
        'escorts': player_losses['escorts'] + player_escort_losses
    }

    player_local_losses = {
        'battleships': player_battleship_losses,
        'cruisers': player_cruiser_losses,
        'escorts': player_escort_losses
    }

    player_battle_losses = {
        'battleships': player_battle_losses['battleships'] + player_battleship_losses,
        'cruisers': player_battle_losses['cruisers'] + player_cruiser_losses,
        'escorts': player_battle_losses['escorts'] + player_escort_losses
    }
        
    player_ships = {
        'battleships': player_ships['battleships'] - player_battleship_losses,
        'cruisers': player_ships['cruisers'] - player_cruiser_losses,
        'escorts': player_ships['escorts'] - player_escort_losses
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


def fight_battle(enemy_firepower, enemy_group_strength):
    """
    Function that is called when the player
    decides to fight an enemy in a mission
    """
    print('Roth: How shall we engage?')

    starting_enemy_ships = {
        'battleships': enemy_group_strength['battleships'],
        'cruisers': enemy_group_strength['cruisers'],
        'escorts': enemy_group_strength['escorts']
    }

    def fight_engagement(enemy_firepower, enemy_group_strength):
        """
        A long, complex function that is called for each firing run
        """
        global enemy_losses
        global player_ships
        global player_losses
        global player_supplies
        global player_battle_losses
        global enemy_battle_losses
        global total_crew

        player_firepower = calculate_player_firepower(player_ships)
        
        print(f'WE HAVE {player_firepower} TURRETS')  # remove this once development is finished
        for key, value in enemy_group_strength.items():
            print(f'The enemy have {value} {key}')

        print('You: we have several options:')
        for key, value in tactical_library.items():
            print(f'{key} - We can {value}')
        
        tactic = input('Type a number from 1 to 6 to select your tactic:\n')
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
            
            firepower_factor = (effective_firepower_difference / player_firepower)
            losses_factor = (effective_enemy_firepower / effective_firepower_difference) / 10

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)

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

            firepower_factor = (effective_firepower_difference / player_firepower)
            losses_factor = (effective_enemy_firepower / effective_firepower_difference) / 7

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)
        
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

            firepower_factor = (effective_firepower_difference / player_firepower)
            losses_factor = (effective_enemy_firepower / effective_firepower_difference) / 5

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)
        
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

            firepower_factor = (effective_firepower_difference / player_firepower)
            losses_factor = (effective_enemy_firepower / effective_firepower_difference) / 3

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)

        elif tactic == '5':
            global missile_volleys
            print('You: Fire missiles!')
            if missile_volleys >= 2:
                print(f'Roth: We currently have enough missiles for {missile_volleys} barrages')
            elif missile_volleys == 1:
                print('Roth: We currently have enough missiles for 1 barrage')
            elif missile_volleys > 0 and missile_volleys < 1:
                print('Roth: We have some missiles, but not enough to break through enemy point defences')
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            elif missile_volleys == 0:
                print('Roth: We currently have no missiles remaining')
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            
            target_factor = 1

            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)
            missiles_fired = (
                player_ships['battleships'] * missile_launchers['battleships']
                + player_ships['cruisers'] * missile_launchers['cruisers']
                + player_ships['escorts'] * missile_launchers['escorts']
            )

            for key, value in effective_enemy_strength.items():
                print(f'Roth: Our missiles will target {value} {key}')
            
            effective_enemy_firepower = calculate_effective_enemy_firepower(effective_enemy_strength)
            print('Roth: Our missiles have a long range')
            print('Roth: We will not face any return fire')
            print(f'Roth: Based on the number of ships we have, we will fire {missiles_fired} missiles')
            print('Roth: Engaging with a missile barrage')

            firepower_factor = (missiles_fired / effective_enemy_firepower)
            if firepower_factor > 1:
                firepower_factor = 1
            losses_factor = 0

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)
            missile_volleys -= 1
            print(f'Roth: We now have enough missiles for {missile_volleys} barrages')
        
        elif tactic == '6':
            global mine_stocks
            print('You: We will layer a minefield and lure the enemy into it')
            if mine_stocks >= 2:
                print(f'Roth: We currently have enough mines for {mine_stocks} fields')
            elif mine_stocks == 1:
                print('Roth: We currently have enough mines for 1 minefield')
            elif mine_stocks > 0 and mine_stocks < 1:
                print('Roth: We have some mines, but not enough to lay a decent field')
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            elif mine_stocks == 0:
                print('Roth: We currently have no mines remaining')
                fight_engagement(enemy_firepower, player_firepower, enemy_group_strength)
            
            target_factor = 1
            effective_enemy_strength = calculate_effective_enemy_strength(enemy_group_strength, target_factor)
            mines_laid = (
                player_ships['battleships'] * mine_layers['battleships']
                + player_ships['cruisers'] * mine_layers['cruisers']
            )
            for key, value in effective_enemy_strength.items():
                print(f'Roth: Our mines will target {value} {key}')
            
            print('Roth: Since we are luring the enemy into a trap, we will not face return fire')
            print('Roth: However, we will need to manoeuvre a lot to lay the minefield and get out of enemy weapons range')
            print(f'Roth: Based on the number of capital ships we have, we will lay {mines_laid} mines')
            print('Roth: Laying a minefield')

            total_enemy_ships = (
                effective_enemy_strength['battleships']
                + effective_enemy_strength['cruisers']
                + effective_enemy_strength['escorts']
            )
            firepower_factor = (mines_laid / total_enemy_ships) / 2
            if firepower_factor > 1:
                firepower_factor = 1
            losses_factor = 0

            enemy_group_strength = update_enemy(
                    effective_enemy_strength, enemy_group_strength,
                    firepower_factor, enemy_losses, player_experience)
            player_ships = update_player(losses_factor)
            player_supplies -= 1
            mine_stocks -= 1
            print(f'Roth: We now have enough mines for {mine_stocks} mine-fields')

        player_supplies -= 1
        print(f'We now have {player_supplies} supplies')

        for key, value in enemy_local_losses.items():
            print(f'We destroyed {value} enemy {key}')

        for key, value in enemy_group_strength.items():
            print(f'The enemy now has {value} {key}')
        
        for key, value in player_local_losses.items():
            print(f'That run cost us {value} {key}')
            
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
            print('Would you like to try again?')
            new_game_decision = input('Press y to try again or n to quit')
            if new_game_decision == 'y':
                new_game()
            elif new_game_decision == 'n':
                main()

        elif player_supplies == 0:
            print('Roth: Admiral, our ships are out of fuel and ammunition!')
            print('Roth: Enemy ships closing in!')
            print('Roth: We cannot fight back!')
            print('You: Very well, broadcast surrender')
            print('You have run out of supplies and have lost the game')
            print('Next time, keep an eye on your supply levels and conserve them')
            print('Would you like to try again?')
            new_game_decision = input('Press y to try again or n to quit')
            if new_game_decision == 'y':
                new_game()
            elif new_game_decision == 'n':
                main()

        elif enemy_group_strength['battleships'] > 0 or enemy_group_strength['cruisers'] > 0 or enemy_group_strength['escorts'] > 0:
            print('Roth: The enemy group has still active ships Admiral!')
            print('Roth: Shall we re-engage?')
            reengage_decision = input('Press y to re-engage the enemy, or n to leave them for follow-on forces:\n')
            if reengage_decision == 'y':
                print('You: Indeed we shall! Good hunting!')
                fight_engagement(enemy_firepower, enemy_group_strength)
            elif reengage_decision == 'n':
                print('You: We have done enough damage, and I do not want to risk our ships further')
                enemy_bypassed = update_enemy_bypassed(enemy_group_strength)
                for key, value in enemy_battle_losses.items():
                    print(f'Roth: We destroyed {value} {key}')
                
                for key, value in player_battle_losses.items():
                    print(f'Roth: We lost {value} {key}')
                
                total_crew_calculator()
                excess_crew_calculator()

                player_battle_losses = {
                'battleships': 0,
                'cruisers': 0,
                'escorts': 0
                }

                enemy_battle_losses = {
                'battleships': 0, 
                'cruisers': 0,
                'escorts': 0
                }
                #  possible call a reset_battle_losses function to reset player_battle_losses and enemy_battle_losses
                """
                for key, value in enemy_bypassed.items():
                    print(f'We have bypassed {value} {key}')
                """
        
        elif enemy_group_strength['battleships'] == 0 and enemy_group_strength['cruisers'] == 0 and enemy_group_strength['escorts'] == 0:
            print('Roth: We have knocked out all enemy ships, Admiral')
            for key, value in enemy_battle_losses.items():
                    print(f'Roth: We destroyed {value} {key}')
                
            for key, value in player_battle_losses.items():
                print(f'Roth: We lost {value} {key}')
            
            total_crew_calculator()
            excess_crew_calculator()
            
            player_battle_losses = {
                'battleships': 0,
                'cruisers': 0,
                'escorts': 0
            }

            enemy_battle_losses = {
                'battleships': 0, 
                'cruisers': 0,
                'escorts': 0
            }
            #  possible call a reset_battle_losses function to reset player_battle_losses and enemy_battle_losses

            print('Roth: Some of the enemy ships may be salvagable')
            boardable_ships = {
                'battleships': math.floor(starting_enemy_ships['battleships'] * 0.20),
                'cruisers': math.floor(starting_enemy_ships['cruisers'] * 0.15),
                'escorts': math.floor(starting_enemy_ships['escorts'] * 0.10)
            }
            
            print('Roth: Shall we attempt to board the enemy ships?')
            boarding_decision = input('Press y to board and capture the enemy ships, or n to move on:\n')
            if boarding_decision == 'y':
                print('You: Yes, hopefully we can bolster our numbers')
                boarding_operation(boardable_ships)
            if boarding_decision == 'n':
                print('You: I would rather not waste our Marines and supplies on these wrecks')
                print('Roth: Very well, We are clear to move on')
        
    fight_engagement(enemy_firepower, enemy_group_strength)


def total_crew_calculator():
    """
    Function that is called in the fight_engagement and
    player_fleet_status functions to calculate the total crew available to the player
    """
    global total_crew
    total_crew = total_crew - ((
        player_battle_losses['battleships'] * ship_crew['battleship']
        + player_battle_losses['cruisers'] * ship_crew['cruiser']
        + player_battle_losses['escorts'] * ship_crew['escort'])
        -
        (player_battle_losses['battleships'] * recovered_crew['battleship']
        + player_battle_losses['cruisers'] * recovered_crew['cruiser']
        + player_battle_losses['escorts'] * recovered_crew['escort']))
    return total_crew


def excess_crew_calculator():
    """
    Function that is called in the fight_engagement and
    player_fleet_status functions to calculate the excess crew available to the player
    for boarding actions
    """
    global excess_crew
    excess_crew = total_crew - (
        minimum_ship_crew['battleship'] * player_ships['battleships']
        + minimum_ship_crew['cruiser'] * player_ships['cruisers']
        + minimum_ship_crew['escort'] * player_ships['escorts']
    )
    return excess_crew
    

def firepower_comparator(player_firepower, enemy_firepower):
    """
    Called each time player fleet and enemy fleet fight
    Compares firepower ratings to determine outcome
    """
    firepower_difference = player_firepower - enemy_firepower
    return firepower_difference


def calculate_effective_enemy_firepower(effective_enemy_strength):
    """
    Calculates the total number of turrets in the part of the enemy
    group that the plater has chosen to attack
    """
    effective_enemy_firepower = (
                (effective_enemy_strength['battleships'] * 20)
                + (effective_enemy_strength['cruisers'] * 10)
                + (effective_enemy_strength['escorts'] * 5))
    return effective_enemy_firepower


def calculate_effective_enemy_strength(enemy_group_strength, target_factor):
    """
    Calculates the number of enemy ships in the part of the enemy
    group thatthe player has chosen to attack
    """
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
    Keeps track of the number of enemy ships that have been bypassed
    """
    global enemy_bypassed
    enemy_bypassed = {
        'battleships': enemy_group_strength['battleships'],
        'cruisers': enemy_group_strength['cruisers'],
        'escorts': enemy_group_strength['escorts']
    }
    return enemy_bypassed


def calculate_player_firepower(player_ships):
    """
    Dynamically calculates player firepower based on the number of ships they have
    """
    player_firepower = (
        (player_ships['battleships'] * ship_firepower['battleship'])
        + (player_ships['cruisers'] * ship_firepower['cruiser'])
        + (player_ships['escorts'] * ship_firepower['escort'])
    )
    return player_firepower


def boarding_operation(boardable_ships):
    """
    Called when the player wants to board and salvage enemy ships after a battle has been won
    """
    global marines
    global player_ships
    global player_supplies
    global total_crew
    global excess_crew
    global marine_experience
    global boarded_ships
    
    available_crew = excess_crew_calculator()

    if boardable_ships['battleships'] == 0 and boardable_ships['cruisers'] == 0 and boardable_ships['escorts'] == 0:
        print('Roth: There are no more ships left to board\n')
    elif marines < 20:
        print('Roth: We do not have enough marines to attempt to board even one escort')
    elif available_crew < 160:
        print('Roth: We do not have enough crew left to crew a captured ship')
    else:
        for key, value in boardable_ships.items():
            print(f'Roth: There are {value} {key} we can board')
        print(f'Roth: We have {marines} marines')
        print(f'Roth: We have {available_crew} sailors available')
        print(f'Roth: We have {player_supplies} repair supplies')
        for key, value in boarding_tactics.items():
            print(f'Roth: {key} - {value}')
        print('Roth: What shall our Marines board first?')

        ship_to_board = input('Enter a number from 1 to 3 to select a class of enemy ship to board, enter 4 to stop boarding enemy ships, or enter 5 to board all remaining enemy ships:\n')
        if ship_to_board == '1':
            print('You: We shall board an enemy battleship')
            if boardable_ships['battleships'] == 0:
                print('Roth: There are no enemy battleships to board')
                boarding_operation(boardable_ships)
            elif marines < 500:
                print('Roth: We do not have enough marines to board an enemy battleship')
                print('Roth: We might have enough to board an enemy cruiser')
                boarding_operation(boardable_ships)
            else:
                print('Roth: Very well, we will need 500 Marines to board and take a battleship')
                boardable_ships['battleships'] -= 1
                marine_casualties = int(500 - (marine_experience * 250))
                marines -= marine_casualties
                player_ships['battleships'] += 1
                boarded_ships['battleship'] += 1
                player_supplies -= 1
                excess_crew -= minimum_ship_crew['battleship']
                print(f'Roth: We lost {marine_casualties} Marines to their internal defences, but the battleship has been taken')
                boarding_operation(boardable_ships)
            
        elif ship_to_board == '2':
            print('You: We shall board an enemy cruiser')
            if boardable_ships['cruisers'] == 0:
                print('Roth: There are no enemy cruisers to board')
                boarding_operation(boardable_ships)
            elif marines < 120:
                print('Roth: We do not have enough marines to board an enemy cruiser')
                print('Roth: But we might have enough to board an enemy escort')
                boarding_operation(boardable_ships)
            else:
                print('Roth: Very well, we will need 120 Marines to board and take a cruiser')
                boardable_ships['cruisers'] -= 1
                marine_casualties = int(120 - (marine_experience * 80))
                marines -= marine_casualties
                player_ships['cruisers'] += 1
                boarded_ships['cruiser'] += 1
                player_supplies -= 1
                excess_crew -= minimum_ship_crew['cruiser']
                print(f'Roth: We lost {marine_casualties} Marines, but the cruiser has been added to our fleet')
                boarding_operation(boardable_ships)
        
        elif ship_to_board == '3':
            print('We shall board an enemy escort')
            if boardable_ships['escorts'] == 0:
                print('There are no enemy escorts to board')
                boarding_operation(boardable_ships)
            else:
                print('Roth: Very well, we will need 20 Marines to board and take an escort')
                boardable_ships['escorts'] -= 1
                marine_casualties = int(20 - (marine_experience * 15))
                marines -= marine_casualties
                player_ships['escorts'] += 1
                boarded_ships['escort'] += 1
                player_supplies -= 1
                excess_crew -= minimum_ship_crew['escort']
                print(f'Roth: We lost {marine_casualties} Marines, but the escort has been added to our screen')
                boarding_operation(boardable_ships)
        
        elif ship_to_board == '4':
            print('You: We have salvaged enough ships. Scuttle the rest')
            print('Roth: Indeed Admiral, better to save our Marines for more important work')
        
        elif ship_to_board == '5':
            marines_required = (
                boardable_ships['battleships'] * 500
                + boardable_ships['cruisers'] * 120
                + boardable_ships['escorts'] * 20
            )

            supplies_required = (
                boardable_ships['battleships']
                + boardable_ships['cruisers']
                + boardable_ships['escorts']
            )
            print(f'Roth: We need {marines_required} Marines to do that')
            print(f'Roth: We need {supplies_required} supplies as well')

            if marines < marines_required:
                print('Roth: We do not have enough Marines to board all enemy ships at the same time')
                print('Roth: But we might be able to board some of them one after another')
                boarding_operation(boardable_ships)
            
            elif player_supplies < supplies_required:
                print('Roth: We have insufficient supplies to repair all of the enemy ships')
                print('Roth: But we might be able to repair some of them')
                boarding_operation(boardable_ships)

            elif boardable_ships['battleships'] > 0 or boardable_ships['cruisers'] > 0 or boardable_ships['escorts'] > 0:
                print('You: Board all of them')
                player_ships['battleships'] += boardable_ships['battleships']
                player_ships['cruisers'] += boardable_ships['cruisers']
                player_ships['escorts'] += boardable_ships['escorts']

                boarded_ships['battleship'] += boardable_ships['battleships']
                boarded_ships['cruiser'] += boardable_ships['cruisers']
                boarded_ships['escort'] += boardable_ships['cruisers']

                excess_crew -= (
                    minimum_ship_crew['battleship'] * boardable_ships['battleships']
                    + minimum_ship_crew['cruiser'] * boardable_ships['cruisers']
                    + minimum_ship_crew['escort'] * boardable_ships['escorts']
                )

                marine_casualties_bb = int(boardable_ships['battleships'] * (500 - (marine_experience * 250)))
                marine_casualties_cc = int(boardable_ships['cruisers'] * (120 - (marine_experience * 80)))
                marine_casualties_dd = int(boardable_ships['escorts'] * (20 - (marine_experience * 15)))

                marine_casualties = (
                    marine_casualties_bb
                    + marine_casualties_cc 
                    + marine_casualties_dd
                )
                print(f'Roth: We lost {marine_casualties} marines')
                marines -= marine_casualties
                print(f'Roth: We now have {marines} marines')

                player_supplies -= (
                    boardable_ships['battleships']
                    + boardable_ships['cruisers']
                    + boardable_ships['escorts']
                )

                boardable_ships['battleships'] = 0
                boardable_ships['cruisers'] = 0
                boardable_ships['escorts'] = 0
        
        marine_experience = (
            boarded_ships['battleship'] * marine_experience_gains['battleship']
            + boarded_ships['cruiser'] * marine_experience_gains['cruiser']
            + boarded_ships['escort'] * marine_experience_gains['escort']
        )

        boarded_ships = {
            'battleship': 0,
            'cruiser': 0,
            'escort': 0
        }
    

def player_fleet_status():
    """
    Function that can be called anytime to display the current status of the player's fleet
    """
    player_firepower = calculate_player_firepower(player_ships) 
    total_crew = total_crew_calculator()
    excess_crew = excess_crew_calculator()
    for key, value in player_ships.items():
        print(f'We currently have {value} {key}')
    print(f"Given the current number of ships, we currently have {player_firepower} turrets")
    print(f'Roth: We currently have enough missiles for {missile_volleys} barrages')
    print(f'Roth: We currently have enough mines for {mine_stocks} mine-fields')
    print(f'We currently have {player_supplies} supplies')
    print(f'Our ships carry {marines} Marines')
    print(f'We currently have {total_crew} sailors in the fleet')
    print(f'However, in extremis, we can spare {excess_crew} for other duties if needed')
    if player_experience == 1:
        print('Our crews are trained, but green and inexperienced')
    if player_experience > 1 and player_experience <= 1.3:
        print('Roth: Our crews have gained some battle experience')
    if player_experience > 1.3 and player_experience <= 1.6:
        print('Roth: Our crews are seasoned veterans')
    if player_experience > 1.7:
        print('Roth: Our crews are hardened combat veterans')


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat - heavily armoured and heavily armed')
    print(f"Battleships have {ship_firepower['battleship']} turrets")
    print('Battleships have 4 missile launchers')
    print('Battleships have 2 mine-tubes')
    print(f"Battleships have {ship_crew['battleship']} sailors")
    print(f"However, they can be crewed by {minimum_ship_crew['battleship']} sailors without affecting performance")
    print('Cruisers are midweight combatants')
    print(f"Cruisers have {ship_firepower['cruiser']} turrets")
    print('Cruisers have 2 missile launchers')
    print('Cruisers have 1 mine-tube')
    print(f"Cruisers have {ship_crew['cruiser']} sailors")
    print(f"However, they can be crewed by {minimum_ship_crew['cruiser']} sailors without affecting performance")
    print('Escorts are light screening ships, effective in numbers')
    print(f"Escorts have {ship_firepower['escort']} turrets")
    print('Escorts have 1 missile launcher')
    print('Escorts do not carry mine-tubes')
    print(f"Escorts have {ship_crew['escort']} sailors")
    print(f"However, they can be crewed by {minimum_ship_crew['escort']} sailors without affecting performance\n")


def tactics():
    """
    Function that can be called to inform the player of what tactics they can use
    in an engagement, what the tactic will do and what the consequences are
    """
    print('You: Broadly speaking, we can use 6 tactics:')
    for key, value in tactical_library.items():
        print(f'We can {value}')

    print('You: If we choose to attack 25% of the enemy, ' 
    + 'we will aim to concentrate our firepower against a relatively small number of enemy ships. ' 
    + 'We should destroy many of those ships we target, and suffer few losses, ' 
    + 'but it will take a long time and a lot of ammunition and fuel to wear down a sizeable enemy force\n')

    print('You: If we choose to attack 50% of the enemy, '
    + 'we will spread out our fire more, and be exposed to more enemy fire and hence suffer more casualties, '
    + 'but overall, we will expend less fuel and ammunition\n')
    
    print('You: If we choose to attack 75% of the enemy, we will spread out our fire even more, '
    + 'and could suffer more casualties, but we will end the fight quickly and hence expend much less fuel and ammo. '
    + 'However, given the risk, this approach is best used against weakened enemy groups\n')
    
    print('You: If we choose to attack all of the enemy, '
    + 'we will through caution to the wind - our firepower will be spread out, and we could suffer many casualties '
    + 'but this is the perfect approach to quickly finishing off weakened enemy groups\n')
    
    print('You: We could also choose to fire a barrage of missiles. '
    + 'Missiles are long range weapons, so we will be safe from return fire, but if we use missiles against '
    + 'many enemy ships, they may shoot down many of the missiles. That said, using a missile barrage '
    + 'could be a good way to soften up an enemy group before a conventional firing run. Our ships also do not '
    + 'carry many missiles, so we should use them sparingly and only when necessary\n')
    
    print('You: We could also choose to lay a minefield. '
    + 'If we use a minefield, we will not face any return fire, as we will lay the minefield and lure the enemy into it. '
    + 'Mines are powerful, and since they are stealthed, cannot be shot down. '
    + 'Our ships do not carry many mines, so we should not waste them against small enemy groups\n')

    print('You: Once the battle is done, some enemy ships may be salvageable. '
    + 'These would make excellent additions to the fleet, provided we can spare the crews. '
    + 'Our ships carry Marines, and we can use them to board enemy ships and clear out the crews. '
    + 'This is risky, as the enemy crews will no doubt be dug in and using their internal defences.\n')

    print('Roth: Thank you Admiral, that was informative')
    print('You: You are welcome Roth - watch and learn, and maybe you will command a fleet youself one day')

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
