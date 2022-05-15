"""
run.py file
All dictionaries, variables and functions
necessary for the game to run are contained within this file
"""
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math

player_starting_ships = {
    'battleships': 20,
    'cruisers': 50,
    'escorts': 150
}

player_ships = {
    'battleships': 20,
    'cruisers': 50,
    'escorts': 150,
}

player_total_destroyed = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

player_total_damaged = {
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

player_destroyed_ships = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

player_damaged_ships = {
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

salvaged_ships = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

player_name = ''
flagship_name = ''
starting_supplies = 100
player_supplies = 100

osiris_fleet_helped = 0
osiris_docks_helped = 0

enemy_groups_destroyed = 0
enemy_groups_damaged = 0
enemy_groups_bypassed = 0


def new_game_reset():
    """
    Function that exists to reset the relevant global dictionaries so that
    a player starts with the correct data when they
    lose a game and decide to restart
    """
    global player_ships
    global player_total_destroyed
    global player_total_damaged
    global enemy_losses
    global enemy_battle_losses
    global enemy_local_losses
    global enemy_bypassed
    global player_experience
    global missile_volleys
    global mine_stocks
    global total_crew
    global excess_crew
    global marines
    global marine_experience
    global player_name
    global flagship_name
    global player_supplies
    global enemy_groups_destroyed
    global enemy_groups_damaged
    global enemy_groups_bypassed

    player_ships = {
        'battleships': player_starting_ships['battleships'],
        'cruisers': player_starting_ships['cruisers'],
        'escorts': player_starting_ships['escorts']
    }
    player_total_damaged = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    player_total_damaged = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    enemy_losses = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
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
    player_experience = 1.0
    missile_volleys = 3
    mine_stocks = 3
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
    marines = (
        (player_ships['battleships'] * 40)
        + (player_ships['cruisers'] * 20)
    )
    marine_experience = 1.0
    player_name = ''
    flagship_name = ''
    player_supplies = 100
    enemy_groups_destroyed = 0
    enemy_groups_damaged = 0
    enemy_groups_bypassed = 0


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
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Do you want to see the capabilities of our ships?')
    while True:
        fleet_capabilities_decision = input(
            'Press y to see info on your ships, or n to move on\n').lower()
        if fleet_capabilities_decision == 'y':
            print('You: Please brief me')
            ship_capabilities()
            break
        elif fleet_capabilities_decision == 'n':
            print('A good naval officer should know their ships by heart')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Admiral, could you tell me what tactics we can use?')
    while True:
        explain_tactics = input(
            'Press y to see your tactics you can employ, or n to move on:\n')
        if explain_tactics == 'y':
            print('You: Of course, Captain')
            tactics()
            break
        elif explain_tactics == 'n':
            print('You: You will just have to watch and learn Roth.')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Now that is done, I will brief you, Admiral')
    print('Roth: The Syndicate Worlds have gathered several assault groups')
    print('Roth: They have attacked at multiple points along the frontier')
    print('Roth: Our fleet has been assembled to stop the enemy')
    print('Roth: We are to plug the holes in our lines')
    print('Roth: Other Alliance forces are assembling behind us')
    print('Roth: They will be able to stop any enemy ships that slip past us')
    print('Roth: High Command wants does not want our forces bogged down')
    print("Roth: They don't want allied forces chasing down small groups")
    print('Roth: They are already planning a counter-attack')
    print('Roth: They want as many ships for that as they can get')
    print('Roth: We should try to avoid leaving enemy groups behind us')
    print('Roth: Follow-on forces might like some target practice though')
    print('Roth: I have reports that allied forces are resisting elsewhere')
    print('Roth: if we help them out, they could reinofrce us.\n')
    print("You: Thank you Captain - let's go save the Alliance!")
    mission_one()


def mission_one():
    """
    Mission 1
    light combat with no real consequences
    intended as an introduction to the game
    """
    print('\n  BEGIN MISSION ONE  \n')
    global player_experience
    global enemy_groups_bypassed
    enemy_group_one = {
        'battleships': 4,
        'cruisers': 8,
        'escorts': 20
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_one)
    player_firepower = calculate_player_firepower(player_ships)
    print('This is the first mission.')
    print('You can expect light combat with no real consequences.')
    print('Experiment and get a feel for the game and how it works\n')
    print(f'Roth: Admiral {player_name}, sensors have detected something!')
    print('Roth: Enemy warships have arrived at the jump point from Salamis!')
    print('Roth: The tactical suite is updating now - this group looks small')
    for key, value in enemy_group_one.items():
        print(f'Roth: The enemy have {value} {key}')
    print(f'Roth: The enemy ships have a total of {enemy_firepower} turrets')
    print('Roth: Based on that, I assess this is a scouting unit')

    firepower_diff = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_diff < 0:
        print(f'Roth: We have {abs(firepower_diff)} fewer turrets')
    elif firepower_diff == 0:
        print('Roth: We are evenly matched in terms of turrets')
    else:
        print(f'Roth: We have {firepower_diff} more turrets')

    print('Roth: Admiral, we should be able to take these guys easily!')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_one = input(
            'Press y to engage the enemy, or n to move on:\n').lower()
        if engage_decision_mission_one == 'y':
            print('You: We engage! All hands - battle stations!')
            fight_battle(enemy_firepower, enemy_group_one)
            player_experience += 0.1
            print('Roth: Congratulations Admiral')
            print('Roth: Our gunners are already notching their barrels')
            break
        elif engage_decision_mission_one == 'n':
            print('You: This is not worth our time')
            print('Roth: Disengage and leave them for follow-on forces')
            print('Roth: Discretion is the better part of valour, Admiral')
            update_enemy_bypassed(enemy_group_one)
            enemy_groups_bypassed += 1
            break
        else:
            print('Please enter y or n')

    print('Roth: Admiral, that enemy group came from Salamis')
    print('Roth: Salamis is a neighbouring system')
    print('Roth: They were likely detached from a larger group')
    print('You: I concur - we can expect heavy resistance at Salamis')
    print('You: All hands, secure from battle stations and prepare for FTL')
    print('You: Roth, lay course for Salamis')
    mission_two()


def mission_two():
    """
    Mission 2
    Heavier combat, requires the player to use their
    experience from Mission One to win
    """
    global player_experience
    global enemy_groups_bypassed
    print('\n  BEGIN MISSION TWO  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Arriving at Salamis in 3....2...1')
    print('Roth: Looks like the enemy is here in strength, Admiral')
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

    firepower_diff = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_diff < 0:
        print(f'Roth: We have {abs(firepower_diff)} fewer turrets')
    elif firepower_diff == 0:
        print('Roth: We are evenly matched in terms of turrets')
    else:
        print(f'Roth: We have {firepower_diff} more turrets')

    print('Roth: This will be a tough battle, Admiral')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_two = input(
            'Press y to engage, or n to disengage:\n')
        if engage_decision_mission_two == 'y':
            print('You: We cannot allow a force this numerous to roam free')
            print('You: All hands, battle stations')
            fight_battle(enemy_firepower, enemy_group_two)
            player_experience += 0.1
            break

        elif engage_decision_mission_two == 'n':
            print('You: No - follow-on forces should be able to handle them')
            update_enemy_bypassed(enemy_group_two)
            enemy_groups_bypassed += 1
            break

        else:
            print('Please enter either y or n')
    print('\n')
    print('Roth: This group was likely one of the Syndics main groups')
    print('Roth: Command estimates that there are at least 4 such groups')
    print('You: Good to know. Where does Command think the next group is?')
    print('Roth: Reports suggest the enemy has targeted Osiris')
    print('Roth: Osiris is the next system over')
    print('Roth: Osiris is a major Alliance military headquarters system')
    print('You: Excellent. All hands, secure from battle stations')
    print('You: Helm, set course for Osiris')
    mission_three()


def mission_three():
    """
    Mission 3
    A more complex mission
    The player is presented with two enemy sub-fleets to deal with
    They must choose which to deal with first
    """
    global player_experience
    global player_supplies
    global marines
    global player_ships
    global enemy_groups_bypassed
    global enemy_groups_damaged
    print('\n  BEGIN MISSION THREE  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Arriving at Osiris in 3...2....1')
    print('You: Status report!')
    print('Roth: The enemy appears to be here in strength Admiral')
    print('Roth: The enemy attack is well underway')
    print('Roth: They have split into two sub-groups\n')
    print('Roth: Sub-group 1 appears to be the largest')
    print('Roth: It is engaging the Osiris system defence forces\n')
    print('Roth: Sub-group 2 appears to hold the remaining ships')
    print('Roth: It is supporting a boarding attack against the dockyards\n')

    enemy_group_three_one = {
        'battleships': 10,
        'cruisers': 32,
        'escorts': 90
    }

    enemy_group_three_two = {
        'battleships': 8,
        'cruisers': 26,
        'escorts': 78
    }

    allied_group = {
        'battleships': 4,
        'cruisers': 14,
        'escorts': 38
    }

    enemy_firepower_one = enemy_firepower_calculator(enemy_group_three_one)
    enemy_firepower_two = enemy_firepower_calculator(enemy_group_three_two)
    allied_firepower = enemy_firepower_calculator(allied_group)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_three_one.items():
        print(f'Roth: Sub-group  1 has {value} {key}')
    print(f'Roth: Sub-group 1 has {enemy_firepower_one} turrets')

    firepower_diff_one = firepower_comparator(
        player_firepower, enemy_firepower_one)
    if firepower_diff_one < 0:
        print(f'Roth: We have {abs(firepower_diff_one)} fewer turrets')
    elif firepower_diff_one == 0:
        print('Roth: We are evenly matched in terms of turrets')
    else:
        print(f'Roth: We have {firepower_diff_one} more turrets')

    print('\n')
    for key, value in enemy_group_three_two.items():
        print(f'Roth: Sub-group  2 has {value} {key}')
    print(f'Roth: Sub-group 2 has {enemy_firepower_two} turrets')

    firepower_diff_two = firepower_comparator(
        player_firepower, enemy_firepower_two)
    if firepower_diff_two < 0:
        print(f'Roth: We have {abs(firepower_diff_two)} fewer turrets')
    elif firepower_diff_two == 0:
        print('Roth: We are evenly matched in terms of turrets')
    else:
        print(f'Roth: We have {firepower_diff_two} more turrets')

    print('\n')
    for key, value in allied_group.items():
        print(f'Roth: Osiris force has {value} {key}')
    print(f'Roth: They have {allied_firepower} turrets')

    def osiris_fleet():
        """
        Small function within mission 3
        Called if player chooses to aid the allied ships in Osiris
        If successful, player is granted reinforcements
        """
        global player_experience
        global osiris_fleet_helped
        global player_ships
        print('You: We need more ships, pronto')
        print('You: They will help us secure the rest of the system')
        print('Roth: Understood Admiral, setting course for the Osiris force')
        print('You: Osiris force, report in!')
        print('OF: Thank the Living Stars! Reinforcements!')
        print('You: Hold on Osiris force. We will deal with the Syndics')
        fight_battle(enemy_firepower_one, enemy_group_three_one)
        player_experience += 0.05
        osiris_fleet_helped = 1
        player_ships['battleships'] += allied_group['battleships']
        player_ships['cruisers'] += allied_group['cruisers']
        player_ships['escorts'] += allied_group['escorts']
        print('OF: Thank you for your assistance, Admiral')
        print('OF: Transferring our ships to your command')

    def osiris_docks():
        """
        Small functions within mission 3
        Called if the player chooses to aid the Osiris Dockyards
        If successful, the player is granted additional supplies
        and Marines
        """
        global player_experience
        global osiris_docks_helped
        global marines
        global player_supplies
        global missile_volleys
        global mine_stocks
        print('You: We need the supplies from the orbital dockyards')
        print('You: They could prove invaluable for future battles')
        print('Roth: Understood Admiral, setting course for the dockyards')
        print('You: Osiris Dockyards, report in!')
        print('ODY: Admiral, enemy assault troops have boarded')
        print('ODY: We are fighting them room to room')
        print('ODY: They are pressing hard!')
        print('You: Hold on, we will deal with the Syndic boarding fleet')
        print('You: Then we will help you clear out the boarders')
        fight_battle(enemy_firepower_one, enemy_group_three_two)
        player_experience += 0.05
        print('Roth: Enemy support ships have been dealt with')
        print('You: Move escorts into fire support positions')
        print(f'Roth: We have {marines} Marines')
        if marines < 100:
            print('Roth: We do not have enough Marines to ')
            print('Roth: We cannot launch a counter-boarding operation')
            print('Roth: But our fire support should still turn the tide')
            print('ODY: We are pushing them back with your fire support')
            print('ODY: But it is costing us badly')
            print('ODY: Syndicate boarding parties are surrendering!')
            print('ODY: Transferring surviving Marines to your command, sir!')
            marines += 500
        elif marines <= 800:
            print('Roth: We have enough Marines to assist the dockyards')
            print('Roth: We can launch a limited counter-boarding operation')
            print('Roth: We should drive out the Syndics with some effort')
            print('Roth: Launching assault shuttles now')
            print('ODY: Your reinforcements are appreciated')
            print('ODY: Enemy forces are breaking off to block you')
            print('ODY: We are rolling them up, but they are still costing us')
            print('ODY: Enemy forces have been defeated')
            print('ODY: Transferring surviving Marines to you command')
            marines += 750
        elif marines > 800:
            print('Roth: We have enough Marines to really help the dockyards')
            print('Roth: We can launch a full counter-boarding operation')
            print('Roth: We should have this done in short order')
            print('Roth: Assault shuttles launching now')
            print('ODY: Your counter assault has severely rattled the enemy!')
            print('ODY: We have them pinned!')
            print('ODY: We are rolling them up quickly!')
            print('ODY: Enemy forces defeated with minimal allied casualties')
            print('ODY: Transferring surviving Marines to you command')
            marines += 1000
        osiris_docks_helped = 1
        print('ODY: You are welcome to our stockpiles for your fleet')
        print('ODY: We can provide fuel, ammunition, mines and missiles')
        player_supplies += 15
        missile_volleys += 1
        mine_stocks += 1

    print('Roth: Shall we aid Osiris?')
    while True:
        engage_decision_mission_three = input(
            'press y to engage, or n to disengage:\n').lower()
        if engage_decision_mission_three == 'y':
            print('You: Osiris is an important staging area. It must not fall')
            print('\n')
            print('You: It appears we have several options')
            print('You: We could aid the Osiris group')
            print('You: Or we could stop that boarding operation')
            print('You: I just need to decide which group to engage first')
            while True:
                try:
                    engage_decision_one = int(input(
                        'Type 1 or 2 to select the group to engage first:\n'))
                    if engage_decision_one == 1:
                        osiris_fleet()
                        break

                    elif engage_decision_one == 2:
                        osiris_docks()
                        break
                    else:
                        print('Please enter either 1 or 2')
                except ValueError:
                    print('Please enter either 1 or 2')

            print('Roth: That is one sub-group down')
            print('Roth: Shall we engage the other?')
            if osiris_fleet_helped == 1:
                while True:
                    engage_decision_two = input(
                        'Type y to help the docks or n to break off:\n')
                    if engage_decision_two == 'y':
                        print('You: We need to help the dockyards garrison')
                        osiris_docks()
                        break
                    elif engage_decision_two == 'n':
                        print('You: We have gained some allied ships')
                        print("You: I can't spare the ships to help the docks")
                        print('You: Disengage')
                        update_enemy_bypassed(enemy_group_three_two)
                        break
                    else:
                        print('Please enter either y or n')

            elif osiris_docks_helped == 1:
                while True:
                    engage_decision_two = input(
                        'Type y to help the allied ships or n to break off:\n')
                    if engage_decision_two == 'y':
                        osiris_fleet()
                        break
                    elif engage_decision_two == 'n':
                        print('You: We have picked up some additonal Marines')
                        print('You: And also some supplies and munitions')
                        print("You: I can't risk my forces further")
                        print('You: Disengage')
                        update_enemy_bypassed(enemy_group_three_one)
                        break
                    else:
                        print('Please enter either y or n')

            if osiris_fleet_helped == 1 and osiris_docks_helped == 1:
                print('Roth: Nicely done Admiral!')
                print('Roth: Osiris is secure')
                print('Roth: In appreciation, Osiris has reinforced us')
                print('Roth: More ships, supplies and Marines')
                player_ships['battleships'] += 1
                player_ships['cruisers'] += 2
                player_ships['escorts'] += 8
                player_supplies += 5
                marines += 100

            break

        elif engage_decision_mission_three == 'n':
            print('You: Osiris is beyond help')
            print('You: Better to disengage')
            print("You: I won't spend ships and sailors on a doomed system")
            print('Roth: Very well, preparing for FTL')
            update_enemy_bypassed(enemy_group_three_one)
            update_enemy_bypassed(enemy_group_three_two)
            enemy_groups_bypassed += 2
            break

        else:
            print('Please enter either y or n')

    mission_four()


def mission_four():
    """
    Mission 4
    Strong enemy resistance
    After combat, player is offered a choice of trading some
    sailors for suuplies
    """
    global player_experience
    global player_supplies
    global excess_crew
    global enemy_groups_bypassed

    print('Roth: Admiral, we have intercepted some enemy communications')
    print('Roth: They indicate that a large enemy group is present at Cyrene')
    print('You: Where is that?')
    print('Roth: The next system over, sir')
    print('\n  BEGIN MISSION FOUR \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Admiral, it appears our intelligence was correct')
    print('Roth: The enemy is here in considerable strength')
    enemy_group_four = {
        'battleships': 26,
        'cruisers': 64,
        'escorts': 186
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_four)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_four.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')

    print('Roth: This will be a difficult battle, Admiral')
    print('Roth: We will have to fight smart to win this one')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_four = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_mission_four == 'y':
            print('You: We cannot allow a force of this strength to survive')
            print('You: All hands, battle stations')
            fight_battle(enemy_firepower, enemy_group_four)
            player_experience += 0.1
            break
        elif engage_decision_mission_four == 'n':
            print('You: We are strong')
            print("You: But we'll suffer significant casualties if we fight")
            print('You: We must break off')
            print('You: Roth, signal follow-on forces to concentrate here')
            update_enemy_bypassed(enemy_group_four)
            enemy_groups_bypassed += 1
            break
        else:
            print('Please enter either y or n')
    print('\n')
    print('Roth: Admiral, a small group of allied ships has arrived')
    print('Roth: They have two messages from High Command')
    print('Roth: The first is a request that we detach 1000 veteran sailors')
    print('Roth: Their experience will be used to help train up new crews')
    print('Roth: In return, they will resupply us')
    if player_experience <= 1.05:
        print('You: Please inform them that we have no veterans to give them')
        print('Roth: Very well sir')
    elif player_experience >= 1.10:
        print('You: We have gained some combat experience')
        while True:
            crew_trade = input(
                'Press y to trade sailors for supplies, or n to refuse:\n')
            if crew_trade == 'y':
                print('You: A capital idea. We could use the supplies')
                excess_crew -= 1000
                player_supplies += 5
                break
            elif crew_trade == 'n':
                print('You: I need those sailors for salvaging enemy ships')
                print('You: Please communicate my apologies')
                break
            else:
                print('Please enter either y or n')
    print('\n')
    print('Roth: The second message contained new orders')
    print('Roth: High Command is  directing us to Medusa Star System')
    print('Roth: An allied convoy is there fleeing a strong enemy force')
    print('You: Very well, lets go help out our fellows')
    mission_five()


def mission_five():
    """
    Mission 5
    Player must save an allied convoy
    Heavy enemy resistance
    But this may be reduced if the player has sufficient mines
    """
    global player_experience
    global mine_stocks
    global player_ships
    global player_supplies
    global marines
    global enemy_groups_bypassed

    print('\n  BEGIN MISSION FIVE  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: High command was right')
    print('Roth: Allied ships spotted')
    print('Roth: No sign of the enemy though')
    print('You: Open a channel to the ')
    print('Roth: Just a moment sir')
    print('You: Alliance Convoy - status report!')
    print('AC: Thank the Living Stars - our message got through')
    print('AC: Admiral, we were in the next system over - Laconia')
    print('AC: The Syndics attacked in force')
    print('AC: They devastated the system')
    print('AC: We think we are all that is left')
    print('AC: We fled, but the enemy are no more than a few hours behind us')
    print('AC: Please sir, you must cover us')
    print('You: Transmit your records')
    print('You: I need to see what we could be up against')
    print('AC: Transmitting now')
    print('AC: This is the force that attacked Laconia')
    print('AC: We fled before we could see how many ships they sent after us')
    print('AC: It could be most of them, or only some')
    enemy_group_five_supposed = {
        'battleships': 32,
        'cruisers': 80,
        'escorts': 200
    }
    enemy_group_five_actual = {
        'battleships': 26,
        'cruisers': 68,
        'escorts': 170
    }
    allied_convoy = {
        'battleships': 3,
        'cruisers': 10,
        'escorts': 26
    }

    enemy_firepower_supposed = enemy_firepower_calculator(
        enemy_group_five_supposed)
    enemy_firepower_actual = enemy_firepower_calculator(
        enemy_group_five_actual)
    player_firepower = calculate_player_firepower(player_ships)
    allied_firepower = enemy_firepower_calculator(allied_convoy)

    for key, value in allied_convoy.items():
        print(f'Roth: The allied convoy has {value} {key}')
    print(f'Based on their numbers, thy have {allied_firepower} turrets')

    for key, value in enemy_group_five_supposed.items():
        print(f'Roth: The enemy force has {value} {key}')
    print(f'The enemy probably have {enemy_firepower_supposed} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower_supposed)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')

    print('Roth: This could be a very difficult fight')
    print('AC: Permission to join up with your fleet Admiral?')
    print('AC: Our ships are damaged, and running low on fuel and ammo though')
    print('AC: Our Marine complements are also depleted')
    while True:
        join_up_decision = input(
            'Press y to have allied convoy join up, or n to refuse them:\n')
        if join_up_decision == 'y':
            print('You: More ships are always welcome, even damaged ones')
            print('You: Repair crews are on their way')
            player_supplies -= 10
            marines += 200
            break
        elif join_up_decision == 'n':
            print("You: I can't spare the supplies to repair your ships")
            print('You: Keep retreating. We will cover you')
            break
        else:
            print('Please enter either y or n')

    print('Roth: Your orders, Admiral?')
    while True:
        engage_decision_mission_five = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_mission_five == 'y':
            print('You: We must cover our retreating forces')
            print('You: But we do not have to face the enemy head on')
            print('Roth: Admiral?')
            print('You: Roth, what are our stocks of mines like?')
            if mine_stocks >= 1:
                print(f'Roth: We have enough for {mine_stocks} fields')
                print('You: Excellent. Lay a minefield at the jump point exit')
                print('You: They will straight into our mines')
                print('You: Then we will spring an ambush')
                print('Roth: A cunning plan Admiral. Laying mines now')
                if mine_stocks == 1:
                    mine_stocks -= 1
                    print('Roth: We have laid a field of standard density sir')
                    print('Roth: When the enemy arrives, they will suffer')
                    print('Roth: They are here!')
                    print('You: All hands, battle stations!')
                    print('Roth: As we feared, most of the enemy are here')
                    print('Roth: The enemy have suffered from our mines')
                    print('Roth: Several enemy ships down')
                    enemy_group_five_actual_one = {
                        'battleships': 20,
                        'cruisers': 54,
                        'escorts': 136
                    }
                    enemy_firepower_one = enemy_firepower_calculator(
                        enemy_group_five_actual_one)
                    for key, value in enemy_group_five_actual_one.items():
                        print(f'Roth: The enemy force has {value} {key}')
                    print(f'The enemy have {enemy_firepower_one} turrets')
                    print('You: All hands, battle stations')
                    fight_battle(
                        enemy_firepower_one, enemy_group_five_actual_one)
                    player_experience += 0.1

                elif mine_stocks >= 2:
                    mine_stocks -= 2
                    print('Roth: We have laid a field of double density')
                    print('Roth: The enemy will be in for a nasty surprise')
                    print('Roth: They are here!')
                    print('Roth: The enemy ploughed straight into our mines')
                    print('Roth: Many enemy ships destroyed')
                    enemy_group_five_actual_two = {
                        'battleships': 15,
                        'cruisers': 40,
                        'escorts': 100
                    }
                    enemy_firepower_two = enemy_firepower_calculator(
                        enemy_group_five_actual_two)
                    for key, value in enemy_group_five_actual_two.items():
                        print(f'Roth: The enemy force has {value} {key}')
                    print(f'The enemy have {enemy_firepower_two} turrets')
                    print('You: All hands, battle stations')
                    fight_battle(
                        enemy_firepower_two, enemy_group_five_actual_two)
                    player_experience += 0.1
                print('Roth: Nicely done Admiral')
                print('Roth: Enemy forces destroyed or in retreat')
                print('Roth: Based on the enemy strength here... ')
                print("Roth: ...we shouldn't face many enemies at Laconia")

            elif mine_stocks == 0:
                print('Roth: We have no mines in our inventory Admiral')
                print('You: Looks like we will have to do this the hard way')
                print('Roth: They are here!')
                print('You: All hands, battle stations')
                print("You: Let's dance")
                fight_battle(enemy_firepower_actual, enemy_group_five_actual)
                player_experience += 0.1
                print('Roth: Nicely done Admiral')
                print('Roth: Without mines, that was a tough fight')
                print('Roth: Enemy forces destroyed or in retreat')
                print('Roth: Based on the enemy strength here... ')
                print("Roth: ...we shouldn't face many enemies at Laconia")

            break

        elif engage_decision_mission_five == 'n':
            print('You: The enemy will likely be coming through in strength')
            print('You: If we retake Laconia, however, we can cut them off')
            print('You: All hands, secure from battle stations')
            print('You: Roth, set course for Laconia')
            update_enemy_bypassed(enemy_group_five_actual)
            enemy_groups_bypassed += 1
            break

        else:
            print('Please enter either y or n')
    mission_six()


def mission_six():
    """
    Mission 6
    Light enemy resistance
    Intended as a rest and recovery mission before final mission
    Player should take few losses
    And may be able to pick up some reinforcements
    """
    global player_experience
    global marines
    global player_supplies
    global enemy_groups_bypassed

    print('\n  BEGIN MISSION SIX  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            print('You: Please Roth')
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Arriving at Laconia in 3...2...1')
    print('You: Status report, Roth')
    print('Roth: As predicted, the enemy forces left here are small')
    print('Roth: But the initial force has shattered allied resistance here')
    print('Roth: The enemy chose their target well')
    print('Roth: Laconia was a centre of military production')
    print('Roth: We might be able to salvage some ships and supplies here')
    print('Roth: Sir, sensors report that the splinter force is still here')
    print('Roth: They are supporting an invasion of Laconia')
    print('Roth: Laconian defence forces will be outnumbered and outgunned')
    print("Roth: The enemy are concentrated at Laconia's factories")
    print('Roth: They are trying to cripple our military industry')
    print('You: What do we have on the enemy group here?')
    enemy_group_six = {
        'battleships': 6,
        'cruisers': 12,
        'escorts': 30
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_six)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_six.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')

    print('Roth: This should be an easier fight Admiral')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_six = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_mission_six == 'y':
            print('You: Yes')
            print('You: We will at least remove support for the enemy landing')
            fight_battle(enemy_firepower, enemy_group_six)
            player_experience += 0.1
            print('Roth: Nice work Admiral')
            print('Roth: Enemy ships destroyed or in retreat')
            print('You: Get me Laconia Command')
            print('LC: Laconia Command here')
            print('You: Status report Laconia Command')
            print('LC: The Syndics have invaded us')
            print('Roth: This must be the famously dry Laconic wit')
            print('You: I can see that, Laconia')
            print('You: Shall I support your forces?')
            print('LC: If you want')
            print('You: Grrrrrr')
            print('You: Roth, move some battleships into bombardment orbits')
            print('Roth: Done sir')
            print('Roth: Laconia is an allied world')
            print("Roth: But we can't use a massive orbital bombardment")
            print("Roth: We will want to spare Laconia's factories")
            if marines < 300:
                print('Roth: Unfortunately, we do not have many Marines')
                print('Roth: We cannot launch a counter invasion')
            elif marines >= 300:
                print('Roth: We have enough Marines for a limited landing')
                print('Roth: Shall we launch shuttles?')
                while True:
                    counter_invasion = input(
                        'Press y to land Marines, or n to leave them to it:\n')
                    if counter_invasion == 'y':
                        print('You: We should help the Laconians out')
                        print('You: In spite of their aggravating nature')
                        print('Roth: Marine assault shuttles launching now')
                        print('Roth: Bombardment ships firing now')
                        print('LC: Much obliged Admiral')
                        print('LC: Our forces are counter attacking')
                        print('Roth: Our Marines are rolling up the enemy')
                        print('LC: Your assistance is noted')
                        print('LC: Some supply shuttles are on the way to you')
                        print('LC: On board are some supplies')
                        print('LC: And a company of our best veterans\n')
                        player_supplies += 2
                        marines += 200
                        break
                    elif counter_invasion == 'n':
                        print('You: If these Laconian pricks are so hard...')
                        print("...let's leave them to it")
                        print('You: Bombard the enemy landing sites')
                        print('Roth: Very well sir')
                        print('Roth: The enemy is trapped here at least\n')
                        break
                    else:
                        print('Please enter either y or n')
            print('You: We should see what we can salvage from the system')
            print('You: What do the sensors report, Roth?')
            print('Roth: Laconia had extensive shipyards and warehouses')
            print('Roth: Most of these have been destroyed, their ships too')
            print('Roth: But a handful are only damaged\n')
            print('Roth: We have managed to retrive some supplies as well')
            player_supplies += 5

            damaged_ships = {
                'battleships': 2,
                'cruisers': 9,
                'escorts': 23
            }

            for key, value in damaged_ships.items():
                print(f'Roth: There are {value} damaged {key}')

            print(f'Roth: We also have {player_supplies} repair supplies')
            print('Roth: It will take a lot to get these wrecks ship-shape')
            crew_required = (
                damaged_ships['battleships'] * minimum_ship_crew['battleship']
                + damaged_ships['cruisers'] * minimum_ship_crew['cruiser']
                + damaged_ships['escorts'] * minimum_ship_crew['escort']
            )
            print('Roth: We will need to crew them as well')
            print(f'Roth: We will require {crew_required} sailors to do that')
            print(f'Roth: We currently have {excess_crew} sailors available')
            if crew_required < excess_crew and player_supplies > 20:
                print('Roth: We have enough sailors and supplies')
                print('Roth: Shall we salvage them?')
                while True:
                    salvage_decision = input(
                        'Press y to salvage the ships, or n to move on:\n')
                    if salvage_decision == 'y':
                        print('You: We need all the ships we can get\n')
                        player_ships['battleships'] += (
                            damaged_ships['battleships'])
                        player_ships['cruisers'] += damaged_ships['cruisers']
                        player_ships['escorts'] += damaged_ships['escorts']
                        player_supplies -= 15
                        break
                    elif salvage_decision == 'n':
                        print('You: I cannot spare the sailors and supplies\n')
                        break
                    else:
                        print('Please enter either y or n')
            elif crew_required > excess_crew:
                print('Roth: We cannot spare the sailors Admiral\n')
            elif player_supplies < 20:
                print('Roth: We do not have the supplies for the repairs\n')

            break

        elif engage_decision_mission_six == 'n':
            print('You: Follow-on forces should be able to handle these guys')
            update_enemy_bypassed(enemy_group_six)
            enemy_groups_bypassed += 1
            break

        else:
            print('Please enter either y or n')

    print('Roth: Well, Laconia is mess, but we have done what we could')
    print('You: Indeed. Where next?')
    print('Roth: Command reports that there is one enemy group left')
    print('Roth: It is currently in the Carthage system')
    print('You: Very well, set course for Carthage')
    mission_seven()


def mission_seven():
    """
    Last campaign mission
    Player has no chance to avoid battle
    They must fight it out
    Then ends the game
    Player's achievements are checked against
    victory conditions
    If player has performed poorly, they lose
    if player has performed well, but not spectacularly, they win
    if player has performed brilliantly, they win and are offered the
    chance to play a difficult bonus mission
    """
    global player_experience
    global player_ships
    print('\n  BEGIN MISSION 7  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    print('Roth: Arriving at Carthage in 3...2...1')
    print('Roth: ADMIRAL! They are right on top of us!')
    print('Roth: We cannot disengage!')
    print('Roth: We must fight this one out!')
    print('You: All hands - BATTLE STATIONS!')
    print('You: Status report, Roth')
    print('Roth: Coming in now Admiral')

    enemy_group_seven = {
        'battleships': 27,
        'cruisers': 71,
        'escorts': 163
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_seven)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_seven.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')

    print('Roth: This will be a hard fight, Admiral')
    print('Roth: We must engage')
    fight_battle(enemy_firepower, enemy_group_seven)
    player_experience += 0.1
    print('Roth: Phew...That was a doozy of the fight')
    print('Roth: Nice bit of ship-handling Adniral')
    print('Roth: All of the Syndicate attack groups have been repulsed')
    print('Roth: A messenger ship from High Command has arrived')
    if enemy_groups_bypassed == 7:
        print('Roth: High Command is very displeased with your performance')
        print('Roth: You refused to engage the enemy unless it was necessary')
        print('Roth: They are calling for your head')
        print('Roth: You are to be placed under arrest immediately')
        print('Roth: Follow-on forces took massive casualties')
        print('Roth: They took the brunt of the fighting')
        print('Roth: They were chasing down the groups we bypassed')
        print('You have failed the game by refusing to fight the enemy\n')
        main()

    elif enemy_groups_destroyed == 8:
        print('Roth: The message is overflowing with praise')
        print('Roth: They commend your willingness to engage the enemy')
        print('Roth: You never failed to engage the enemy')
        print('Roth: And you prosecuted them to the utmost')
        print('Roth: Not a single enemy ship got past us')
        print('Roth: Follow-on forces are dismayed at the lack of targets!\n')
        print('Roth: We have inflicted extreme losses on the enemy')
        print('Roth: You remember that there was a counter attack planned?')
        print('Roth: They want us to lead it')
        print('Roth: Do you want in?')
        while True:
            bonus_decision = input(
                'Press y to launch a counter-attack, or n to hold off:\n')
            if bonus_decision == 'y':
                print('You: Hell yes!')
                print('You: We will be able to turn the tables on them!')
                bonus_mission()
                break
            elif bonus_decision == 'n':
                print('You: I appreciate the thought')
                print('You: But I do not think we are strong enough')
                campaign_report()
                break
            else:
                print('Please enter either y or n')

    elif enemy_groups_damaged == 8:
        print('Roth: High Command is praising your aggression')
        print('Roth: But they frown on your lack of staying power')
        print('Roth: All of the enemy groups got past us')
        print('Roth: But we did managed to inflict some losses')
        print('Roth: Follow-on forces appreciate the damage we did though')
        print('Roth: But they took moderate casualties\n')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: None of the enemy groups were decisively stopped')
        print('Roth: Therefore the Alliance is not in a position to launch it')
        print('Roth: Nonetheless, congratulations are in order')
        print('Roth: We managed to stop a major Syndicate attack')
        print('Roth: They will think twice about trying that again')
        campaign_report()

    elif enemy_groups_destroyed >= 5:
        print('Roth: High Command is praising your ability')
        print(f'Roth: {enemy_groups_destroyed} enemy groups were destroyed')
        print('Roth: We have inflicted severe casualties on the enemy')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: They still think it is viable')
        print('Roth: They want us to lead it')
        print('Roth: Do you want to do that?')
        while True:
            bonus_decision = input(
                'Press y to launch a counter-attack, or n to hold off:\n')
            if bonus_decision == 'y':
                print('You: Yes - we will be able to turn the tables on them')
                bonus_mission()
                break
            elif bonus_decision == 'n':
                print('You: I appreciate the thought')
                print('You: But I do not think we are strong enough')
                campaign_report()
                break
            else:
                print('Please enter either y or n')

    elif enemy_groups_destroyed >= 1:
        print('Roth: High Command is appreciative of your service')
        print(f'Roth: {enemy_groups_destroyed} enemy groups were destroyed')
        print('Roth: We have inflicted modest casualties on the enemy')
        print('Roth: Follow-on forces took severe casualties')
        print('Roth: Remember that Command was planning a counter attack?')
        print('Roth: High Command does not feel able to launch it')
        campaign_report()

    elif enemy_groups_damaged >= 2:
        print('Roth: High Command is displeased with your performance')
        print('Roth: They order that you be placed under arrest')
        print(f'Roth: We damaged {enemy_groups_damaged} groups')
        print('Roth: Many enemy ships got past us')
        print('Roth: Follow-on forces took major losses')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: Few of the enemy groups were decisively stopped')
        print('Roth: Therefore the Alliance is not in a position to launch it')
        campaign_report()

    else:
        print('Roth: We met with mixed success')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: High Command does not feel able to launch it')
        campaign_report()


def bonus_mission():
    """
    Bonus mission function
    Not guaranteed to be called
    Very heavy enemy resistance
    Player must all their experience to win
    """
    global player_experience
    global missile_volleys
    global mine_stocks
    print('\n  BEGIN BONUS MISSION   \n')
    print('Roth: We are preparating for our counter attack, Admiral')
    print('Roth: In preparation, Command has reinforced and resupplied us')
    print('Roth: Our damaged ships have been repaired and returned to us')
    missile_volleys += 2
    mine_stocks += 1
    player_ships['battleships'] += player_total_damaged['battleships']
    player_ships['cruisers'] += player_total_damaged['cruisers']
    player_ships['escorts'] += player_total_damaged['escorts']
    print('Roth: Command has also assigned us some of our follow-on forces')
    player_ships['battleships'] += 5
    player_ships['cruisers'] += 12
    player_ships['escorts'] += 29
    print('Roth: Recon indicates that we will need every ship')
    print('Roth: The Syndicate Worlds clearly anticipate a counter attack')
    print('Roth: They have drawn in a lot of their system defence forces')
    print('Roth: This will be a hard fight')
    print('Roth: High Command has also given us our mission')
    print('Roth: We are to raid the Syndicate system of Pella')
    print('Roth: Pella is a military staging area with many ship yards')
    print('Roth: We need to destroy these ship yards')
    print('Roth: We could hamper ability to replace their losses long-term')
    print('\n')
    print('Roth: Do you want to review the new status of the fleet, Admiral?')
    while True:
        fleet_status_decision = input(
            'Press y to see fleet status or n to move on:\n').lower()
        if fleet_status_decision == 'y':
            print('You: Please Roth')
            player_fleet_status()
            break
        elif fleet_status_decision == 'n':
            print('Roth: Very well Admiral')
            break
        else:
            print('Please enter y or n')
    print('\n')
    enemy_group_final = {
        'battleships': 40,
        'cruisers': 95,
        'escorts': 287
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_final)
    player_firepower = calculate_player_firepower(player_ships)
    print('Roth: Whoa....the enemy is here in massive numbers')
    for key, value in enemy_group_final.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')

    print('Roth: This will be one mother of a fight, Admiral')
    print('Roth: We have clearly rattled them')
    print('Roth: But perhaps this is too much for us')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_bonus_mission = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_bonus_mission == 'y':
            print("You: We're here and we're ready. Let's do this")
            fight_battle(enemy_firepower, enemy_group_final)
            player_experience += 0.1
            print('\n')
            print('Roth: Enemy forces destroyed or in retreat')
            print('You: Excellent. Move in and start destroying the shipyards')
            print('Roth: Very good sir')
            print('Roth: Their shipyards are wrecked sir')
            print('You: Excellent, mission accomplished then')
            print("You: Let's head on home for some well deserved leave")
            print('Roth: A capital idea sir')
            campaign_report()
            break
        elif engage_decision_bonus_mission == 'n':
            print('You: How can they have so many ships?!?')
            print('You: I mislike this')
            print("You: We can't take these fellas without insane casualties")
            print('You: Sound the retreat')
            print('Roth: I concur Admiral - retreating now')
            print('Roth: A shame we had to retreat Admiral')
            print('Roth: Better that than fighting when hopelessly outclassed')
            print("You: I'll be content with victory in defence")
            campaign_report()
            break
        else:
            print('Please enter either y or n')


def campaign_report():
    """
    Campaign report function
    Sums up information about the player's campaign
    prints player losses, enemy losses, etc
    """
    print('\n CAMPAIGN REPORT')
    print('Roth: I took the liberty of compiling a report on our campaign')
    print('\n')
    for key, value in player_starting_ships.items():
        print(f'Roth: We started with {value} {key}')
    print('\n')
    for key, value in player_ships.items():
        print(f'Roth: We finished our campaign with {value} {key}')
    print('\n')
    for key, value in player_total_damaged.items():
        print(f'Roth: We lost {value} {key} damaged')
    print('\n')
    for key, value in player_total_destroyed.items():
        print(f'Roth: We lost {value} {key} destroyed')
    print('\n')
    for key, value in enemy_losses.items():
        print(f'Roth: We destroyed {value} enemy {key}')
    print('\n')
    for key, value in enemy_bypassed.items():
        print(f'Roth: We bypassed {value} enemy {key}')
    print('\n')
    print(f'Roth: We started with {starting_supplies}% supply levels')
    print(f'Roth: We end the campaign with {player_supplies}% supplies')
    print('\n')
    if player_experience == 1.1:
        print('Roth: We only fought one battle - our final engagement')
        print('Roth: Hence, our sailors do not have much combat experience')
    elif player_experience > 1.1 and player_experience < 1.4:
        print('Roth: We fought a handful of battles')
        print('Roth: Hence, our sailors have considerable combat experience')
    elif player_experience >= 1.4 and player_experience < 1.7:
        print('Roth: We fought the enemy several times')
        print('Roth: As a result, our sailors have a lot of combat experience')
    elif player_experience >= 1.7:
        print('Roth: We fought the enemy at every opportunity')
        print('Roth: Our sailors are probably some of the best in human space')
    starting_marines = (
        (player_starting_ships['battleships'] * 40)
        + (player_starting_ships['cruisers'] * 20)
    )
    print(f'Roth: We started with {starting_marines} marines')
    print(f'Roth: We ended our campaign with {marines} marines')
    if marine_experience == 1.0:
        print('Roth: Our Marines gain no combat experience in our campaign')
    elif marine_experience > 1.0 and marine_experience < 1.3:
        print('Roth: Our Marines gained some experience in our campaign')
    elif marine_experience >= 1.3 and marine_experience < 1.6:
        print('Roth: Our Marines gained a considerable amount of experience')
    elif marine_experience >= 1.6:
        print('Roth: Our Marines gained a lot of combat experience')
        print('Roth: They are probably some of the best troops in human space')


def update_enemy(
        effective_enemy_strength, enemy_group_strength,
        firepower_factor, player_experience):
    """
    Updates enemy_group_strength dictionary
    Updates global enemy_losses dictionary
    Returns updated enemy_group_strength dictionary to fight_engagement
    """
    global enemy_losses
    global enemy_local_losses
    global enemy_battle_losses
    damage_factor = firepower_factor * player_experience
    if damage_factor > 1:
        damage_factor = 1
    enemy_battleship_losses = (
        math.ceil(effective_enemy_strength['battleships'] * damage_factor))
    enemy_cruiser_losses = (
        math.ceil(effective_enemy_strength['cruisers'] * damage_factor))
    enemy_escort_losses = (
        math.ceil(effective_enemy_strength['escorts'] * damage_factor))

    enemy_group_strength = {
        'battleships': (
            enemy_group_strength['battleships'] - enemy_battleship_losses),
        'cruisers': (
            enemy_group_strength['cruisers'] - enemy_cruiser_losses),
        'escorts': (
            enemy_group_strength['escorts'] - enemy_escort_losses)
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
        'battleships': (
            enemy_battle_losses['battleships'] + enemy_battleship_losses),
        'cruisers': (
            enemy_battle_losses['cruisers'] + enemy_cruiser_losses),
        'escorts': (
            enemy_battle_losses['escorts'] + enemy_escort_losses)
    }

    if enemy_group_strength['battleships'] < 0:
        enemy_group_strength = {
            'battleships': 0,
            'cruisers': enemy_group_strength['cruisers'],
            'escorts': enemy_group_strength['escorts']
        }
    if enemy_group_strength['cruisers'] < 0:
        enemy_group_strength = {
            'battleships': enemy_group_strength['battleships'],
            'cruisers': 0,
            'escorts': enemy_group_strength['escorts']
        }
    if enemy_group_strength['escorts'] < 0:
        enemy_group_strength = {
            'battleships': enemy_group_strength['battleships'],
            'cruisers': enemy_group_strength['cruisers'],
            'escorts': 0
        }

    return enemy_group_strength


def update_player(losses_factor):
    """
    Updates global player_total_destroyed dictionary
    Updates global player_ships dictionary
    Checks if player_ships dictionary contains negative values,
    and corrects to 0 if so
    Returns updated player_ships dictionary
    """
    global player_ships
    global player_total_destroyed  # possibly remove this, unnecessary
    global player_local_losses
    global player_battle_losses
    global player_destroyed_ships
    global player_damaged_ships
    global marines

    player_battleship_losses = (
        math.floor(player_ships['battleships'] * losses_factor))
    player_cruiser_losses = (
        math.floor(player_ships['cruisers'] * losses_factor))
    player_escort_losses = (
        math.ceil(player_ships['escorts'] * losses_factor))

    player_battle_losses = {
        'battleships': (
            player_battle_losses['battleships'] + player_battleship_losses),
        'cruisers': (
            player_battle_losses['cruisers'] + player_cruiser_losses),
        'escorts': (
            player_battle_losses['escorts'] + player_escort_losses)
    }

    player_destroyed_ships = {
        'battleships': math.ceil(player_battle_losses['battleships'] * 0.30),
        'cruisers': math.ceil(player_battle_losses['cruisers'] * 0.40),
        'escorts': math.ceil(player_battle_losses['escorts'] * 0.50)
    }

    player_damaged_ships = {
        'battleships': math.floor(player_battle_losses['battleships'] * 0.70),
        'cruisers': math.floor(player_battle_losses['cruisers'] * 0.60),
        'escorts': math.floor(player_battle_losses['escorts'] * 0.50)
    }

    marines -= (
        int(math.ceil(player_destroyed_ships['battleships'] * 40 * 0.20))
        + int(math.ceil(player_destroyed_ships['cruisers'] * 20 * 0.30))
        + int(math.ceil(player_damaged_ships['battleships'] * 40 * 0.10))
        + int(math.ceil(player_damaged_ships['cruisers'] * 20 * 0.20))
    )

    player_local_losses = {
        'battleships': player_battleship_losses,
        'cruisers': player_cruiser_losses,
        'escorts': player_escort_losses
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
        global player_total_destroyed
        global player_supplies
        global player_total_destroyed
        global player_total_damaged
        global total_crew
        global enemy_groups_damaged
        global enemy_groups_destroyed

        player_firepower = calculate_player_firepower(player_ships)

        for key, value in enemy_group_strength.items():
            print(f'The enemy have {value} {key}')

        print('You: we have several options:')
        for key, value in tactical_library.items():
            print(f'{key} - We can {value}')

        try:
            tactic = int(input(
                'Type a number from 1 to 6 to select your tactic:\n'))
            if tactic > 6:
                print(f'{tactic} is an invalid selection')
                print('Enter a number between 1 and 6 to select your tactic')
                player_supplies += 1
                fight_engagement(enemy_firepower, enemy_group_strength)

            if tactic == 1:
                print('You: We will aim to hit 25% of them in our firing run')
                print('Roth: A sound plan - maximum concentration of force\n')
                target_factor = 0.25
                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)

                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                print(f'Roth: We have {player_firepower} turrets')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: We will be facing {value} {key}')
                print('\n')

                effective_enemy_firepower = (
                    calculate_effective_enemy_firepower(
                        effective_enemy_strength))

                print(f'Roth: They have {effective_enemy_firepower} turrets\n')
                effective_firepower_difference = firepower_comparator(
                    player_firepower, effective_enemy_firepower)
                efd = effective_firepower_difference
                #  efd is used here because of line length issues
                if effective_firepower_difference < 0:
                    print(f'Roth: We will have {abs(efd)} fewer turrets')
                elif effective_firepower_difference > 0:
                    print(f'Roth: We will have {efd} more turrets')
                elif effective_firepower_difference == 0:
                    print('Roth: What a coincidence!')
                    print('Both our fleets have the same nunber of turrets!')
                # More print statements here refering to 'combat power'

                player_combat_power = player_combat_power_calculator(
                    player_firepower)
                effective_enemy_combat_power = (
                    effective_enemy_combat_power_calculator(
                        effective_enemy_firepower))
                diff = player_combat_power - effective_enemy_combat_power

                if diff > 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: We have the advantage in combat power')
                    firepower_factor = (
                        combat_power_difference / player_firepower)
                    losses_factor = (
                        (effective_enemy_firepower / combat_power_difference))
                    losses_factor = losses_factor / 5

                elif diff == 0:
                    combat_power_difference = 1
                    print('Roth: There is no difference in combat power')
                    print('Roth: We are evenly matched')
                    print('Roth: Are you sure this is a good idea?')
                    if player_experience > 1.0:
                        print('Roth: Our experience gives us a advantage')
                        print('Roth: But this will still be bloody')
                    firepower_factor = 0.50
                    losses_factor = 0.50

                elif diff < 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: They have the advantage in combat power')
                    print('Roth: This is a bad idea Admiral')
                    print('Roth: We should consider another approach')
                    firepower_factor = (
                        player_firepower / combat_power_difference) / 5
                    losses_factor = (
                        combat_power_difference / effective_enemy_firepower)

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                projected_player_losses = (round(losses_factor, 2)) * 100
                ped = projected_enemy_destroyed
                ppl = projected_player_losses

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print(f'Roth: We will probably lose {ppl}% of our ships')
                print('Roth: We will consume a about 1% of our fuel and ammo')
                print('\n')

                print('Roth: Shall we proceed?')
                while True:
                    proceed_decision = input(
                        'Press y to make your attack, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: I like the sound of those odds')
                        print('You: All ships, fire at will!')
                        print('Roth: Engaging per your orders Admiral!\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        break

                    elif proceed_decision == 'n':
                        print('You: Hmmm, I mislike those odds')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter either y or n')

            elif tactic == 2:
                print('You: We will hit half of their ships in our firing run')
                target_factor = 0.50
                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)

                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                print(f'Roth: We have {player_firepower} turrets')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: We will be facing {value} {key}')
                print('\n')

                effective_enemy_firepower = (
                    calculate_effective_enemy_firepower(
                        effective_enemy_strength))

                print(f'Roth: They have {effective_enemy_firepower} turrets\n')
                effective_firepower_difference = firepower_comparator(
                    player_firepower, effective_enemy_firepower)
                efd = effective_firepower_difference
                #  efd is used here because of line length issues
                if effective_firepower_difference < 0:
                    print(f'Roth: We will have {abs(efd)} fewer turrets')
                elif effective_firepower_difference > 0:
                    print(f'Roth: We will have {efd} more turrets')
                elif effective_firepower_difference == 0:
                    print('Roth: What a coincidence!')
                    print('Both our fleets have the same nunber of turrets!')
                # More print statements here refering to 'combat power'

                player_combat_power = player_combat_power_calculator(
                    player_firepower)
                effective_enemy_combat_power = (
                    effective_enemy_combat_power_calculator(
                        effective_enemy_firepower))
                diff = player_combat_power - effective_enemy_combat_power

                if diff > 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: We have the advantage in combat power')
                    firepower_factor = (
                        combat_power_difference / player_firepower)
                    losses_factor = (
                        (effective_enemy_firepower / combat_power_difference))
                    losses_factor = losses_factor / 5

                elif diff == 0:
                    combat_power_difference = 1
                    print('Roth: There is no difference in combat power')
                    print('Roth: We are evenly matched')
                    print('Roth: Are you sure this is a good idea?')
                    if player_experience > 1.0:
                        print('Roth: Our experience gives us a advantage')
                        print('Roth: But this will still be bloody')
                    firepower_factor = 0.50
                    losses_factor = 0.50

                elif diff < 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: They have the advantage in combat power')
                    print('Roth: This is a bad idea Admiral')
                    print('Roth: We should consider another approach')
                    firepower_factor = (
                        player_firepower / combat_power_difference) / 5
                    losses_factor = (
                        combat_power_difference / effective_enemy_firepower)

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                projected_player_losses = (round(losses_factor, 2)) * 100
                ped = projected_enemy_destroyed
                ppl = projected_player_losses

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print(f'Roth: We will probably lose {ppl}% of our ships')
                print('Roth: We will consume a about 1% of our fuel and ammo')
                print('\n')

                print('Roth: Shall we proceed?')
                while True:
                    proceed_decision = input(
                        'Press y to make your attack, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: I like the sound of those odds')
                        print('You: All ships, fire at will!')
                        print('Roth: Engaging per your orders Admiral!\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        break

                    elif proceed_decision == 'n':
                        print('You: Hmmm, I mislike those odds')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter either y or n')

            elif tactic == 3:
                print('You: We will aim to hit three-quarters of them')
                target_factor = 0.75
                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)

                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                print(f'Roth: We have {player_firepower} turrets')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: We will be facing {value} {key}')
                print('\n')

                effective_enemy_firepower = (
                    calculate_effective_enemy_firepower(
                        effective_enemy_strength))

                print(f'Roth: They have {effective_enemy_firepower} turrets\n')
                effective_firepower_difference = firepower_comparator(
                    player_firepower, effective_enemy_firepower)
                efd = effective_firepower_difference
                #  efd is used here because of line length issues
                if effective_firepower_difference < 0:
                    print(f'Roth: We will have {abs(efd)} fewer turrets')
                elif effective_firepower_difference > 0:
                    print(f'Roth: We will have {efd} more turrets')
                elif effective_firepower_difference == 0:
                    print('Roth: What a coincidence!')
                    print('Both our fleets have the same nunber of turrets!')
                # More print statements here refering to 'combat power'

                player_combat_power = player_combat_power_calculator(
                    player_firepower)
                effective_enemy_combat_power = (
                    effective_enemy_combat_power_calculator(
                        effective_enemy_firepower))
                diff = player_combat_power - effective_enemy_combat_power

                if diff > 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: We have the advantage in combat power')
                    firepower_factor = (
                        combat_power_difference / player_firepower)
                    losses_factor = (
                        (effective_enemy_firepower / combat_power_difference))
                    losses_factor = losses_factor / 5

                elif diff == 0:
                    combat_power_difference = 1
                    print('Roth: There is no difference in combat power')
                    print('Roth: We are evenly matched')
                    print('Roth: Are you sure this is a good idea?')
                    if player_experience > 1.0:
                        print('Roth: Our experience gives us a advantage')
                        print('Roth: But this will still be bloody')
                    firepower_factor = 0.50
                    losses_factor = 0.50

                elif diff < 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: They have the advantage in combat power')
                    print('Roth: This is a bad idea Admiral')
                    print('Roth: We should consider another approach')
                    firepower_factor = (
                        player_firepower / combat_power_difference) / 5
                    losses_factor = (
                        combat_power_difference / effective_enemy_firepower)

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                projected_player_losses = (round(losses_factor, 2)) * 100
                ped = projected_enemy_destroyed
                ppl = projected_player_losses

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print(f'Roth: We will probably lose {ppl}% of our ships')
                print('Roth: We will consume a about 1% of our fuel and ammo')
                print('\n')

                print('Roth: Shall we proceed?')
                while True:
                    proceed_decision = input(
                        'Press y to make your attack, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: I like the sound of those odds')
                        print('You: All ships, fire at will!')
                        print('Roth: Engaging per your orders Admiral!\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        break

                    elif proceed_decision == 'n':
                        print('You: Hmmm, I mislike those odds')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter either y or n')

            elif tactic == 4:
                print('You: Maximum attack! Target all enemy ships!')
                target_factor = 1

                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)

                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                print(f'Roth: We have {player_firepower} turrets')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: We will be facing {value} {key}')
                print('\n')

                effective_enemy_firepower = (
                    calculate_effective_enemy_firepower(
                        effective_enemy_strength))

                print(f'Roth: They have {effective_enemy_firepower} turrets\n')
                effective_firepower_difference = firepower_comparator(
                    player_firepower, effective_enemy_firepower)
                efd = effective_firepower_difference
                #  efd is used here because of line length issues
                if effective_firepower_difference < 0:
                    print(f'Roth: We will have {abs(efd)} fewer turrets')
                elif effective_firepower_difference > 0:
                    print(f'Roth: We will have {efd} more turrets')
                elif effective_firepower_difference == 0:
                    print('Roth: What a coincidence!')
                    print('Both our fleets have the same nunber of turrets!')
                # More print statements here refering to 'combat power'

                player_combat_power = player_combat_power_calculator(
                    player_firepower)
                effective_enemy_combat_power = (
                    effective_enemy_combat_power_calculator(
                        effective_enemy_firepower))
                diff = player_combat_power - effective_enemy_combat_power

                if diff > 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: We have the advantage in combat power')
                    firepower_factor = (
                        combat_power_difference / player_firepower)
                    losses_factor = (
                        (effective_enemy_firepower / combat_power_difference))
                    losses_factor = losses_factor / 5

                elif diff == 0:
                    combat_power_difference = 1
                    print('Roth: There is no difference in combat power')
                    print('Roth: We are evenly matched')
                    print('Roth: Are you sure this is a good idea?')
                    if player_experience > 1.0:
                        print('Roth: Our experience gives us a advantage')
                        print('Roth: But this will still be bloody')
                    firepower_factor = 0.50
                    losses_factor = 0.50

                elif diff < 0:
                    combat_power_difference = (
                        combat_power_difference_calculator(diff))
                    print('Roth: They have the advantage in combat power')
                    print('Roth: This is a bad idea Admiral')
                    print('Roth: We should consider another approach')
                    firepower_factor = (
                        player_firepower / combat_power_difference) / 5
                    losses_factor = (
                        combat_power_difference / effective_enemy_firepower)

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                projected_player_losses = (round(losses_factor, 2)) * 100
                ped = projected_enemy_destroyed
                ppl = projected_player_losses

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print(f'Roth: We will probably lose {ppl}% of our ships')
                print('Roth: We will consume a about 1% of our fuel and ammo')
                print('\n')

                print('Roth: Shall we proceed?')
                while True:
                    proceed_decision = input(
                        'Press y to make your attack, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: I like the sound of those odds')
                        print('You: All ships, fire at will!')
                        print('Roth: Engaging per your orders Admiral!\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        break

                    elif proceed_decision == 'n':
                        print('You: Hmmm, I mislike those odds')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter either y or n')

            elif tactic == 5:
                global missile_volleys
                print('You: Fire missiles!')
                if missile_volleys >= 2:
                    print(f'Roth: We can fire {missile_volleys} barrages')
                elif missile_volleys == 1:
                    print('Roth: We have enough missiles for 1 barrage')
                elif missile_volleys > 0 and missile_volleys < 1:
                    print('Roth: We have some missiles')
                    print("Roth: But we can't break through enemy defences")
                    fight_engagement(enemy_firepower, enemy_group_strength)
                elif missile_volleys == 0:
                    print('Roth: We currently have no missiles remaining')
                    fight_engagement(enemy_firepower, enemy_group_strength)

                target_factor = 1

                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)
                missiles_fired = (
                    (player_ships['battleships']
                        * missile_launchers['battleships'])
                    + (player_ships['cruisers']
                        * missile_launchers['cruisers'])
                    + (player_ships['escorts']
                        * missile_launchers['escorts'])
                )
                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: Our missiles will target {value} {key}')
                print('\n')

                effective_enemy_firepower = (
                    calculate_effective_enemy_firepower(
                        effective_enemy_strength))
                print('Roth: Our missiles have a long range')
                print('Roth: We will not face any return fire')
                print(f'Roth: We will fire {missiles_fired} missiles')
                print('Roth: We will use up 1 of our missile barrages')

                firepower_factor = (missiles_fired / effective_enemy_firepower)
                if firepower_factor > 1:
                    firepower_factor = 1
                losses_factor = 0

                print(f'The firepower_factor is {firepower_factor}')
                print(f'The losses factor is {losses_factor}')
                """
                Remove the above prints for deployment
                """

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                ped = projected_enemy_destroyed

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print('Roth: We will not lose any of our ships')
                print('Roth: We will consume a about 1% of our fuel and ammo')
                print('\n')

                print('Roth: Shall we fire a missile barrage?')
                while True:
                    proceed_decision = input(
                        'Press y to fire missiles, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: Fire missiles!')
                        print('Roth: Firing missiles!\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        missile_volleys -= 1
                        print(f'Roth: We now have {missile_volleys} barrages')
                        break

                    elif proceed_decision == 'n':
                        print('You: We would be wasting our missiles')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter either y or n')

            elif tactic == 6:
                global mine_stocks
                print('You: We will lay mines and lure the enemy into them')
                if mine_stocks >= 2:
                    print(f'Roth: We have mines for {mine_stocks} fields')
                elif mine_stocks == 1:
                    print('Roth: We have enough mines for 1 minefield')
                elif mine_stocks > 0 and mine_stocks < 1:
                    print('Roth: We have some mines')
                    print('Roth: But not enough to lay a decent field')
                    fight_engagement(enemy_firepower, enemy_group_strength)
                elif mine_stocks == 0:
                    print('Roth: We currently have no mines remaining')
                    fight_engagement(enemy_firepower, enemy_group_strength)

                target_factor = 1
                effective_enemy_strength = calculate_effective_enemy_strength(
                    enemy_group_strength, target_factor)
                mines_laid = (
                    player_ships['battleships'] * mine_layers['battleships']
                    + player_ships['cruisers'] * mine_layers['cruisers']
                )
                for key, value in player_ships.items():
                    print(f'Roth: We have {value} {key}')
                print('\n')
                for key, value in effective_enemy_strength.items():
                    print(f'Roth: Our mines will target {value} {key}')
                print('\n')

                print('Roth: We are luring the enemy into a trap')
                print('Roth: We will not face return fire')
                print('Roth: However, we will need to burn a lot of fuel')
                print(f'Roth: We will lay {mines_laid} mines')

                total_enemy_ships = (
                    effective_enemy_strength['battleships']
                    + effective_enemy_strength['cruisers']
                    + effective_enemy_strength['escorts']
                )
                firepower_factor = (mines_laid / total_enemy_ships) / 2
                if firepower_factor > 1:
                    firepower_factor = 1
                losses_factor = 0

                projected_enemy_destroyed = (round(firepower_factor, 2)) * 100
                ped = projected_enemy_destroyed

                print(f'Roth: We can probably destroy {ped}% of the enemy')
                print('Roth: We will not lose any of our ships')
                print('Roth: We will consume a about 2% of our fuel\n')

                print('Roth: Shall we lay a minefield?')
                while True:
                    proceed_decision = input(
                        'Press y to lay a minefield, or n to break off:\n')
                    if proceed_decision == 'y':
                        print('You: Yes - lay mines')
                        print('Roth: Deploying mines now Admiral\n')
                        enemy_group_strength = update_enemy(
                                effective_enemy_strength, enemy_group_strength,
                                firepower_factor, player_experience)
                        player_ships = update_player(losses_factor)
                        player_supplies -= 1
                        mine_stocks -= 1
                        print(f'Roth: We can now lay {mine_stocks} minefields')
                        break

                    elif proceed_decision == 'n':
                        print('You: We would be wasting our mines')
                        print('You: I will consider a different approach\n')
                        fight_engagement(enemy_firepower, enemy_group_strength)
                        break

                    else:
                        print('Please enter y or n')

        except ValueError:
            print('Enter a number between 1 and 6 to select your tactic')
            player_supplies += 1
            fight_engagement(enemy_firepower, enemy_group_strength)

        player_supplies -= 1
        print(f'Roth: We now have {player_supplies} supplies\n')

        for key, value in enemy_local_losses.items():
            print(f'Roth: We destroyed {value} enemy {key} in that firing run')
        print('\n')

        for key, value in enemy_group_strength.items():
            print(f'Roth: The enemy now has {value} {key} remaining')
        print('\n')

        for key, value in player_local_losses.items():
            print(f'Roth: That run cost us {value} {key}')
        print('\n')

        for key, value in player_ships.items():
            print(f'Roth: We now have {value} {key}')
        print('\n')

        if (player_ships['battleships'] == 0 and
            player_ships['cruisers'] == 0 and
                player_ships['escorts'] == 0):
            print('Roth: Shields failing Admiral!')
            print('Roth: Multiple hull breaches!')
            print('Roth: The reactor is melting down!')
            print('Roth: Oh Sh......')
            print('Your tactical decisions have resulted in defeat')
            print('Would you like to try again?')
            new_game_decision = input('Press y to try again or n to quit:\n')
            if new_game_decision == 'y':
                new_game_reset()
                new_game()
            elif new_game_decision == 'n':
                main()

        elif player_supplies == 0:
            print('Roth: Admiral, our ships are out of fuel and ammunition!')
            print('Roth: Enemy ships closing in!')
            print('Roth: We cannot fight back!')
            print('You: Very well, broadcast surrender')
            print('You have run out of supplies and have lost the game')
            print('Next time, keep an eye on your fuel and ammo')
            print('Would you like to try again?')
            new_game_decision = input('Press y to try again or n to quit:\n')
            if new_game_decision == 'y':
                new_game_reset()
                new_game()
            elif new_game_decision == 'n':
                main()

        elif (enemy_group_strength['battleships'] > 0 or
                enemy_group_strength['cruisers'] > 0 or
                enemy_group_strength['escorts'] > 0):
            print('Roth: The enemy group has still active ships Admiral!')
            print('Roth: Shall we re-engage?')
            while True:
                reengage_decision = input(
                    'Press y to re-engage the enemy, or n to leave them:\n')
                if reengage_decision == 'y':
                    print('You: Indeed we shall! Good hunting!')
                    fight_engagement(enemy_firepower, enemy_group_strength)
                    break
                elif reengage_decision == 'n':
                    print('You: We have done enough damage')
                    print('You: I do not want to risk our ships further')
                    update_enemy_bypassed(enemy_group_strength)
                    enemy_groups_damaged += 1

                    player_total_destroyed = {
                        'battleships': (
                            player_total_destroyed['battleships']
                            + player_destroyed_ships['battleships']),
                        'cruisers': player_total_destroyed['cruisers'] + (
                            player_destroyed_ships['cruisers']),
                        'escorts': player_total_destroyed['escorts'] + (
                            player_destroyed_ships['escorts'])
                    }

                    player_total_damaged = {
                        'battleships': (
                            player_total_damaged['battleships']
                            + player_damaged_ships['battleships']),
                        'cruisers': player_total_damaged['cruisers'] + (
                            player_damaged_ships['cruisers']),
                        'escorts': player_total_damaged['escorts'] + (
                            player_damaged_ships['escorts'])
                    }

                    for key, value in enemy_battle_losses.items():
                        print(f'Roth: We destroyed {value} {key}')
                    print('\n')

                    for key, value in player_battle_losses.items():
                        print(f'Roth: {value} of our {key} were knocked out')
                    print('\n')

                    print('Roth: Of those...\n')

                    total_crew_calculator()
                    excess_crew_calculator()

                    for key, value in player_destroyed_ships.items():
                        print(f'Roth: {value} of our {key} were destroyed')
                    print('Roth: We cannot recover them\n')

                    for key, value in player_damaged_ships.items():
                        print(f'Roth: {value} of our {key} were badly damaged')
                    print('Roth: They cannot keep up with the fleet')
                    print('Roth: We will have to leave them behind')
                    print('Roth: Follow-on forces could repair them')
                    print('Roth: They may return to us in time\n')

                    reset_battle_losses()
                    break

                else:
                    print('Please enter either y or n')

        elif (enemy_group_strength['battleships'] == 0 and
                enemy_group_strength['cruisers'] == 0 and
                enemy_group_strength['escorts'] == 0):
            print('Roth: We have knocked out all enemy ships, Admiral\n')
            enemy_groups_destroyed += 1

            player_total_destroyed = {
                'battleships': player_total_destroyed['battleships'] + (
                    player_destroyed_ships['battleships']),
                'cruisers': player_total_destroyed['cruisers'] + (
                    player_destroyed_ships['cruisers']),
                'escorts': player_total_destroyed['escorts'] + (
                    player_destroyed_ships['escorts'])
            }

            player_total_damaged = {
                'battleships': player_total_damaged['battleships'] + (
                    player_damaged_ships['battleships']),
                'cruisers': player_total_damaged['cruisers'] + (
                    player_damaged_ships['cruisers']),
                'escorts': player_total_damaged['escorts'] + (
                    player_damaged_ships['escorts'])
            }

            for key, value in enemy_battle_losses.items():
                print(f'Roth: We destroyed {value} {key} in that battle')
            print('\n')

            for key, value in player_battle_losses.items():
                print(f'Roth: {value} of our {key} were knocked out')
            print('\n')

            print('Roth: Of those...\n')

            total_crew_calculator()
            excess_crew_calculator()

            for key, value in player_destroyed_ships.items():
                print(f'Roth: {value} of our {key} were destroyed outright')
            print('Roth: We cannot recover them\n')

            for key, value in player_damaged_ships.items():
                print(f'Roth: {value} of our {key} were badly damaged')
            print('Roth: They cannot keep up with the fleet')
            print('Roth: They will have to be left behind')
            print('Roth: But follow-on forces might be able to repair them')
            print('Roth: They may return to us in time\n')

            reset_battle_losses()

            print('Roth: Some of the enemy ships may be salvagable')
            boardable_ships = {
                'battleships': math.floor(
                    starting_enemy_ships['battleships'] * 0.20),
                'cruisers': math.floor(
                    starting_enemy_ships['cruisers'] * 0.15),
                'escorts': math.floor(
                    starting_enemy_ships['escorts'] * 0.10)
            }

            print('Roth: Shall we attempt to board the enemy ships?')
            while True:
                boarding_decision = input(
                    'Press y to board the enemy ships, or n to move on:\n')
                if boarding_decision == 'y':
                    print('You: Yes, hopefully we can bolster our numbers')
                    boarding_operation(boardable_ships)
                    break
                elif boarding_decision == 'n':
                    print("You: These wrecks aren't worth it")
                    print('Roth: Very well, We are clear to move on')
                    break
                else:
                    print('Please enter either y or n')

    fight_engagement(enemy_firepower, enemy_group_strength)


def total_crew_calculator():
    """
    Function that is called in the fight_engagement and player_fleet_status
    functions to calculate the total crew available to the player
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
    player_fleet_status functions to calculate the excess crew
    available to the player for boarding actions
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
        'battleships': math.ceil(
            enemy_group_strength['battleships'] * target_factor),
        'cruisers': math.ceil(
            enemy_group_strength['cruisers'] * target_factor),
        'escorts': math.ceil(
            enemy_group_strength['escorts'] * target_factor)
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
    enemy_firepower = (
        (enemy_strength['battleships'] * battleship_firepower)
        + (enemy_strength['cruisers'] * cruiser_firepower)
        + (enemy_strength['escorts'] * escort_firepower))
    return enemy_firepower


def player_combat_power_calculator(player_firepower):
    """
    Squares player_firepower argument
    produces the player_combat_power variable
    Returns player_combat_power
    """
    player_combat_power = player_firepower**2
    return player_combat_power


def effective_enemy_combat_power_calculator(effective_enemy_firepower):
    """
    Squares effective_enemy_firepower argument
    Produces the enemy_combat_power variable
    Returns effective_enemy_combat_power
    """
    effective_enemy_combat_power = effective_enemy_firepower**2
    return effective_enemy_combat_power


def combat_power_difference_calculator(diff):
    """
    Finds square root of the diff
    Converts diff to positive if necessary so that square root can be performed
    Returns combat_power_difference
    """
    combat_power_difference = math.sqrt(abs(diff))
    return combat_power_difference


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
    Dynamically calculates player firepower
    based on the number of ships they have
    """
    player_firepower = (
        (player_ships['battleships'] * ship_firepower['battleship'])
        + (player_ships['cruisers'] * ship_firepower['cruiser'])
        + (player_ships['escorts'] * ship_firepower['escort'])
    )
    return player_firepower


def boarding_operation(boardable_ships):
    """
    Called when the player wants to board and salvage
    enemy ships after a battle has been won
    """
    global marines
    global player_ships
    global player_supplies
    global total_crew
    global excess_crew
    global marine_experience
    #  global boarded_ships
    global salvaged_ships

    available_crew = excess_crew_calculator()

    boarded_ships = {
        'battleship': 0,
        'cruiser': 0,
        'escort': 0
    }

    if (boardable_ships['battleships'] == 0 and
        boardable_ships['cruisers'] == 0 and
            boardable_ships['escorts'] == 0):
        print('Roth: There are no more ships left to board\n')
    elif marines < 20:
        print('Roth: We do not have enough Marines')
        print('Roth: We cannot board even one escort')
    elif available_crew < 160:
        print('Roth: We do not have enough crew left to crew a captured ship')
    else:
        for key, value in boardable_ships.items():
            print(f'Roth: There are {value} {key} we can board')
        print('\n')
        print(f'Roth: We have {marines} marines')
        print(f'Roth: We have {available_crew} sailors available')
        print(f'Roth: We have {player_supplies} repair supplies')
        print('\n')
        for key, value in boarding_tactics.items():
            print(f'Roth: {key} - {value}')
        print('Roth: What shall our Marines board first?')
        while True:
            ship_to_board = input(
                'Enter a number between 1 and 5 to select your tactic:\n')
            if ship_to_board == '1':
                print('You: We shall board an enemy battleship')
                if boardable_ships['battleships'] == 0:
                    print('Roth: There are no enemy battleships to board')
                    boarding_operation(boardable_ships)
                elif marines < 500:
                    print('Roth: We do not have enough Marines')
                    print('Roth: We cannot board the battleship')
                    print('Roth: We might be able to board an enemy cruiser')
                    boarding_operation(boardable_ships)
                else:
                    print('Roth: Very well, assault shuttles away')
                    boardable_ships['battleships'] -= 1
                    marine_casualties = int(500 - (marine_experience * 250))
                    marines -= marine_casualties
                    player_ships['battleships'] += 1
                    boarded_ships['battleship'] += 1
                    salvaged_ships['battleships'] += 1
                    player_supplies -= 1
                    excess_crew -= minimum_ship_crew['battleship']
                    print(f'Roth: We lost {marine_casualties} Marines')
                    print('Roth: But we took the battleship')
                    boarding_operation(boardable_ships)

                break

            elif ship_to_board == '2':
                print('You: We shall board an enemy cruiser')
                if boardable_ships['cruisers'] == 0:
                    print('Roth: There are no enemy cruisers to board')
                    boarding_operation(boardable_ships)
                elif marines < 120:
                    print('Roth: We do not have enough Marines')
                    print('Roth: We cannot board an enemy cruiser')
                    print('Roth: We might be able to board an enemy escort')
                    boarding_operation(boardable_ships)
                else:
                    print('Roth: Very well, assault shuttles away')
                    boardable_ships['cruisers'] -= 1
                    marine_casualties = int(120 - (marine_experience * 80))
                    marines -= marine_casualties
                    player_ships['cruisers'] += 1
                    boarded_ships['cruiser'] += 1
                    salvaged_ships['cruisers'] += 1
                    player_supplies -= 1
                    excess_crew -= minimum_ship_crew['cruiser']
                    print(f'Roth: We lost {marine_casualties} Marines')
                    print('Roth: But we took the cruiser')
                    boarding_operation(boardable_ships)

                break

            elif ship_to_board == '3':
                print('We shall board an enemy escort')
                if boardable_ships['escorts'] == 0:
                    print('There are no enemy escorts to board')
                    boarding_operation(boardable_ships)
                else:
                    print('Roth: Very well, assault shuttles launching')
                    boardable_ships['escorts'] -= 1
                    marine_casualties = int(20 - (marine_experience * 15))
                    marines -= marine_casualties
                    player_ships['escorts'] += 1
                    boarded_ships['escort'] += 1
                    salvaged_ships['escorts'] += 1
                    player_supplies -= 1
                    excess_crew -= minimum_ship_crew['escort']
                    print(f'Roth: We lost {marine_casualties} Marines')
                    print('Roth: but the escort has been added to our screen')
                    boarding_operation(boardable_ships)

                break

            elif ship_to_board == '4':
                print('You: We have salvaged enough ships. Scuttle the rest')
                print('Roth: Indeed, better to save our Marines')
                break

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
                    print('Roth: We do not have sufficient Marines, sir')
                    print("Roth: We can't take all enemy ships simultaneously")
                    print('Roth: We might be able to board some of them')
                    boarding_operation(boardable_ships)

                elif player_supplies < supplies_required:
                    print('Roth: We cannot repair all of the enemy ships')
                    print('Roth: But we might be able to repair some of them')
                    boarding_operation(boardable_ships)

                elif (boardable_ships['battleships'] > 0 or
                        boardable_ships['cruisers'] > 0 or
                        boardable_ships['escorts'] > 0):
                    print('You: Board all of them')
                    battleships = boardable_ships['battleships']
                    cruisers = boardable_ships['cruisers']
                    escorts = boardable_ships['escorts']

                    player_ships['battleships'] += battleships
                    player_ships['cruisers'] += cruisers
                    player_ships['escorts'] += escorts

                    boarded_ships['battleship'] += battleships
                    boarded_ships['cruiser'] += cruisers
                    boarded_ships['escort'] += escorts

                    salvaged_ships['battleships'] += battleships
                    salvaged_ships['cruisers'] += cruisers
                    salvaged_ships['escorts'] += escorts

                    excess_crew -= (
                        (minimum_ship_crew['battleship']
                            * boardable_ships['battleships'])
                        + (minimum_ship_crew['cruiser']
                            * boardable_ships['cruisers'])
                        + (minimum_ship_crew['escort']
                            * boardable_ships['escorts'])
                    )

                    marine_casualties_bb = int(
                        battleships * (500 - (marine_experience * 250)))
                    marine_casualties_cc = int(
                        cruisers * (120 - (marine_experience * 80)))
                    marine_casualties_dd = int(
                        escorts * (20 - (marine_experience * 15)))

                    marine_casualties = (
                        marine_casualties_bb
                        + marine_casualties_cc
                        + marine_casualties_dd
                    )

                    for key, value in boarded_ships.items():
                        print(f'Roth: We boarded {value} {key}')

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

                break

            else:
                print('Please enter a number between 1 and 5')

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


def reset_battle_losses():
    """
    Sets the values of all keys within player_battle_losses,
    player_destroyed_ships,
    player_damaged_ships
    and enemy_battle_losses to 0
    """
    global player_battle_losses
    global player_destroyed_ships
    global player_damaged_ships
    global enemy_battle_losses

    player_battle_losses = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    player_destroyed_ships = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    player_damaged_ships = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    enemy_battle_losses = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }


def player_fleet_status():
    """
    Function that can be called at the start of each mission
    Displays the current status of the player's fleet
    As well as supplies, mines, missiles, crew and marines
    """
    player_firepower = calculate_player_firepower(player_ships)
    for key, value in player_ships.items():
        print(f'Roth: We currently have {value} {key}')
    print('\n')
    print(f"Roth: We currently have {player_firepower} turrets")
    print(f'Roth: We have enough missiles for {missile_volleys} barrages')
    print(f'Roth: We have enough mines for {mine_stocks} mine-fields')
    print(f'Roth: We currently have {player_supplies} supplies\n')
    for key, value in player_total_destroyed.items():
        print(f'Roth: {value} of our {key} have been destroyed')
    print('\n')
    for key, value in player_total_damaged.items():
        print(f'Roth: {value} of our {key} have been damaged and left behind')
    print('\n')
    for key, value in salvaged_ships.items():
        print(f'Roth: {value} enemy {key} have be boarded and salvaged')
    print('\n')
    print(f'Roth: We currently have {total_crew} sailors in the fleet')
    print(f'Roth: However, we can spare {excess_crew} for other duties\n')
    if player_experience == 1:
        print('Roth: Our crews are trained, but green and inexperienced\n')
    elif player_experience > 1 and player_experience <= 1.3:
        print('Roth: Our crews have gained some battle experience\n')
    elif player_experience > 1.3 and player_experience <= 1.6:
        print('Roth: Our crews are seasoned veterans\n')
    elif player_experience > 1.7:
        print('Roth: Our crews are hardened combat veterans\n')
    print(f'\nRoth: Our ships carry {marines} Marines')
    if marines < 1800:
        print('Roth: We have lost Marines in combat and to ship destruction')
    if marines > 1800:
        print('Roth: We have picked up some additional Marines')
    if marine_experience == 1.0:
        print('Roth: Our Marines are inexperienced in boarding actions\n')
    elif marine_experience > 1.0 and marine_experience <= 1.3:
        print('Roth: Our Marines have gained some combat experience\n')
    elif marine_experience > 1.3 and marine_experience <= 1.6:
        print('Roth: Our Marines are now seasoned veterans\n')
    elif marine_experience > 1.7:
        print('Roth: Our Marines are hardened veterans\n')


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat')
    print('Roth: They are heavily armoured and armed')
    print(f"Battleships have {ship_firepower['battleship']} turrets")
    print('Battleships have 4 missile launchers')
    print('Battleships have 2 mine-tubes')
    print(f"Battleships have {ship_crew['battleship']} sailors")
    print('Battleships also carry 40 Marines\n')
    print('Cruisers are midweight combatants')
    print(f"Cruisers have {ship_firepower['cruiser']} turrets")
    print('Cruisers have 2 missile launchers')
    print('Cruisers have 1 mine-tube')
    print(f"Cruisers have {ship_crew['cruiser']} sailors")
    print('Cruisers carry 20 Marines\n')
    print('Escorts are light screening ships, effective in numbers')
    print(f"Escorts have {ship_firepower['escort']} turrets")
    print('Escorts have 1 missile launcher')
    print('Escorts do not carry mine-tubes')
    print(f"Escorts have {ship_crew['escort']} sailors")
    print('Escorts do not carry Marines\n')


def tactics():
    """
    Function that is called in new_game to inform the player of what tactics
    they can use in an engagement, what the tactic will do
    and what the consequences are
    """
    print('You: Broadly speaking, we can use 6 tactics:')
    for key, value in tactical_library.items():
        print(f'We can {value}')

    print('\n')
    print('You: Attacking 25% of the enemy has several advantages')
    print('You: We will greatly concentrate our firepower')
    print('You: We destroy many enemy ships')
    print('You: We should also face little return fire, so losses will be low')
    print("You: It's a good approach for facing down superior enemy numbers")
    print('You: However, there are disadvantages too')
    print('You: It will take a lot of fuel and ammo to wear down enemy forces')
    print('\n')
    print('You: Attacking 50% of the enemy has advantages too')
    print('You: Our fire will be less concentrated')
    print('You: We will also be exposed to more enemy fire')
    print('You: So we could take heavier losses')
    print('You: But we will require fewer firing runs overall')
    print('You: So we be more efficient in terms of fuel and ammo')
    print('\n')
    print('You: Striking 75% of the enemy has advantages as well')
    print('You: We will spread out out fire even more')
    print('You: And potentially be exposed to more enemy fire')
    print('You: We could suffer more casualties')
    print('You: But we could require far fewer firing runs')
    print('You: So, we should use less fuel and ammo')
    print('You: This is a could approach for weakened enemy groups')
    print('\n')
    print('You: Finally, we could attack all of the enemy')
    print('You: This would be risky, throwing caution to the wind')
    print('You: Our fire will be very spread out')
    print('You: And we could suffer badly')
    print('You: But we will use very little fuel and ammo')
    print('You: This is the perfect tactic for smaller enemy groups')
    print('\n')

    print('You: We could also choose to fire a barrage of missiles')
    print('You: Missiles are long range weapons')
    print('You: So, we will be safe from return fire')
    print('You: However, strong enemy groups could shoot down many missiles')
    print('You: That said, they are a good way of softening up enemy groups')
    print('You: Then we can go in with a conventional firing run')
    print('You: Our missile stocks are limited')
    print('You: So they should be used sparingly')
    print('\n')

    print('You: We could also choose to lay a minefield')
    print('You: We can lay mines and the pull back')
    print('You: The enemy will then run into our mines')
    print('You: So, we will not face any return fire')
    print('You: Mines are potent and cannot be shot down')
    print('You: We do not have many mines')
    print('You: So we should carefully consider using them')

    print('You: Once the battle is done, some enemy ships may be salvageable')
    print('You: We will need to use our Marines to board them')
    print('You: They would make excellent additions to the fleet')
    print('You: However, we could lose many Marines')
    print('You: We would then be without an important capability')
    print('\n')
    print('Roth: Thank you Admiral, that was informative')
    print('You: You are welcome Roth - watch and learn')
    print('Maybe you will command a fleet youself one day')


def main():
    """
    Contains main program functions
    """
    print('Welcome to Fleet Command, a space battle simulator game')
    print('\n')
    print('The Alliance is a confederation of democratic star-systems')
    print('The Syndicate Worlds are an autocratic empire')
    print('These two powers have been at war for 20 years')
    print('The war shows no sign of ending')
    print('Both sides are locked in a stalemate')
    print('Neither can gain an advantage')
    print('But maybe that is about to change')
    print('\n')
    print('You are a promising young naval officer')
    print('You have just been given command of a fleet')
    print('The Syndicate Worlds have gathered a mighty fleet')
    print('They have attacked at multiple points')
    print('You have been charged with defending the Alliance\n')
    print('Do you want to start a new game?')
    while True:
        new_game_decision = input('Press y to start the game, or n to quit:\n')
        if new_game_decision == 'y':
            new_game_reset()
            new_game()
            break
        elif new_game_decision == 'n':
            new_game_reset()
            main()
            break
        else:
            print('Please enter either y or n')


if __name__ == '__main__':
    main()
