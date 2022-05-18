"""
run.py file
All dictionaries, variables and functions
necessary for the game to run are contained within this file
"""
# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import math

PLAYER_STARTING_SHIPS = {
    'battleships': 20,
    'cruisers': 50,
    'escorts': 150
}

PLAYER_SHIPS = {
    'battleships': 20,
    'cruisers': 50,
    'escorts': 150,
}

PLAYER_TOTAL_DESTROYED = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

PLAYER_TOTAL_DAMAGED = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

PLAYER_LOCAL_LOSSES = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

PLAYER_BATTLE_LOSSES = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

PLAYER_DESTROYED_SHIPS = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

PLAYER_DAMAGED_SHIPS = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

ENEMY_LOSSES = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0,
}

ENEMY_LOCAL_LOSSES = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

ENEMY_BATTLE_LOSSES = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

ENEMY_BYPASSED = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

SHIP_FIREPOWER = {
    'battleship': 20,
    'cruiser': 10,
    'escort': 5,
}

SHIP_CREW = {
    'battleship': 2000,
    'cruiser': 1000,
    'escort': 200
}

MINIMUM_SHIP_CREW = {
    'battleship': int(SHIP_CREW['battleship'] * 0.80),
    'cruiser': int(SHIP_CREW['cruiser'] * 0.80),
    'escort': int(SHIP_CREW['escort'] * 0.80)
}

PLAYER_EXPERIENCE = 1.0

RECOVERED_CREW = {
    'battleship': int(SHIP_CREW['battleship'] * 0.60),
    'cruiser': int(SHIP_CREW['cruiser'] * 0.50),
    'escort': int(SHIP_CREW['escort'] * 0.40)
}

TOTAL_CREW = (
    SHIP_CREW['battleship'] * PLAYER_SHIPS['battleships']
    + SHIP_CREW['cruiser'] * PLAYER_SHIPS['cruisers']
    + SHIP_CREW['escort'] * PLAYER_SHIPS['escorts']
)

EXCESS_CREW = (
    TOTAL_CREW - (
        MINIMUM_SHIP_CREW['battleship'] * PLAYER_SHIPS['battleships']
        + MINIMUM_SHIP_CREW['cruiser'] * PLAYER_SHIPS['cruisers']
        + MINIMUM_SHIP_CREW['escort'] * PLAYER_SHIPS['escorts']
    )
)

MISSILE_VOLLEYS = 3

MISSILE_LAUNCHERS = {
    'battleships': 4,
    'cruisers': 2,
    'escorts': 1
}

MINE_STOCKS = 3

MINE_LAYERS = {
    'battleships': 2,
    'cruisers': 1
}

TACTICAL_LIBRARY = {
    '1': 'attack 25% of the enemy',
    '2': 'attack 50% of the enemy',
    '3': 'attack 75% of the enemy',
    '4': 'attack all of the enemy',
    '5': 'launch a missile barrage',
    '6': 'lay a stealth mine-field'
}

BOARDING_TACTICS = {
    '1': 'We can board a battleship',
    '2': 'We can board a cruiser',
    '3': 'We can board an escort',
    '4': 'We can board all of the enemy ships at once',
    '5': 'We can stop boarding enemy ships'
}

MARINES = (
    (PLAYER_SHIPS['battleships'] * 40)
    + (PLAYER_SHIPS['cruisers'] * 20)
)

MARINE_EXPERIENCE = 1.0

MARINE_EXPERIENCE_GAINS = {
    'battleship': 0.05,
    'cruiser': 0.03,
    'escort': 0.01
}

BOARDED_SHIPS = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

SALVAGED_SHIPS = {
    'battleships': 0,
    'cruisers': 0,
    'escorts': 0
}

OSIRIS_GROUP = {
    'battleships': 4,
    'cruisers': 14,
    'escorts': 38
}

OSIRIS_EXTRA = {
    'battleships': 1,
    'cruisers': 2,
    'escorts': 8
}

ALLIED_CONVOY = {
    'battleships': 3,
    'cruisers': 10,
    'escorts': 26
}

LACONIA_SHIPS = {
    'battleships': 2,
    'cruisers': 9,
    'escorts': 23
}

PLAYER_NAME = ''
FLAGSHIP_NAME = ''
STARTING_SUPPLIES = 30
PLAYER_SUPPLIES = 30

OSIRIS_FLEET_HELPED = 0
OSIRIS_DOCKS_HELPED = 0
OSIRIS_MORE_SHIPS = 0
ALLIED_CONVOY_JOINED = 0
LACONIA_SHIPS_HELPED = 0

ENEMY_GROUPS_DESTROYED = 0
ENEMY_GROUPS_DAMAGED = 0
ENEMY_GROUPS_BYPASSED = 0


def new_game_reset():
    """
    Function that exists to reset the relevant global dictionaries so that
    a player starts with the correct data when they
    lose a game and decide to restart
    """
    global PLAYER_SHIPS
    global PLAYER_TOTAL_DESTROYED
    global PLAYER_TOTAL_DAMAGED
    global SALVAGED_SHIPS
    global ENEMY_LOSSES
    global ENEMY_BATTLE_LOSSES
    global ENEMY_LOCAL_LOSSES
    global ENEMY_BYPASSED
    global PLAYER_EXPERIENCE
    global MISSILE_VOLLEYS
    global MINE_STOCKS
    global TOTAL_CREW
    global EXCESS_CREW
    global MARINES
    global MARINE_EXPERIENCE
    global PLAYER_NAME
    global FLAGSHIP_NAME
    global PLAYER_SUPPLIES
    global ENEMY_GROUPS_DESTROYED
    global ENEMY_GROUPS_DAMAGED
    global ENEMY_GROUPS_BYPASSED

    PLAYER_SHIPS = {
        'battleships': PLAYER_STARTING_SHIPS['battleships'],
        'cruisers': PLAYER_STARTING_SHIPS['cruisers'],
        'escorts': PLAYER_STARTING_SHIPS['escorts']
    }
    PLAYER_TOTAL_DESTROYED = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    PLAYER_TOTAL_DAMAGED = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    SALVAGED_SHIPS = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    ENEMY_LOSSES = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    ENEMY_LOCAL_LOSSES = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    ENEMY_BATTLE_LOSSES = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    ENEMY_BYPASSED = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }
    PLAYER_EXPERIENCE = 1.0
    MISSILE_VOLLEYS = 3
    MINE_STOCKS = 3
    TOTAL_CREW = (
        SHIP_CREW['battleship'] * PLAYER_SHIPS['battleships']
        + SHIP_CREW['cruiser'] * PLAYER_SHIPS['cruisers']
        + SHIP_CREW['escort'] * PLAYER_SHIPS['escorts']
    )
    EXCESS_CREW = (
        TOTAL_CREW - (
            MINIMUM_SHIP_CREW['battleship'] * PLAYER_SHIPS['battleships']
            + MINIMUM_SHIP_CREW['cruiser'] * PLAYER_SHIPS['cruisers']
            + MINIMUM_SHIP_CREW['escort'] * PLAYER_SHIPS['escorts']
        )
    )
    MARINES = (
        (PLAYER_SHIPS['battleships'] * 40)
        + (PLAYER_SHIPS['cruisers'] * 20)
    )
    MARINE_EXPERIENCE = 1.0
    PLAYER_NAME = ''
    FLAGSHIP_NAME = ''
    PLAYER_SUPPLIES = 30
    ENEMY_GROUPS_DESTROYED = 0
    ENEMY_GROUPS_DAMAGED = 0
    ENEMY_GROUPS_BYPASSED = 0


def new_game():
    """
    Starts a new game
    """
    global PLAYER_NAME
    global FLAGSHIP_NAME
    print('\n  NEW GAME  \n')
    PLAYER_NAME = input('Please enter your name:\n')
    FLAGSHIP_NAME = input('Please enter the name of your flagship:\n')
    print(f'Roth: Good morning Admiral {PLAYER_NAME}')
    print('Roth: I am Captain Roth, your staff officer')
    print(f'Roth: Welcome aboard the battleship {FLAGSHIP_NAME}, Admiral')
    print(f'Roth: The {FLAGSHIP_NAME} is your command ship')
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
    input('Press enter to continue\n')
    print('Roth: Now that is done, I will brief you, Admiral')
    print('Roth: The Syndicate Worlds have gathered several assault groups')
    print('Roth: They have attacked at multiple points along the frontier')
    print('Roth: Our fleet has been assembled to stop the enemy')
    print('Roth: We are to plug the holes in our lines\n')
    print('Roth: Other Alliance forces are assembling behind us')
    print('Roth: They will be able to stop any enemy ships that slip past us')
    print('Roth: High Command wants does not want our forces bogged down')
    print("Roth: They don't want allied forces chasing down small groups")
    print('Roth: They are already planning a counter-attack')
    print('Roth: They want as many ships for that as they can get')
    print('Roth: We should try to avoid leaving enemy groups behind us')
    print('Roth: Follow-on forces might like some target practice though\n')
    print('Roth: I have reports that allied forces are resisting elsewhere')
    print('Roth: if we help them out, they could reinofrce us.\n')
    print("You: Thank you Captain - let's go save the Alliance!")
    input('Press enter to continue\n')
    mission_one()


def mission_one():
    """
    Mission 1
    light combat with no real consequences
    intended as an introduction to the game
    """
    print('\n  MISSION ONE  \n')
    global PLAYER_EXPERIENCE
    global ENEMY_GROUPS_BYPASSED
    enemy_group_one = {
        'battleships': 4,
        'cruisers': 8,
        'escorts': 20
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_one)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)
    print('This is the first mission')
    print('You can expect light combat with no real consequences')
    print('Experiment and get a feel for the game and how it works\n')
    input('Press enter to continue\n')
    print(f'Roth: Admiral {PLAYER_NAME}, sensors have detected something!')
    print('Roth: Enemy warships have arrived at the jump point from Salamis!')
    print('Roth: The tactical suite is updating now - this group looks small')
    for key, value in enemy_group_one.items():
        print(f'Roth: The enemy have {value} {key}')
    print(f'Roth: The enemy ships have a total of {enemy_firepower} turrets')
    print('Roth: Based on that, I assess this is a scouting unit')
    input('Press enter to continue\n')
    firepower_diff = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_diff < 0:
        print(f'Roth: We have {abs(firepower_diff)} fewer turrets')
    elif firepower_diff == 0:
        print('Roth: We are evenly matched in terms of turrets')
    else:
        print(f'Roth: We have {firepower_diff} more turrets')

    print('Roth: Admiral, we should be able to take this group easily!')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_one = input(
            'Press y to engage the enemy, or n to move on:\n').lower()
        if engage_decision_mission_one == 'y':
            print('You: We engage! All hands - battle stations!')
            fight_battle(enemy_firepower, enemy_group_one)
            PLAYER_EXPERIENCE += 0.03
            print('Roth: Congratulations Admiral')
            print('Roth: Our gunners are already notching their barrels')
            break
        elif engage_decision_mission_one == 'n':
            print('You: This is not worth our time')
            print('Roth: Disengage and leave them for follow-on forces')
            print('Roth: Discretion is the better part of valour, Admiral')
            update_enemy_bypassed(enemy_group_one)
            ENEMY_GROUPS_BYPASSED += 1
            break
        else:
            print('Please enter y or n')
    input('Press enter to continue\n')
    print('Roth: Admiral, that enemy group came from Salamis')
    print('Roth: Salamis is a neighbouring system')
    print('Roth: They were likely detached from a larger group')
    print('You: I concur - we can expect heavy resistance at Salamis')
    print('You: All hands, secure from battle stations and prepare for FTL')
    print('You: Roth, lay course for Salamis')
    input('Press enter to continue\n')
    mission_two()


def mission_two():
    """
    Mission 2
    Heavier combat, requires the player to use their
    experience from Mission One to win
    """
    global PLAYER_EXPERIENCE
    global ENEMY_GROUPS_BYPASSED
    print('\n  MISSION TWO  \n')
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
    input('Press enter to continue\n')
    print('Roth: Arriving at Salamis in 3....2...1')
    print('Roth: Looks like the enemy is here in strength, Admiral')
    enemy_group_two = {
        'battleships': 12,
        'cruisers': 30,
        'escorts': 100
    }
    enemy_firepower = enemy_firepower_calculator(enemy_group_two)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)

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
    input('Press enter to continue\n')
    print('Roth: This will be a tough battle, Admiral')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_two = input(
            'Press y to engage, or n to disengage:\n')
        if engage_decision_mission_two == 'y':
            print('You: We cannot allow a force this numerous to roam free')
            print('You: All hands, battle stations')
            fight_battle(enemy_firepower, enemy_group_two)
            PLAYER_EXPERIENCE += 0.03
            break

        elif engage_decision_mission_two == 'n':
            print('You: No - follow-on forces should be able to handle them')
            update_enemy_bypassed(enemy_group_two)
            ENEMY_GROUPS_BYPASSED += 1
            break

        else:
            print('Please enter either y or n')
    input('Press enter to continue\n')
    print("Roth: This group was likely one of the Syndics' main groups")
    print('Roth: Command estimates that there are at least 4 such groups')
    print('You: Good to know. Where does Command think the next group is?')
    print('Roth: Reports suggest the enemy has targeted Osiris')
    print('Roth: Osiris is the next system over')
    print('Roth: Osiris is a major Alliance military headquarters system')
    print('You: Excellent. All hands, secure from battle stations')
    print('You: Helm, set course for Osiris')
    input('Press enter to continue\n')
    mission_three()


def mission_three():
    """
    Mission 3
    A more complex mission
    The player is presented with two enemy sub-fleets to deal with
    They must choose which to deal with first
    """
    global PLAYER_EXPERIENCE
    global PLAYER_SUPPLIES
    global MARINES
    global PLAYER_SHIPS
    global ENEMY_GROUPS_BYPASSED
    global ENEMY_GROUPS_DAMAGED
    global MINE_STOCKS
    global MISSILE_VOLLEYS
    global OSIRIS_MORE_SHIPS
    print('\n  MISSION THREE  \n')
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
    input('Press enter to continue\n')
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

    enemy_firepower_one = enemy_firepower_calculator(enemy_group_three_one)
    enemy_firepower_two = enemy_firepower_calculator(enemy_group_three_two)
    allied_firepower = enemy_firepower_calculator(OSIRIS_GROUP)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)
    input('Press enter to continue\n')
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
    for key, value in OSIRIS_GROUP.items():
        print(f'Roth: Osiris force has {value} {key}')
    print(f'Roth: They have {allied_firepower} turrets')

    def osiris_fleet():
        """
        Small function within mission 3
        Called if player chooses to aid the allied ships in Osiris
        If successful, player is granted reinforcements
        """
        global PLAYER_EXPERIENCE
        global OSIRIS_FLEET_HELPED
        global PLAYER_SHIPS
        print('You: We need more ships, pronto')
        print('You: They will help us secure the rest of the system')
        print('Roth: Understood Admiral, setting course for the Osiris force')
        input('Press enter to continue\n')
        print('You: Osiris force, report in!')
        print('OF: Thank the Living Stars! Reinforcements!')
        print('You: Hold on Osiris force. We will deal with the Syndics')
        input('Press enter to continue\n')
        fight_battle(enemy_firepower_one, enemy_group_three_one)
        PLAYER_EXPERIENCE += 0.02
        OSIRIS_FLEET_HELPED = 1
        PLAYER_SHIPS['battleships'] += OSIRIS_GROUP['battleships']
        PLAYER_SHIPS['cruisers'] += OSIRIS_GROUP['cruisers']
        PLAYER_SHIPS['escorts'] += OSIRIS_GROUP['escorts']
        print('OF: Thank you for your assistance, Admiral')
        print('OF: Transferring our ships to your command')
        input('Press enter to continue\n')

    def osiris_docks():
        """
        Small functions within mission 3
        Called if the player chooses to aid the Osiris Dockyards
        If successful, the player is granted additional supplies
        and Marines
        """
        global PLAYER_EXPERIENCE
        global OSIRIS_DOCKS_HELPED
        global MARINES
        global PLAYER_SUPPLIES
        global MISSILE_VOLLEYS
        global MINE_STOCKS
        print('You: We need the supplies from the orbital dockyards')
        print('You: They could prove invaluable for future battles')
        print('Roth: Understood Admiral, setting course for the dockyards')
        input('Press enter to continue\n')
        print('You: Osiris Dockyards, report in!')
        print('ODY: Admiral, enemy assault troops have boarded')
        print('ODY: We are fighting them room to room')
        print('ODY: They are pressing hard!')
        print('You: Hold on, we will deal with the Syndic boarding fleet')
        print('You: Then we will help you clear out the boarders')
        input('Press enter to continue\n')
        fight_battle(enemy_firepower_one, enemy_group_three_two)
        PLAYER_EXPERIENCE += 0.02
        print('Roth: Enemy support ships have been dealt with')
        print('You: Move escorts into fire support positions')
        print(f'Roth: We have {MARINES} Marines')
        input('Press enter to continue\n')
        if MARINES < 100:
            print('Roth: We do not have enough Marines')
            print('Roth: We cannot launch a counter-boarding operation')
            print('Roth: But our fire support should still turn the tide')
            input('Press enter to continue\n')
            print('ODY: We are pushing them back with your fire support')
            print('ODY: But it is costing us badly')
            print('ODY: Syndicate boarding parties are surrendering!')
            print('ODY: Transferring surviving Marines to your command, sir!')
            MARINES += 500
            input('Press enter to continue\n')
        elif MARINES <= 800:
            print('Roth: We have enough Marines to assist the dockyards')
            print('Roth: We can launch a limited counter-boarding operation')
            print('Roth: We should drive out the Syndics with some effort')
            input('Press enter to continue\n')
            print('Roth: Launching assault shuttles now')
            print('ODY: Your reinforcements are appreciated')
            print('ODY: Enemy forces are breaking off to block you')
            print('ODY: We are rolling them up, but they are still costing us')
            input('Press enter to continue\n')
            print('ODY: Enemy forces have been defeated')
            print('ODY: Transferring surviving Marines to you command')
            input('Press enter to continue\n')
            MARINES += 750
        elif MARINES > 800:
            print('Roth: We have enough Marines to really help the dockyards')
            print('Roth: We can launch a full counter-boarding operation')
            print('Roth: We should have this done in short order')
            print('Roth: Assault shuttles launching now')
            input('Press enter to continue\n')
            print('ODY: Your counter assault has severely rattled the enemy!')
            print('ODY: We have them pinned!')
            print('ODY: We are rolling them up quickly!')
            input('Press enter to continue\n')
            print('ODY: Enemy forces defeated with minimal allied casualties')
            print('ODY: Transferring surviving Marines to you command')
            MARINES += 1000
        OSIRIS_DOCKS_HELPED = 1
        input('Press enter to continue\n')
        print('ODY: You are welcome to our stockpiles for your fleet')
        print('ODY: We can provide fuel, ammunition, mines and missiles')
        PLAYER_SUPPLIES += 15
        MISSILE_VOLLEYS += 1
        MINE_STOCKS += 1
    input('Press enter to continue\n')
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
                        'Enter 1 or 2 to select the group to engage first:\n'))
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
            input('Press enter to continue\n')
            print('Roth: That is one sub-group down')
            print('Roth: Shall we engage the other?')
            if OSIRIS_FLEET_HELPED == 1:
                while True:
                    engage_decision_two = input(
                        'Enter y to help the docks or n to break off:\n')
                    if engage_decision_two == 'y':
                        print('You: We need to help the dockyards garrison')
                        osiris_docks()
                        break
                    elif engage_decision_two == 'n':
                        print('You: We have gained some allied ships')
                        print("You: I can't spare the ships to help the docks")
                        print('You: Disengage')
                        update_enemy_bypassed(enemy_group_three_two)
                        input('Press enter to continue\n')
                        break
                    else:
                        print('Please enter either y or n')

            elif OSIRIS_DOCKS_HELPED == 1:
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
                        input('Press enter to continue\n')
                        break
                    else:
                        print('Please enter either y or n')

            if OSIRIS_FLEET_HELPED == 1 and OSIRIS_DOCKS_HELPED == 1:
                OSIRIS_MORE_SHIPS = 1
                print('Roth: Nicely done Admiral!')
                print('Roth: Osiris is secure')
                input('Press enter to continue\n')
                print('Roth: In appreciation, Osiris has reinforced us')
                print('Roth: More supplies, mines, missiles and Marines')
                PLAYER_SHIPS['battleships'] += OSIRIS_EXTRA['battleships']
                PLAYER_SHIPS['cruisers'] += OSIRIS_EXTRA['cruisers']
                PLAYER_SHIPS['escorts'] += OSIRIS_EXTRA['escorts']
                PLAYER_SUPPLIES += 5
                MARINES += 100
                MISSILE_VOLLEYS += 1
                MINE_STOCKS += 1
                print('Roth: They have also released some more ships')
                print('Roth: A battleship, 2 cruisers and 8 escorts')

            break

        elif engage_decision_mission_three == 'n':
            print('You: Osiris is beyond help')
            print('You: Better to disengage')
            print("You: I won't spend ships and sailors on a doomed system")
            print('Roth: Very well, preparing for FTL')
            update_enemy_bypassed(enemy_group_three_one)
            update_enemy_bypassed(enemy_group_three_two)
            ENEMY_GROUPS_BYPASSED += 2
            input('Press enter to continue\n')
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
    global PLAYER_EXPERIENCE
    global PLAYER_SUPPLIES
    global EXCESS_CREW
    global ENEMY_GROUPS_BYPASSED

    print('Roth: Admiral, we have intercepted some enemy communications')
    print('Roth: They indicate that a large enemy group is present at Cyrene')
    print('You: Where is that?')
    print('Roth: The next system over, sir')
    input('Press enter to continue\n')
    print('\n  MISSION FOUR \n')
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
    input('Press enter to continue\n')
    print('Roth: Admiral, it appears our intelligence was correct')
    print('Roth: The enemy is here in considerable strength')
    enemy_group_four = {
        'battleships': 26,
        'cruisers': 64,
        'escorts': 186
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_four)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)

    for key, value in enemy_group_four.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')
    input('Press enter to continue\n')
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
            PLAYER_EXPERIENCE += 0.03
            input('Press enter to continue\n')
            break
        elif engage_decision_mission_four == 'n':
            print('You: We are strong')
            print("You: But we'll suffer significant casualties if we fight")
            print('You: We must break off')
            print('You: Roth, signal follow-on forces to concentrate here')
            update_enemy_bypassed(enemy_group_four)
            ENEMY_GROUPS_BYPASSED += 1
            input('Press enter to continue\n')
            break
        else:
            print('Please enter either y or n')
    print('\n')
    print('Roth: Admiral, a small group of allied ships has arrived')
    print('Roth: They have two messages from High Command')
    print('Roth: The first is a request that we detach 1000 veteran sailors')
    print('Roth: Their experience will be used to help train up new crews')
    print('Roth: In return, they will resupply us')
    if PLAYER_EXPERIENCE <= 1.05:
        print('You: Please inform them that we have no veterans to give them')
        print('Roth: Very well sir')
    elif PLAYER_EXPERIENCE >= 1.10:
        print('You: We have gained some combat experience')
        while True:
            crew_trade = input(
                'Press y to trade sailors for supplies, or n to refuse:\n')
            if crew_trade == 'y':
                print('You: A capital idea. We could use the supplies')
                EXCESS_CREW -= 1000
                PLAYER_SUPPLIES += 5
                input('Press enter to continue\n')
                break
            elif crew_trade == 'n':
                print('You: I need those sailors for salvaging enemy ships')
                print('You: Please communicate my apologies')
                input('Press enter to continue\n')
                break
            else:
                print('Please enter either y or n')
    print('\n')
    print('Roth: The second message contained new orders')
    print('Roth: High Command is  directing us to Medusa Star System')
    print('Roth: An allied convoy is there fleeing a strong enemy force')
    print('You: Very well, lets go help out our fellows')
    input('Press enter to continue\n')
    mission_five()


def mission_five():
    """
    Mission 5
    Player must save an allied convoy
    Heavy enemy resistance
    But this may be reduced if the player has sufficient mines
    """
    global PLAYER_EXPERIENCE
    global MINE_STOCKS
    global PLAYER_SHIPS
    global PLAYER_SUPPLIES
    global MARINES
    global ENEMY_GROUPS_BYPASSED
    global ALLIED_CONVOY_JOINED
    print('\n  MISSION FIVE  \n')
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
    input('Press enter to continue\n')
    print('Roth: High command was right')
    print('Roth: Allied ships spotted')
    print('Roth: No sign of the enemy though')
    print('You: Open a channel to the convoy')
    print('Roth: Just a moment sir')
    input('Press enter to continue\n')
    print('You: Alliance Convoy - status report!')
    print('AC: Thank the Living Stars - our message got through')
    print('AC: Admiral, we were in the next system over - Laconia')
    print('AC: The Syndics attacked in force')
    print('AC: They devastated the system')
    print('AC: We think we are all that is left')
    print('AC: We fled, but the enemy are no more than a few hours behind us')
    print('AC: Please sir, you must cover us')
    input('Press enter to continue\n')
    print('You: Transmit your records')
    print('You: I need to see what we could be up against')
    print('AC: Transmitting now')
    print('AC: This is the force that attacked Laconia')
    print('AC: We fled before we could see how many ships they sent after us')
    print('AC: It could be most of them, or only some')
    input('Press enter to continue\n')
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

    enemy_firepower_supposed = enemy_firepower_calculator(
        enemy_group_five_supposed)
    enemy_firepower_actual = enemy_firepower_calculator(
        enemy_group_five_actual)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)
    allied_firepower = enemy_firepower_calculator(ALLIED_CONVOY)

    for key, value in ALLIED_CONVOY.items():
        print(f'Roth: The allied convoy has {value} {key}')
    print(f'Based on their numbers, they have {allied_firepower} turrets')

    for key, value in enemy_group_five_supposed.items():
        print(f'Roth: The enemy force has {value} {key}')
    print(f'The enemy probably have {enemy_firepower_supposed} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower_supposed)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')
    input('Press enter to continue\n')
    print('Roth: This could be a very difficult fight')
    print('AC: Permission to join up with your fleet Admiral?')
    print('AC: Our ships are damaged, and running low on fuel and ammo though')
    print('AC: Our Marine complements are also depleted')
    input('Press enter to continue\n')
    while True:
        join_up_decision = input(
            'Press y to have allied convoy join up, or n to refuse them:\n')
        if join_up_decision == 'y':
            print('You: More ships are always welcome, even damaged ones')
            print('You: Repair crews are on their way')
            PLAYER_SHIPS['battleships'] += ALLIED_CONVOY['battleships']
            PLAYER_SHIPS['cruisers'] += ALLIED_CONVOY['cruisers']
            PLAYER_SHIPS['escorts'] += ALLIED_CONVOY['escorts']
            ALLIED_CONVOY_JOINED = 1
            PLAYER_SUPPLIES -= 10
            MARINES += 200
            break
        elif join_up_decision == 'n':
            print("You: I can't spare the supplies to repair your ships")
            print('You: Keep retreating. We will cover you')
            break
        else:
            print('Please enter either y or n')
    input('Press enter to continue\n')
    print('Roth: Your orders, Admiral?')
    while True:
        engage_decision_mission_five = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_mission_five == 'y':
            print('You: We must cover our retreating forces')
            print('You: But we do not have to face the enemy head on')
            print('Roth: Admiral?')
            print('You: Roth, what are our stocks of mines like?')
            input('Press enter to continue\n')
            if MINE_STOCKS >= 1:
                print(f'Roth: We have enough for {MINE_STOCKS} fields')
                print('You: Excellent. Lay a minefield at the jump point exit')
                print('You: They will straight into our mines')
                print('You: Then we will spring an ambush')
                print('Roth: A cunning plan Admiral. Laying mines now')
                input('Press enter to continue\n')
                if MINE_STOCKS == 1:
                    MINE_STOCKS -= 1
                    print('Roth: We have laid a field of standard density sir')
                    print('Roth: When the enemy arrives, they will suffer')
                    input('Press enter to continue\n')
                    print('Roth: They are here!')
                    print('You: All hands, battle stations!')
                    print('Roth: As we feared, most of the enemy are here')
                    print('Roth: The enemy have suffered from our mines')
                    print('Roth: Several enemy ships down')
                    input('Press enter to continue\n')
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
                    input('Press enter to continue\n')
                    fight_battle(
                        enemy_firepower_one, enemy_group_five_actual_one)
                    PLAYER_EXPERIENCE += 0.03

                elif MINE_STOCKS >= 2:
                    MINE_STOCKS -= 2
                    print('Roth: We have laid a field of double density')
                    print('Roth: The enemy will be in for a nasty surprise')
                    input('Press enter to continue\n')
                    print('Roth: They are here!')
                    print('Roth: The enemy ploughed straight into our mines')
                    print('Roth: Many enemy ships destroyed')
                    input('Press enter to continue\n')
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
                    input('Press enter to continue\n')
                    fight_battle(
                        enemy_firepower_two, enemy_group_five_actual_two)
                    PLAYER_EXPERIENCE += 0.03
                print('Roth: Nicely done Admiral')
                print('Roth: Enemy forces destroyed or in retreat')
                print('Roth: Based on the enemy strength here... ')
                print("Roth: ...we shouldn't face many enemies at Laconia")
                input('Press enter to continue\n')

            elif MINE_STOCKS == 0:
                print('Roth: We have no mines in our inventory Admiral')
                print('You: Looks like we will have to do this the hard way')
                input('Press enter to continue\n')
                print('Roth: They are here!')
                print('You: All hands, battle stations')
                print("You: Let's dance")
                input('Press enter to continue\n')
                fight_battle(enemy_firepower_actual, enemy_group_five_actual)
                PLAYER_EXPERIENCE += 0.03
                input('Press enter to continue\n')
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
            ENEMY_GROUPS_BYPASSED += 1
            input('Press enter to continue\n')
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
    global PLAYER_EXPERIENCE
    global MARINES
    global PLAYER_SUPPLIES
    global ENEMY_GROUPS_BYPASSED
    global LACONIA_SHIPS_HELPED
    print('\n  MISSION SIX  \n')
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
    input('Press enter to continue\n')
    print('Roth: Arriving at Laconia in 3...2...1')
    print('You: Status report, Roth')
    print('Roth: As predicted, the enemy forces left here are small')
    input('Press enter to continue\n')
    print('Roth: But the initial force has shattered allied resistance here')
    print('Roth: The enemy chose their target well')
    print('Roth: Laconia was a centre of military production')
    print('Roth: We might be able to salvage some supplies here')
    input('Press enter to continue\n')
    print('Roth: Sir, we have a message from the Laconian defence forces')
    print('Roth: They report significant damage, and request assistance')
    print('You: Very well, we will aid them once the enemy here is defeated')
    input('Press enter to continue\n')
    print('Roth: Sir, sensors report that the splinter force is still here')
    print('Roth: They are supporting an invasion of Laconia')
    print('Roth: Laconian ground forces will be outnumbered and outgunned')
    print("Roth: The enemy are concentrated at Laconia's factories")
    print('Roth: They are trying to cripple our military industry')
    input('Press enter to continue\n')
    print('You: What do we have on the enemy group here?')
    enemy_group_six = {
        'battleships': 6,
        'cruisers': 12,
        'escorts': 30
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_six)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)

    for key, value in enemy_group_six.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')
    input('Press enter to continue\n')
    print('Roth: This should be an easier fight Admiral')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_mission_six = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_mission_six == 'y':
            print('You: Yes')
            print('You: We will at least remove support for the enemy landing')
            fight_battle(enemy_firepower, enemy_group_six)
            PLAYER_EXPERIENCE += 0.03
            input('Press enter to continue\n')
            print('Roth: Nice work Admiral')
            print('Roth: Enemy ships destroyed or in retreat')
            input('Press enter to continue\n')
            print('You: Get me Laconia Command')
            print('LC: Laconia Command here')
            print('You: Status report Laconia Command')
            print('LC: The Syndics have invaded us')
            print('Roth: This must be the famously dry Laconic wit')
            input('Press enter to continue\n')
            print('You: I can see that, Laconia')
            print('You: Shall I support your forces?')
            print('LC: If you want')
            print('You: Grrrrrr')
            input('Press enter to continue\n')
            print('You: Roth, move some battleships into bombardment orbits')
            print('Roth: Done sir')
            print('Roth: Laconia is an allied world')
            print("Roth: But we can't use a massive orbital bombardment")
            print("Roth: We will want to spare Laconia's factories")
            input('Press enter to continue\n')
            if MARINES < 300:
                print('Roth: Unfortunately, we do not have many Marines')
                print('Roth: We cannot launch a counter invasion')
            elif MARINES >= 300:
                print('Roth: We have enough Marines for a limited landing')
                print('Roth: Shall we launch shuttles?')
                while True:
                    counter_invasion = input(
                        'Press y to land Marines, or n to leave them to it:\n')
                    if counter_invasion == 'y':
                        print('You: We should help the Laconians out')
                        print('You: In spite of their aggravating nature')
                        input('Press enter to continue\n')
                        print('Roth: Marine assault shuttles launching now')
                        print('Roth: Bombardment ships firing now')
                        input('Press enter to continue\n')
                        print('LC: Much obliged Admiral')
                        print('LC: Our forces are counter attacking')
                        print('Roth: Our Marines are rolling up the enemy')
                        input('Press enter to continue\n')
                        print('LC: Your assistance is noted')
                        print('LC: Some supply shuttles are on the way to you')
                        print('LC: On board are some supplies')
                        print('LC: And a company of our best veterans\n')
                        PLAYER_SUPPLIES += 3
                        MARINES += 200
                        input('Press enter to continue\n')
                        break
                    elif counter_invasion == 'n':
                        print('You: If these Laconian pricks are so hard...')
                        print("...let's leave them to it")
                        print('You: Bombard the enemy landing sites')
                        print('Roth: Very well sir')
                        print('Roth: The enemy is trapped here at least\n')
                        input('Press enter to continue\n')
                        break
                    else:
                        print('Please enter either y or n')
            print('You: We should see what we can salvage from the system')
            print('You: What do the sensors report, Roth?')
            print('Roth: Laconia had extensive shipyards and warehouses')
            print('Roth: Most of these have been destroyed, their ships too')
            print('Roth: But a handful are only damaged\n')
            print('Roth: We have managed to retrive some supplies from them')
            input('Press enter to continue\n')
            print('Roth: We are now clear to assist the defence force ships')
            PLAYER_SUPPLIES += 8

            for key, value in LACONIA_SHIPS.items():
                print(f'Roth: There are {value} damaged {key}')

            print(f'Roth: We also have {PLAYER_SUPPLIES} repair supplies')
            print('Roth: It will take a lot to get these wrecks ship-shape')
            input('Press enter to continue\n')
            if PLAYER_SUPPLIES > 20:
                print('Roth: We have enough supplies')
                print('Roth: Shall we repair the ships?')
                while True:
                    salvage_decision = input(
                        'Press y to repair the ships, or n to move on:\n')
                    if salvage_decision == 'y':
                        LACONIA_SHIPS_HELPED = 1
                        print('You: We need all the ships we can get\n')
                        PLAYER_SHIPS['battleships'] += (
                            LACONIA_SHIPS['battleships'])
                        PLAYER_SHIPS['cruisers'] += LACONIA_SHIPS['cruisers']
                        PLAYER_SHIPS['escorts'] += LACONIA_SHIPS['escorts']
                        MARINES += 200
                        PLAYER_SUPPLIES -= 15
                        break
                    elif salvage_decision == 'n':
                        print('You: I cannot spare the supplies\n')
                        input('Press enter to continue\n')
                        break
                    else:
                        print('Please enter either y or n')
            elif PLAYER_SUPPLIES < 20:
                print('Roth: We do not have the supplies for the repairs\n')
                input('Press enter to continue\n')

            break

        elif engage_decision_mission_six == 'n':
            print('You: Follow-on forces should be able to handle these guys')
            update_enemy_bypassed(enemy_group_six)
            ENEMY_GROUPS_BYPASSED += 1
            input('Press enter to continue\n')
            break

        else:
            print('Please enter either y or n')

    print('Roth: Well, Laconia is mess, but we have done what we could')
    print('You: Indeed. Where next?')
    print('Roth: Command reports that there is one enemy group left')
    print('Roth: It is currently in the Carthage system')
    print('You: Very well, set course for Carthage')
    input('Press enter to continue\n')
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
    global PLAYER_EXPERIENCE
    print('\n  MISSION 7  \n')
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
    input('Press enter to continue\n')
    print('Roth: Arriving at Carthage in 3...2...1')
    print('Roth: ADMIRAL! They are right on top of us!')
    print('Roth: We cannot disengage!')
    print('Roth: We must fight this one out!')
    input('Press enter to continue\n')
    print('You: All hands - BATTLE STATIONS!')
    print('You: Status report, Roth')
    print('Roth: Coming in now Admiral')
    input('Press enter to continue\n')
    enemy_group_seven = {
        'battleships': 27,
        'cruisers': 71,
        'escorts': 163
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_seven)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)

    for key, value in enemy_group_seven.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(
        player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets')
    else:
        print(f'Roth: We have {firepower_difference} more turrets')
    input('Press enter to continue\n')
    print('Roth: This will be a hard fight, Admiral')
    print('Roth: We must engage')
    fight_battle(enemy_firepower, enemy_group_seven)
    PLAYER_EXPERIENCE += 0.03
    input('Press enter to continue\n')
    print('Roth: Phew...That was a doozy of the fight')
    print('Roth: Nice bit of ship-handling Adniral')
    input('Press enter to continue\n')
    print('Roth: All of the Syndicate attack groups have been repulsed')
    print('Roth: A messenger ship from High Command has arrived')
    input('Press enter to continue\n')
    if ENEMY_GROUPS_BYPASSED >= 7:
        print('Roth: High Command is very displeased with your performance')
        print('Roth: You refused to engage the enemy unless it was necessary')
        print('Roth: They are calling for your head')
        print('Roth: You are to be placed under arrest immediately')
        print('Roth: Follow-on forces took massive casualties')
        print('Roth: They took the brunt of the fighting')
        print('Roth: They were chasing down the groups we bypassed')
        input('Press enter to continue\n')
        print('You have failed the game by refusing to fight the enemy\n')
        campaign_report()

    elif ENEMY_GROUPS_DESTROYED == 8:
        print('Roth: The message is overflowing with praise')
        print('Roth: They commend your willingness to engage the enemy')
        print('Roth: You never failed to engage the enemy')
        print('Roth: And you prosecuted them to the utmost')
        print('Roth: Not a single enemy ship got past us')
        print('Roth: Follow-on forces are dismayed at the lack of targets!\n')
        print('Roth: We have inflicted extreme losses on the enemy')
        input('Press enter to continue\n')
        print('Roth: You remember that there was a counter attack planned?')
        print('Roth: They want us to lead it')
        print('Roth: Do you want in?')
        while True:
            bonus_decision = input(
                'Press y to launch a counter-attack, or n to hold off:\n')
            if bonus_decision == 'y':
                print('You: Hell yes!')
                print('You: We will be able to turn the tables on them!')
                input('Press enter to continue\n')
                bonus_mission()
                break
            elif bonus_decision == 'n':
                print('You: I appreciate the thought')
                print('You: But I do not think we are strong enough')
                input('Press enter to continue\n')
                campaign_report()
                break
            else:
                print('Please enter either y or n')

    elif ENEMY_GROUPS_DAMAGED == 8:
        print('Roth: High Command is praising your aggression')
        print('Roth: But they frown on your lack of staying power')
        print('Roth: All of the enemy groups got past us')
        print('Roth: But we did managed to inflict some losses')
        print('Roth: Follow-on forces appreciate the damage we did though')
        print('Roth: But they took moderate casualties\n')
        input('Press enter to continue\n')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: None of the enemy groups were decisively stopped')
        print('Roth: Therefore the Alliance is not in a position to launch it')
        input('Press enter to continue\n')
        print('Roth: Nonetheless, congratulations are in order')
        print('Roth: We managed to stop a major Syndicate attack')
        print('Roth: They will think twice about trying that again')
        input('Press enter to continue\n')
        campaign_report()

    elif ENEMY_GROUPS_DESTROYED >= 5:
        print('Roth: High Command is praising your ability')
        print(f'Roth: {ENEMY_GROUPS_DESTROYED} enemy groups were destroyed')
        print('Roth: We have inflicted severe casualties on the enemy')
        input('Press enter to continue\n')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: They still think it is viable')
        print('Roth: They want us to lead it')
        print('Roth: Do you want to do that?')
        while True:
            bonus_decision = input(
                'Press y to launch a counter-attack, or n to hold off:\n')
            if bonus_decision == 'y':
                print('You: Yes - we will be able to turn the tables on them')
                input('Press enter to continue\n')
                bonus_mission()
                break
            elif bonus_decision == 'n':
                print('You: I appreciate the thought')
                print('You: But I do not think we are strong enough')
                input('Press enter to continue\n')
                campaign_report()
                break
            else:
                print('Please enter either y or n')

    elif ENEMY_GROUPS_DESTROYED >= 1:
        print('Roth: High Command is appreciative of your service')
        print(f'Roth: {ENEMY_GROUPS_DESTROYED} enemy groups were destroyed')
        print('Roth: We have inflicted modest casualties on the enemy')
        print('Roth: Follow-on forces took severe casualties')
        input('Press enter to continue\n')
        print('Roth: Remember that Command was planning a counter attack?')
        print('Roth: High Command does not feel able to launch it')
        campaign_report()

    elif ENEMY_GROUPS_DAMAGED >= 2:
        print('Roth: High Command is displeased with your performance')
        print('Roth: They order that you be placed under arrest')
        print(f'Roth: We damaged {ENEMY_GROUPS_DAMAGED} groups')
        print('Roth: Many enemy ships got past us')
        print('Roth: Follow-on forces took major losses')
        input('Press enter to continue\n')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: Few of the enemy groups were decisively stopped')
        print('Roth: Therefore the Alliance is not in a position to launch it')
        input('Press enter to continue\n')
        campaign_report()

    else:
        print('Roth: We met with mixed success')
        print('Roth: Remember that Command was planning a counter-attack?')
        print('Roth: High Command does not feel able to launch it')
        input('Press enter to continue\n')
        campaign_report()


def bonus_mission():
    """
    Bonus mission function
    Not guaranteed to be called
    Very heavy enemy resistance
    Player must all their experience to win
    """
    global PLAYER_EXPERIENCE
    global MISSILE_VOLLEYS
    global MINE_STOCKS
    global PLAYER_SUPPLIES
    print('\n  BONUS MISSION   \n')
    input('Press enter to continue\n')
    print('Roth: We are preparating for our counter attack, Admiral')
    print('Roth: In preparation, Command has reinforced and resupplied us')
    print('Roth: Our damaged ships have been repaired and returned to us')
    MISSILE_VOLLEYS += 2
    MINE_STOCKS += 1
    PLAYER_SUPPLIES += 15
    PLAYER_SHIPS['battleships'] += PLAYER_TOTAL_DAMAGED['battleships']
    PLAYER_SHIPS['cruisers'] += PLAYER_TOTAL_DAMAGED['cruisers']
    PLAYER_SHIPS['escorts'] += PLAYER_TOTAL_DAMAGED['escorts']
    input('Press enter to continue\n')
    print('Roth: Command has also assigned us some of their follow-on forces')
    PLAYER_SHIPS['battleships'] += 5
    PLAYER_SHIPS['cruisers'] += 12
    PLAYER_SHIPS['escorts'] += 29
    print('Roth: Recon indicates that we will need every ship')
    print('Roth: The Syndicate Worlds clearly anticipate a counter attack')
    print('Roth: They have drawn in a lot of their system defence forces')
    print('Roth: This will be a hard fight')
    input('Press enter to continue\n')
    print('Roth: High Command has also given us our mission')
    print('Roth: We are to raid the Syndicate system of Pella')
    print('Roth: Pella is a military staging area with many ship yards')
    print('Roth: We need to destroy these ship yards')
    print('Roth: We could hamper ability to replace their losses long-term')
    input('Press enter to continue\n')
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
    input('Press enter to continue\n')
    enemy_group_final = {
        'battleships': 40,
        'cruisers': 95,
        'escorts': 287
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_final)
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)
    print('Roth: Arriving at Pella in 3...2....1')
    input('Press enter to continue\n')
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
    input('Press enter to continue\n')
    print('Roth: This will be one mother of a fight, Admiral')
    print('Roth: We have clearly rattled them')
    print('Roth: But perhaps this is too much for us')
    input('Press enter to continue\n')
    print('Roth: Shall we engage?')
    while True:
        engage_decision_bonus_mission = input(
            'press y to engage, or n to disengage:\n')
        if engage_decision_bonus_mission == 'y':
            print("You: We're here and we're ready. Let's do this")
            fight_battle(enemy_firepower, enemy_group_final)
            PLAYER_EXPERIENCE += 0.03
            input('Press enter to continue\n')
            print('Roth: Enemy forces destroyed or in retreat')
            print('You: Excellent. Move in and start destroying the shipyards')
            print('Roth: Very good sir')
            input('Press enter to continue\n')
            print('Roth: Their shipyards are wrecked sir')
            print('You: Excellent, mission accomplished then')
            print("You: Let's head on home for some well deserved leave")
            print('Roth: A capital idea sir')
            input('Press enter to continue\n')
            campaign_report()
            break
        elif engage_decision_bonus_mission == 'n':
            print('You: How can they have so many ships?!?')
            print('You: I mislike this')
            print("You: We can't take these fellas without insane casualties")
            print('You: Sound the retreat')
            print('Roth: I concur Admiral - retreating now')
            input('Press enter to continue\n')
            print('Roth: A shame we had to retreat Admiral')
            print('Roth: Better that than fighting when hopelessly outclassed')
            print("You: I'll be content with victory in defence")
            input('Press enter to continue\n')
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
    for key, value in PLAYER_STARTING_SHIPS.items():
        print(f'Roth: We started with {value} {key}')
    print('\n')
    for key, value in PLAYER_SHIPS.items():
        print(f'Roth: We finished our campaign with {value} {key}')
    print('\n')
    input('Press enter to continue\n')
    for key, value in PLAYER_TOTAL_DAMAGED.items():
        print(f'Roth: We lost {value} {key} damaged')
    print('\n')
    for key, value in PLAYER_TOTAL_DESTROYED.items():
        print(f'Roth: We lost {value} {key} destroyed')
    print('\n')
    input('Press enter to continue\n')
    for key, value in ENEMY_LOSSES.items():
        print(f'Roth: We destroyed {value} enemy {key}')
    print('\n')
    for key, value in ENEMY_BYPASSED.items():
        print(f'Roth: We bypassed {value} enemy {key}')
    print('\n')
    input('Press enter to continue\n')
    print(f'Roth: We started with {STARTING_SUPPLIES}% supply levels')
    print(f'Roth: We end the campaign with {PLAYER_SUPPLIES}% supplies')
    print('\n')
    input('Press enter to continue\n')
    if PLAYER_EXPERIENCE == 1.1:
        print('Roth: We only fought one battle - our final engagement')
        print('Roth: Hence, our sailors do not have much combat experience')
    elif PLAYER_EXPERIENCE > 1.1 and PLAYER_EXPERIENCE < 1.4:
        print('Roth: We fought a handful of battles')
        print('Roth: Hence, our sailors have considerable combat experience')
    elif PLAYER_EXPERIENCE >= 1.4 and PLAYER_EXPERIENCE < 1.7:
        print('Roth: We fought the enemy several times')
        print('Roth: As a result, our sailors have a lot of combat experience')
    elif PLAYER_EXPERIENCE >= 1.7:
        print('Roth: We fought the enemy at every opportunity')
        print('Roth: Our sailors are probably some of the best in human space')
    input('Press enter to continue\n')
    starting_marines = (
        (PLAYER_STARTING_SHIPS['battleships'] * 40)
        + (PLAYER_STARTING_SHIPS['cruisers'] * 20)
    )
    print(f'Roth: We started with {starting_marines} Marines')
    print(f'Roth: We ended our campaign with {MARINES} Marines')
    if MARINE_EXPERIENCE == 1.0:
        print('Roth: Our Marines gained no combat experience in our campaign')
    elif MARINE_EXPERIENCE > 1.0 and MARINE_EXPERIENCE < 1.3:
        print('Roth: Our Marines gained some experience in our campaign')
    elif MARINE_EXPERIENCE >= 1.3 and MARINE_EXPERIENCE < 1.6:
        print('Roth: Our Marines gained a considerable amount of experience')
    elif MARINE_EXPERIENCE >= 1.6:
        print('Roth: Our Marines gained a lot of combat experience')
        print('Roth: They are probably some of the best troops in human space')
    print('\n')
    input('Press enter to continue\n')
    print('You have seen what you accomplished')
    print('Can you do better?')
    while True:
        new_game_decision = input('Press y to for a new game or n to quit:\n')
        if new_game_decision == 'y':
            new_game_reset()
            new_game()
            break
        elif new_game_decision == 'n':
            main()
            break
        else:
            print('Please enter either y or n')


def update_enemy(
        effective_enemy_strength, enemy_group_strength,
        firepower_factor, PLAYER_EXPERIENCE):
    """
    Updates enemy_group_strength dictionary
    Updates global ENEMY_LOSSES dictionary
    Returns updated enemy_group_strength dictionary to fight_engagement
    """
    global ENEMY_LOSSES
    global ENEMY_LOCAL_LOSSES
    global ENEMY_BATTLE_LOSSES
    damage_factor = firepower_factor * PLAYER_EXPERIENCE
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

    ENEMY_LOSSES = {
        'battleships': ENEMY_LOSSES['battleships'] + enemy_battleship_losses,
        'cruisers': ENEMY_LOSSES['cruisers'] + enemy_cruiser_losses,
        'escorts': ENEMY_LOSSES['escorts'] + enemy_escort_losses
    }

    ENEMY_LOCAL_LOSSES = {
        'battleships': enemy_battleship_losses,
        'cruisers': enemy_cruiser_losses,
        'escorts': enemy_escort_losses
    }

    ENEMY_BATTLE_LOSSES = {
        'battleships': (
            ENEMY_BATTLE_LOSSES['battleships'] + enemy_battleship_losses),
        'cruisers': (
            ENEMY_BATTLE_LOSSES['cruisers'] + enemy_cruiser_losses),
        'escorts': (
            ENEMY_BATTLE_LOSSES['escorts'] + enemy_escort_losses)
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
    Updates global PLAYER_TOTAL_DESTROYED dictionary
    Updates global PLAYER_SHIPS dictionary
    Checks if PLAYER_SHIPS dictionary contains negative values,
    and corrects to 0 if so
    Returns updated PLAYER_SHIPS dictionary
    """
    global PLAYER_SHIPS
    global PLAYER_TOTAL_DESTROYED  # possibly remove this, unnecessary
    global PLAYER_LOCAL_LOSSES
    global PLAYER_BATTLE_LOSSES
    global PLAYER_DESTROYED_SHIPS
    global PLAYER_DAMAGED_SHIPS
    global MARINES

    player_battleship_losses = (
        round(PLAYER_SHIPS['battleships'] * (losses_factor / 1.5)))
    player_cruiser_losses = (
        round(PLAYER_SHIPS['cruisers'] * (losses_factor)))
    player_escort_losses = (
        round(PLAYER_SHIPS['escorts'] * losses_factor))

    PLAYER_BATTLE_LOSSES = {
        'battleships': (
            PLAYER_BATTLE_LOSSES['battleships'] + player_battleship_losses),
        'cruisers': (
            PLAYER_BATTLE_LOSSES['cruisers'] + player_cruiser_losses),
        'escorts': (
            PLAYER_BATTLE_LOSSES['escorts'] + player_escort_losses)
    }

    PLAYER_DESTROYED_SHIPS = {
        'battleships': math.ceil(PLAYER_BATTLE_LOSSES['battleships'] * 0.30),
        'cruisers': math.ceil(PLAYER_BATTLE_LOSSES['cruisers'] * 0.40),
        'escorts': math.ceil(PLAYER_BATTLE_LOSSES['escorts'] * 0.50)
    }

    PLAYER_DAMAGED_SHIPS = {
        'battleships': math.floor(PLAYER_BATTLE_LOSSES['battleships'] * 0.70),
        'cruisers': math.floor(PLAYER_BATTLE_LOSSES['cruisers'] * 0.60),
        'escorts': math.floor(PLAYER_BATTLE_LOSSES['escorts'] * 0.50)
    }

    MARINES -= (
        int(math.ceil(PLAYER_DESTROYED_SHIPS['battleships'] * 40 * 0.20))
        + int(math.ceil(PLAYER_DESTROYED_SHIPS['cruisers'] * 20 * 0.30))
        + int(math.ceil(PLAYER_DAMAGED_SHIPS['battleships'] * 40 * 0.10))
        + int(math.ceil(PLAYER_DAMAGED_SHIPS['cruisers'] * 20 * 0.20))
    )

    PLAYER_LOCAL_LOSSES = {
        'battleships': player_battleship_losses,
        'cruisers': player_cruiser_losses,
        'escorts': player_escort_losses
    }

    PLAYER_SHIPS = {
        'battleships': PLAYER_SHIPS['battleships'] - player_battleship_losses,
        'cruisers': PLAYER_SHIPS['cruisers'] - player_cruiser_losses,
        'escorts': PLAYER_SHIPS['escorts'] - player_escort_losses
    }

    if PLAYER_SHIPS['battleships'] <= 1:
        PLAYER_SHIPS = {
            'battleships': 0,
            'cruisers': PLAYER_SHIPS['cruisers'],
            'escorts': PLAYER_SHIPS['escorts']
        }
    if PLAYER_SHIPS['cruisers'] <= 1:
        PLAYER_SHIPS = {
            'battleships': PLAYER_SHIPS['battleships'],
            'cruisers': 0,
            'escorts': PLAYER_SHIPS['escorts']
        }
    if PLAYER_SHIPS['escorts'] <= 1:
        PLAYER_SHIPS = {
            'battleships': PLAYER_SHIPS['battleships'],
            'cruisers': PLAYER_SHIPS['cruisers'],
            'escorts': 0
        }
    return PLAYER_SHIPS


def fight_battle(enemy_firepower, enemy_group_strength):
    """
    Function that is called when the player
    decides to fight an enemy in a mission
    """
    print('\n')
    print('Roth: How shall we engage?')
    print('\n')
    starting_enemy_ships = {
        'battleships': enemy_group_strength['battleships'],
        'cruisers': enemy_group_strength['cruisers'],
        'escorts': enemy_group_strength['escorts']
    }

    number_enemy_ships = (
        starting_enemy_ships['battleships']
        + starting_enemy_ships['cruisers']
        + starting_enemy_ships['escorts']
    )

    def fight_engagement(
            enemy_firepower, enemy_group_strength, number_enemy_ships):
        """
        A long, complex function that is called for each firing run
        """
        global ENEMY_LOSSES
        global PLAYER_SHIPS
        global PLAYER_TOTAL_DESTROYED
        global PLAYER_SUPPLIES
        global PLAYER_TOTAL_DESTROYED
        global PLAYER_TOTAL_DAMAGED
        global TOTAL_CREW
        global ENEMY_GROUPS_DAMAGED
        global ENEMY_GROUPS_DESTROYED

        player_firepower = calculate_player_firepower(PLAYER_SHIPS)

        for key, value in enemy_group_strength.items():
            print(f'The enemy have {value} {key}')
        print('\n')
        print('You: We have several options:')
        for key, value in TACTICAL_LIBRARY.items():
            print(f'{key} - We can {value}')
        print('\n')
        while True:
            try:
                tactic = int(input(
                    'Type a number from 1 to 6 to select your tactic:\n'))
                if tactic > 6:
                    print(f'{tactic} is an invalid selection')
                    print('Enter a number between 1 and 6')
                    fight_engagement(
                        enemy_firepower, enemy_group_strength,
                        number_enemy_ships)

                if tactic == 1:
                    print('You: We will aim to hit 25% of them in our attack')
                    print('Roth: A sound plan - maximum concentration\n')
                    target_factor = 0.25
                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))

                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    print(f'Roth: We have {player_firepower} turrets')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: We will be facing {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
                    effective_enemy_firepower = (
                        calculate_effective_enemy_firepower(
                            effective_enemy_strength))
                    eef = effective_enemy_firepower
                    print(f'Roth: They have {eef} turrets\n')
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
                        print('Both our fleets have the same firepower!')

                    player_combat_power = player_combat_power_calculator(
                        player_firepower)
                    effective_enemy_combat_power = (
                        effective_enemy_combat_power_calculator(
                            effective_enemy_firepower))
                    diff = player_combat_power - effective_enemy_combat_power

                    if diff > 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: We have the advantage in combat power')
                        firepower_factor = (
                            cpd / player_firepower)
                        losses_factor = (
                            (effective_enemy_firepower / cpd))
                        losses_factor = losses_factor / 5

                    elif diff == 0:
                        combat_power_difference = 1
                        print('Roth: There is no difference in combat power')
                        print('Roth: We are evenly matched')
                        print('Roth: Are you sure this is a good idea?')
                        if PLAYER_EXPERIENCE > 1.0:
                            print('Roth: Our experience gives us a advantage')
                            print('Roth: But this will still be bloody')
                        firepower_factor = 0.50
                        losses_factor = 0.50

                    elif diff < 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: They have the advantage in combat power')
                        print('Roth: This is a bad idea Admiral')
                        print('Roth: We should consider another approach')
                        firepower_factor = (
                            player_firepower / cpd) / 5
                        losses_factor = (
                            cpd / effective_enemy_firepower)

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    projected_player_losses = (round(losses_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    ppl = projected_player_losses
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print(f'Roth: We will probably lose {ppl}% of our ships')
                    print('\n')

                    print('Roth: Shall we proceed?')
                    while True:
                        proceed_decision = input(
                            'Press y to proceed, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: I like the sound of those odds')
                            print('You: All ships, fire at will!')
                            print('Roth: Engaging per your orders Admiral!\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            print('Roth: Weapons firing!')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: Hmmm, I mislike those odds')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter either y or n')
                    break

                elif tactic == 2:
                    print('You: We will hit half of their ships in our attack')
                    target_factor = 0.50
                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))

                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    print(f'Roth: We have {player_firepower} turrets')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: We will be facing {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
                    effective_enemy_firepower = (
                        calculate_effective_enemy_firepower(
                            effective_enemy_strength))
                    eef = effective_enemy_firepower
                    print(f'Roth: They have {eef} turrets\n')
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
                        print('Both our fleets have the same firepower')

                    player_combat_power = player_combat_power_calculator(
                        player_firepower)
                    effective_enemy_combat_power = (
                        effective_enemy_combat_power_calculator(
                            effective_enemy_firepower))
                    diff = player_combat_power - effective_enemy_combat_power

                    if diff > 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: We have the advantage in combat power')
                        firepower_factor = (
                            cpd / player_firepower)
                        losses_factor = (
                            (effective_enemy_firepower / cpd))
                        losses_factor = losses_factor / 5

                    elif diff == 0:
                        combat_power_difference = 1
                        print('Roth: There is no difference in combat power')
                        print('Roth: We are evenly matched')
                        print('Roth: Are you sure this is a good idea?')
                        if PLAYER_EXPERIENCE > 1.0:
                            print('Roth: Our experience gives us a advantage')
                            print('Roth: But this will still be bloody')
                        firepower_factor = 0.50
                        losses_factor = 0.50

                    elif diff < 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: They have the advantage in combat power')
                        print('Roth: This is a bad idea Admiral')
                        print('Roth: We should consider another approach')
                        firepower_factor = (
                            player_firepower / cpd) / 5
                        losses_factor = (
                            cpd / effective_enemy_firepower)

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    projected_player_losses = (round(losses_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    ppl = projected_player_losses
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print(f'Roth: We will probably lose {ppl}% of our ships')
                    print('\n')

                    print('Roth: Shall we proceed?')
                    while True:
                        proceed_decision = input(
                            'Press y to proceed, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: I like the sound of those odds')
                            print('You: All ships, fire at will!')
                            print('Roth: Engaging per your orders Admiral!\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            print('Roth: Weapons firing!')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: Hmmm, I mislike those odds')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter either y or n')
                    break

                elif tactic == 3:
                    print('You: We will aim to hit three-quarters of them')
                    target_factor = 0.75
                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))

                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    print(f'Roth: We have {player_firepower} turrets')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: We will be facing {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
                    effective_enemy_firepower = (
                        calculate_effective_enemy_firepower(
                            effective_enemy_strength))
                    eef = effective_enemy_firepower
                    print(f'Roth: They have {eef} turrets\n')
                    effective_firepower_difference = firepower_comparator(
                        player_firepower, effective_enemy_firepower)
                    efd = effective_firepower_difference
                    #  efd and eef are used here because of line length issues
                    if effective_firepower_difference < 0:
                        print(f'Roth: We will have {abs(efd)} fewer turrets')
                    elif effective_firepower_difference > 0:
                        print(f'Roth: We will have {efd} more turrets')
                    elif effective_firepower_difference == 0:
                        print('Roth: What a coincidence!')
                        print('Both our fleets have the same firepower!')

                    player_combat_power = player_combat_power_calculator(
                        player_firepower)
                    effective_enemy_combat_power = (
                        effective_enemy_combat_power_calculator(
                            effective_enemy_firepower))
                    diff = player_combat_power - effective_enemy_combat_power

                    if diff > 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: We have the advantage in combat power')
                        firepower_factor = (
                            cpd / player_firepower)
                        losses_factor = (
                            (effective_enemy_firepower / cpd))
                        losses_factor = losses_factor / 5

                    elif diff == 0:
                        combat_power_difference = 1
                        print('Roth: There is no difference in combat power')
                        print('Roth: We are evenly matched')
                        print('Roth: Are you sure this is a good idea?')
                        if PLAYER_EXPERIENCE > 1.0:
                            print('Roth: Our experience gives us a advantage')
                            print('Roth: But this will still be bloody')
                        firepower_factor = 0.50
                        losses_factor = 0.50

                    elif diff < 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: They have the advantage in combat power')
                        print('Roth: This is a bad idea Admiral')
                        print('Roth: We should consider another approach')
                        firepower_factor = (
                            player_firepower / cpd) / 5
                        losses_factor = (
                            cpd / effective_enemy_firepower)

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    projected_player_losses = (round(losses_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    ppl = projected_player_losses
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print(f'Roth: We will probably lose {ppl}% of our ships')
                    print('\n')

                    print('Roth: Shall we proceed?')
                    while True:
                        proceed_decision = input(
                            'Press y to proceed, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: I like the sound of those odds')
                            print('You: All ships, fire at will!')
                            print('Roth: Engaging per your orders Admiral!\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            print('Roth: Weapons firing!')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: Hmmm, I mislike those odds')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter either y or n')
                    break

                elif tactic == 4:
                    print('You: Maximum attack! Target all enemy ships!')
                    target_factor = 1

                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))

                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    print(f'Roth: We have {player_firepower} turrets')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: We will be facing {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
                    effective_enemy_firepower = (
                        calculate_effective_enemy_firepower(
                            effective_enemy_strength))
                    eef = effective_enemy_firepower
                    print(f'Roth: They have {eef} turrets\n')
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
                        print('Both our fleets have equal firepower!')

                    player_combat_power = player_combat_power_calculator(
                        player_firepower)
                    effective_enemy_combat_power = (
                        effective_enemy_combat_power_calculator(
                            effective_enemy_firepower))
                    diff = player_combat_power - effective_enemy_combat_power

                    if diff > 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: We have the advantage in combat power')
                        firepower_factor = (
                            cpd / player_firepower)
                        losses_factor = (
                            (effective_enemy_firepower / cpd))
                        losses_factor = losses_factor / 5

                    elif diff == 0:
                        combat_power_difference = 1
                        print('Roth: There is no difference in combat power')
                        print('Roth: We are evenly matched')
                        print('Roth: Are you sure this is a good idea?')
                        if PLAYER_EXPERIENCE > 1.0:
                            print('Roth: Our experience gives us a advantage')
                            print('Roth: But this will still be bloody')
                        firepower_factor = 0.50
                        losses_factor = 0.50

                    elif diff < 0:
                        combat_power_difference = (
                            combat_power_difference_calculator(diff))
                        cpd = combat_power_difference
                        print('Roth: They have the advantage in combat power')
                        print('Roth: This is a bad idea Admiral')
                        print('Roth: We should consider another approach')
                        firepower_factor = (
                            player_firepower / cpd) / 5
                        losses_factor = (
                            cpd / effective_enemy_firepower)

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    projected_player_losses = (round(losses_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    ppl = projected_player_losses
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print(f'Roth: We will probably lose {ppl}% of our ships')
                    print('\n')

                    print('Roth: Shall we proceed?')
                    while True:
                        proceed_decision = input(
                            'Press y to proceed, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: I like the sound of those odds')
                            print('You: All ships, fire at will!')
                            print('Roth: Engaging per your orders Admiral!\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            print('Roth: Weapons firing!')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: Hmmm, I mislike those odds')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter either y or n')
                    break

                elif tactic == 5:
                    global MISSILE_VOLLEYS
                    print('You: Fire missiles!')
                    if MISSILE_VOLLEYS >= 2:
                        print(f'Roth: We can fire {MISSILE_VOLLEYS} barrages')
                    elif MISSILE_VOLLEYS == 1:
                        print('Roth: We have enough missiles for 1 barrage')
                    elif MISSILE_VOLLEYS > 0 and MISSILE_VOLLEYS < 1:
                        print('Roth: We have some missiles')
                        print("Roth: But we can't break the enemy defences")
                        fight_engagement(
                            enemy_firepower, enemy_group_strength,
                            number_enemy_ships)
                    elif MISSILE_VOLLEYS == 0:
                        print('Roth: We currently have no missiles remaining')
                        fight_engagement(
                            enemy_firepower, enemy_group_strength,
                            number_enemy_ships)

                    target_factor = 1

                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))
                    missiles_fired = (
                        (PLAYER_SHIPS['battleships']
                            * MISSILE_LAUNCHERS['battleships'])
                        + (PLAYER_SHIPS['cruisers']
                            * MISSILE_LAUNCHERS['cruisers'])
                        + (PLAYER_SHIPS['escorts']
                            * MISSILE_LAUNCHERS['escorts'])
                    )
                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: Our missiles will target {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
                    effective_enemy_firepower = (
                        calculate_effective_enemy_firepower(
                            effective_enemy_strength))
                    print('Roth: Our missiles have a long range')
                    print('Roth: We will not face any return fire')
                    print(f'Roth: We will fire {missiles_fired} missiles')
                    print('Roth: We will use up 1 of our missile barrages')

                    firepower_factor = (
                        missiles_fired / effective_enemy_firepower)
                    if firepower_factor > 1:
                        firepower_factor = 1
                    losses_factor = 0

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print('Roth: We will not lose any of our ships')
                    print('\n')

                    print('Roth: Shall we fire a missile barrage?')
                    while True:
                        proceed_decision = input(
                            'Press y to fire missiles, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: Fire missiles!')
                            print('Roth: Firing missiles!\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            MISSILE_VOLLEYS -= 1
                            print(f'Roth: We have {MISSILE_VOLLEYS} barrages')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: We would be wasting our missiles')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter either y or n')
                    break

                elif tactic == 6:
                    global MINE_STOCKS
                    print('You: We will lay a minefield')
                    print('You: Then we will lure the enemy into it')
                    if MINE_STOCKS >= 2:
                        print(f'Roth: We have mines for {MINE_STOCKS} fields')
                    elif MINE_STOCKS == 1:
                        print('Roth: We have enough mines for 1 minefield')
                    elif MINE_STOCKS > 0 and MINE_STOCKS < 1:
                        print('Roth: We have some mines')
                        print('Roth: But not enough to lay a decent field')
                        fight_engagement(
                            enemy_firepower, enemy_group_strength,
                            number_enemy_ships)
                    elif MINE_STOCKS == 0:
                        print('Roth: We currently have no mines remaining')
                        fight_engagement(
                            enemy_firepower, enemy_group_strength,
                            number_enemy_ships)

                    target_factor = 1
                    effective_enemy_strength = (
                        calculate_effective_enemy_strength(
                            enemy_group_strength, target_factor))
                    mines_laid = (
                        PLAYER_SHIPS['battleships'] * (
                            MINE_LAYERS['battleships'])
                        + PLAYER_SHIPS['cruisers'] * (
                            MINE_LAYERS['cruisers'])
                    )
                    for key, value in PLAYER_SHIPS.items():
                        print(f'Roth: We have {value} {key}')
                    print('\n')
                    for key, value in effective_enemy_strength.items():
                        print(f'Roth: Our mines will target {value} {key}')
                    print('\n')
                    input('Press enter to continue\n')
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

                    projected_enemy_destroyed = (
                        round(firepower_factor, 2)) * 100
                    ped = projected_enemy_destroyed
                    input('Press enter to continue\n')
                    print(f'Roth: We can probably destroy {ped}% of the enemy')
                    print('Roth: We will not lose any of our ships')

                    print('Roth: Shall we lay a minefield?')
                    while True:
                        proceed_decision = input(
                            'Press y to lay a minefield, or n to break off:\n')
                        if proceed_decision == 'y':
                            print('You: Yes - lay mines')
                            print('Roth: Deploying mines now Admiral\n')
                            enemy_group_strength = update_enemy(
                                    effective_enemy_strength,
                                    enemy_group_strength,
                                    firepower_factor, PLAYER_EXPERIENCE)
                            PLAYER_SHIPS = update_player(losses_factor)
                            PLAYER_SUPPLIES -= 1
                            MINE_STOCKS -= 1
                            print(f'Roth: We can now lay {MINE_STOCKS} fields')
                            input('Press enter to continue\n')
                            break

                        elif proceed_decision == 'n':
                            print('You: We would be wasting our mines')
                            print('You: I will consider a different tactic\n')
                            fight_engagement(
                                enemy_firepower, enemy_group_strength,
                                number_enemy_ships)
                            break

                        else:
                            print('Please enter y or n')
                    break

                else:
                    print('Enter a number between 1 and 6')

            except ValueError:
                print('Enter a number between 1 and 6 to select your tactic')
                fight_engagement(
                    enemy_firepower, enemy_group_strength,
                    number_enemy_ships)

        PLAYER_SUPPLIES -= 1
        print(f'Roth: We now have {PLAYER_SUPPLIES} supplies\n')

        for key, value in ENEMY_LOCAL_LOSSES.items():
            print(f'Roth: We destroyed {value} enemy {key} in that firing run')
        print('\n')

        for key, value in enemy_group_strength.items():
            print(f'Roth: The enemy now has {value} {key} remaining')
        print('\n')
        input('Press enter to continue\n')
        for key, value in PLAYER_LOCAL_LOSSES.items():
            print(f'Roth: That run cost us {value} {key}')
        print('\n')

        for key, value in PLAYER_SHIPS.items():
            print(f'Roth: We now have {value} {key}')
        print('\n')
        input('Press enter to continue\n')
        if (PLAYER_SHIPS['battleships'] == 0 and
            PLAYER_SHIPS['cruisers'] == 0 and
                PLAYER_SHIPS['escorts'] == 0):
            print('Roth: Shields failing Admiral!')
            input('Press enter to continue\n')
            print('Roth: Multiple hull breaches!')
            input('Press enter to continue\n')
            print('Roth: The reactor is melting down!')
            input('Press enter to continue\n')
            print('Roth: Oh Sh......')
            input('Press enter to continue\n')
            print('BOOOOOOOOOOOM')
            input('Press enter to continue\n')
            print('Your tactical decisions have resulted in defeat')
            print('Would you like to try again?')
            new_game_decision = input('Press y to try again or n to quit:\n')
            if new_game_decision == 'y':
                new_game_reset()
                new_game()
            elif new_game_decision == 'n':
                main()

        elif PLAYER_SUPPLIES == 0:
            print('Roth: Admiral, our ships are out of fuel and ammunition!')
            input('Press enter to continue\n')
            print('Roth: Enemy ships closing in!')
            print('Roth: We cannot fight back!')
            input('Press enter to continue\n')
            print('You: Very well, broadcast surrender')
            input('Press enter to continue\n')
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
            input('Press enter to continue\n')
            print('Roth: Shall we re-engage?')
            while True:
                reengage_decision = input(
                    'Press y to re-engage the enemy, or n to leave them:\n')
                if reengage_decision == 'y':
                    print('You: Indeed we shall! Good hunting!')
                    input('Press enter to continue\n')
                    fight_engagement(
                        enemy_firepower, enemy_group_strength,
                        number_enemy_ships)
                    break
                elif reengage_decision == 'n':
                    print('You: We have done enough damage')
                    print('You: I do not want to risk our ships further')
                    update_enemy_bypassed(enemy_group_strength)
                    ENEMY_GROUPS_DAMAGED += 1

                    PLAYER_TOTAL_DESTROYED = {
                        'battleships': (
                            PLAYER_TOTAL_DESTROYED['battleships']
                            + PLAYER_DESTROYED_SHIPS['battleships']),
                        'cruisers': PLAYER_TOTAL_DESTROYED['cruisers'] + (
                            PLAYER_DESTROYED_SHIPS['cruisers']),
                        'escorts': PLAYER_TOTAL_DESTROYED['escorts'] + (
                            PLAYER_DESTROYED_SHIPS['escorts'])
                    }

                    PLAYER_TOTAL_DAMAGED = {
                        'battleships': (
                            PLAYER_TOTAL_DAMAGED['battleships']
                            + PLAYER_DAMAGED_SHIPS['battleships']),
                        'cruisers': PLAYER_TOTAL_DAMAGED['cruisers'] + (
                            PLAYER_DAMAGED_SHIPS['cruisers']),
                        'escorts': PLAYER_TOTAL_DAMAGED['escorts'] + (
                            PLAYER_DAMAGED_SHIPS['escorts'])
                    }
                    input('Press enter to continue\n')
                    for key, value in ENEMY_BATTLE_LOSSES.items():
                        print(f'Roth: We destroyed {value} {key}')
                    print('\n')

                    for key, value in PLAYER_BATTLE_LOSSES.items():
                        print(f'Roth: {value} of our {key} were knocked out')
                    print('\n')
                    input('Press enter to continue\n')
                    print('Roth: Of those...\n')

                    total_crew_calculator()
                    excess_crew_calculator()

                    for key, value in PLAYER_DESTROYED_SHIPS.items():
                        print(f'Roth: {value} of our {key} were destroyed')
                    print('Roth: We cannot recover them\n')

                    for key, value in PLAYER_DAMAGED_SHIPS.items():
                        print(f'Roth: {value} of our {key} were badly damaged')
                    print('Roth: They cannot keep up with the fleet')
                    print('Roth: We will have to leave them behind')
                    print('Roth: Follow-on forces could repair them')
                    print('Roth: They may return to us in time\n')
                    reset_battle_losses()
                    input('Press enter to continue\n')
                    break

                else:
                    print('Please enter either y or n')

        elif (enemy_group_strength['battleships'] == 0 and
                enemy_group_strength['cruisers'] == 0 and
                enemy_group_strength['escorts'] == 0):
            print('Roth: We have knocked out all enemy ships, Admiral\n')
            ENEMY_GROUPS_DESTROYED += 1

            PLAYER_TOTAL_DESTROYED = {
                'battleships': PLAYER_TOTAL_DESTROYED['battleships'] + (
                    PLAYER_DESTROYED_SHIPS['battleships']),
                'cruisers': PLAYER_TOTAL_DESTROYED['cruisers'] + (
                    PLAYER_DESTROYED_SHIPS['cruisers']),
                'escorts': PLAYER_TOTAL_DESTROYED['escorts'] + (
                    PLAYER_DESTROYED_SHIPS['escorts'])
            }

            PLAYER_TOTAL_DAMAGED = {
                'battleships': PLAYER_TOTAL_DAMAGED['battleships'] + (
                    PLAYER_DAMAGED_SHIPS['battleships']),
                'cruisers': PLAYER_TOTAL_DAMAGED['cruisers'] + (
                    PLAYER_DAMAGED_SHIPS['cruisers']),
                'escorts': PLAYER_TOTAL_DAMAGED['escorts'] + (
                    PLAYER_DAMAGED_SHIPS['escorts'])
            }
            input('Press enter to continue\n')
            for key, value in ENEMY_BATTLE_LOSSES.items():
                print(f'Roth: We destroyed {value} {key} in that battle')
            print('\n')

            for key, value in PLAYER_BATTLE_LOSSES.items():
                print(f'Roth: {value} of our {key} were knocked out')
            print('\n')
            input('Press enter to continue\n')
            print('Roth: Of those...\n')

            total_crew_calculator()
            excess_crew_calculator()

            for key, value in PLAYER_DESTROYED_SHIPS.items():
                print(f'Roth: {value} of our {key} were destroyed outright')
            print('Roth: We cannot recover them\n')
            number_destroyed_player = int(
                PLAYER_DESTROYED_SHIPS['battleships']
                + PLAYER_DESTROYED_SHIPS['cruisers']
                + PLAYER_DESTROYED_SHIPS['escorts']
            )
            for key, value in PLAYER_DAMAGED_SHIPS.items():
                print(f'Roth: {value} of our {key} were badly damaged')
            print('Roth: They cannot keep up with the fleet')
            print('Roth: They will have to be left behind')
            print('Roth: But follow-on forces might be able to repair them')
            print('Roth: They may return to us in time\n')

            reset_battle_losses()
            input('Press enter to continue\n')
            boardable_ships = {
                'battleships': math.floor(
                    starting_enemy_ships['battleships'] * 0.20),
                'cruisers': math.floor(
                    starting_enemy_ships['cruisers'] * 0.15),
                'escorts': math.floor(
                    starting_enemy_ships['escorts'] * 0.10)
            }
            supplies_gained_enemy = math.floor(
                number_enemy_ships / 30
            )
            supplies_gained_player = math.floor(
                number_destroyed_player / 20
            )
            sg = supplies_gained_enemy + supplies_gained_player
            PLAYER_SUPPLIES += sg
            print(f'Roth: We salvaged {sg} supplies from destroyed ships')
            input('Press enter to continue\n')
            print('Roth: Some of the enemy ships may be salvagable')
            print('Roth: Shall we attempt to board the enemy ships?')
            while True:
                boarding_decision = input(
                    'Press y to board the enemy ships, or n to move on:\n')
                if boarding_decision == 'y':
                    print('You: Yes, hopefully we can bolster our numbers')
                    input('Press enter to continue\n')
                    boarding_operation(boardable_ships)
                    break
                elif boarding_decision == 'n':
                    print("You: These wrecks aren't worth it")
                    print('Roth: Very well, We are clear to move on')
                    input('Press enter to continue\n')
                    break
                else:
                    print('Please enter either y or n')

    fight_engagement(
        enemy_firepower, enemy_group_strength, number_enemy_ships)


def total_crew_calculator():
    """
    Function that is called in the fight_engagement and player_fleet_status
    functions to calculate the total crew available to the player
    """
    global TOTAL_CREW
    TOTAL_CREW = TOTAL_CREW - ((
        PLAYER_BATTLE_LOSSES['battleships'] * SHIP_CREW['battleship']
        + PLAYER_BATTLE_LOSSES['cruisers'] * SHIP_CREW['cruiser']
        + PLAYER_BATTLE_LOSSES['escorts'] * SHIP_CREW['escort'])
        -
        (PLAYER_BATTLE_LOSSES['battleships'] * RECOVERED_CREW['battleship']
            + PLAYER_BATTLE_LOSSES['cruisers'] * RECOVERED_CREW['cruiser']
            + PLAYER_BATTLE_LOSSES['escorts'] * RECOVERED_CREW['escort']))
    return TOTAL_CREW


def excess_crew_calculator():
    """
    Function that is called in the fight_engagement and
    player_fleet_status functions to calculate the excess crew
    available to the player for boarding actions
    """
    global EXCESS_CREW
    EXCESS_CREW = TOTAL_CREW - (
        MINIMUM_SHIP_CREW['battleship'] * PLAYER_SHIPS['battleships']
        + MINIMUM_SHIP_CREW['cruiser'] * PLAYER_SHIPS['cruisers']
        + MINIMUM_SHIP_CREW['escort'] * PLAYER_SHIPS['escorts']
    )
    return EXCESS_CREW


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
    Updates global ENEMY_BYPASSED dictionary
    Keeps track of the number of enemy ships that have been bypassed
    """
    global ENEMY_BYPASSED
    ENEMY_BYPASSED = {
        'battleships': ENEMY_BYPASSED['battleships'] + (
            enemy_group_strength['battleships']),
        'cruisers': ENEMY_BYPASSED['cruisers'] + (
            enemy_group_strength['cruisers']),
        'escorts': ENEMY_BYPASSED['escorts'] + (
            enemy_group_strength['escorts'])
    }
    return ENEMY_BYPASSED


def calculate_player_firepower(PLAYER_SHIPS):
    """
    Dynamically calculates player firepower
    based on the number of ships they have
    """
    player_firepower = (
        (PLAYER_SHIPS['battleships'] * SHIP_FIREPOWER['battleship'])
        + (PLAYER_SHIPS['cruisers'] * SHIP_FIREPOWER['cruiser'])
        + (PLAYER_SHIPS['escorts'] * SHIP_FIREPOWER['escort'])
    )
    return player_firepower


def boarding_operation(boardable_ships):
    """
    Called when the player wants to board and salvage
    enemy ships after a battle has been won
    """
    global MARINES
    global PLAYER_SHIPS
    global PLAYER_SUPPLIES
    global TOTAL_CREW
    global EXCESS_CREW
    global MARINE_EXPERIENCE
    global SALVAGED_SHIPS

    available_crew = excess_crew_calculator()

    BOARDED_SHIPS = {
        'battleship': 0,
        'cruiser': 0,
        'escort': 0
    }

    if (boardable_ships['battleships'] == 0 and
        boardable_ships['cruisers'] == 0 and
            boardable_ships['escorts'] == 0):
        print('Roth: There are no more ships left to board\n')
    elif MARINES < 20:
        print('Roth: We do not have enough Marines')
        print('Roth: We cannot board even one escort')
    elif available_crew < 160:
        print('Roth: We do not have enough crew left to crew a captured ship')
    else:
        for key, value in boardable_ships.items():
            print(f'Roth: There are {value} {key} we can board')
        print('\n')
        print(f'Roth: We have {MARINES} Marines')
        print(f'Roth: We have {available_crew} sailors available')
        print(f'Roth: We have {PLAYER_SUPPLIES} repair supplies')
        print('\n')
        for key, value in BOARDING_TACTICS.items():
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
                elif MARINES < 250:
                    print('Roth: We do not have enough Marines')
                    print('Roth: We cannot board the battleship')
                    print('Roth: We might be able to board an enemy cruiser')
                    boarding_operation(boardable_ships)
                else:
                    print('Roth: Very well, assault shuttles away')
                    boardable_ships['battleships'] -= 1
                    marine_casualties = int(250 - (MARINE_EXPERIENCE * 125))
                    MARINES -= marine_casualties
                    PLAYER_SHIPS['battleships'] += 1
                    BOARDED_SHIPS['battleship'] += 1
                    SALVAGED_SHIPS['battleships'] += 1
                    PLAYER_SUPPLIES -= 1
                    EXCESS_CREW -= MINIMUM_SHIP_CREW['battleship']
                    print(f'Roth: We lost {marine_casualties} Marines')
                    print('Roth: But we took the battleship')
                    boarding_operation(boardable_ships)

                break

            elif ship_to_board == '2':
                print('You: We shall board an enemy cruiser')
                if boardable_ships['cruisers'] == 0:
                    print('Roth: There are no enemy cruisers to board')
                    boarding_operation(boardable_ships)
                elif MARINES < 120:
                    print('Roth: We do not have enough Marines')
                    print('Roth: We cannot board an enemy cruiser')
                    print('Roth: We might be able to board an enemy escort')
                    boarding_operation(boardable_ships)
                else:
                    print('Roth: Very well, assault shuttles away')
                    boardable_ships['cruisers'] -= 1
                    marine_casualties = int(120 - (MARINE_EXPERIENCE * 80))
                    MARINES -= marine_casualties
                    PLAYER_SHIPS['cruisers'] += 1
                    BOARDED_SHIPS['cruiser'] += 1
                    SALVAGED_SHIPS['cruisers'] += 1
                    PLAYER_SUPPLIES -= 1
                    EXCESS_CREW -= MINIMUM_SHIP_CREW['cruiser']
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
                    marine_casualties = int(20 - (MARINE_EXPERIENCE * 15))
                    MARINES -= marine_casualties
                    PLAYER_SHIPS['escorts'] += 1
                    BOARDED_SHIPS['escort'] += 1
                    SALVAGED_SHIPS['escorts'] += 1
                    PLAYER_SUPPLIES -= 1
                    EXCESS_CREW -= MINIMUM_SHIP_CREW['escort']
                    print(f'Roth: We lost {marine_casualties} Marines')
                    print('Roth: but the escort has been added to our screen')
                    boarding_operation(boardable_ships)

                break

            elif ship_to_board == '4':
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

                if MARINES < marines_required:
                    print('Roth: We do not have sufficient Marines, sir')
                    print("Roth: We can't take all enemy ships simultaneously")
                    print('Roth: We might be able to board some of them')
                    boarding_operation(boardable_ships)

                elif PLAYER_SUPPLIES < supplies_required:
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

                    PLAYER_SHIPS['battleships'] += battleships
                    PLAYER_SHIPS['cruisers'] += cruisers
                    PLAYER_SHIPS['escorts'] += escorts

                    BOARDED_SHIPS['battleship'] += battleships
                    BOARDED_SHIPS['cruiser'] += cruisers
                    BOARDED_SHIPS['escort'] += escorts

                    SALVAGED_SHIPS['battleships'] += battleships
                    SALVAGED_SHIPS['cruisers'] += cruisers
                    SALVAGED_SHIPS['escorts'] += escorts

                    EXCESS_CREW -= (
                        (MINIMUM_SHIP_CREW['battleship']
                            * boardable_ships['battleships'])
                        + (MINIMUM_SHIP_CREW['cruiser']
                            * boardable_ships['cruisers'])
                        + (MINIMUM_SHIP_CREW['escort']
                            * boardable_ships['escorts'])
                    )

                    marine_casualties_bb = int(
                        battleships * (500 - (MARINE_EXPERIENCE * 250)))
                    marine_casualties_cc = int(
                        cruisers * (120 - (MARINE_EXPERIENCE * 80)))
                    marine_casualties_dd = int(
                        escorts * (20 - (MARINE_EXPERIENCE * 15)))

                    marine_casualties = (
                        marine_casualties_bb
                        + marine_casualties_cc
                        + marine_casualties_dd
                    )

                    for key, value in BOARDED_SHIPS.items():
                        print(f'Roth: We boarded {value} {key}')

                    print(f'Roth: We lost {marine_casualties} Marines')
                    MARINES -= marine_casualties
                    print(f'Roth: We now have {MARINES} Marines')

                    PLAYER_SUPPLIES -= (
                        boardable_ships['battleships']
                        + boardable_ships['cruisers']
                        + boardable_ships['escorts']
                    )

                    boardable_ships['battleships'] = 0
                    boardable_ships['cruisers'] = 0
                    boardable_ships['escorts'] = 0

                break

            elif ship_to_board == '5':
                print('You: We have salvaged enough ships. Scuttle the rest')
                print('Roth: Indeed, better to save our Marines')
                break

            else:
                print('Please enter a number between 1 and 5')

        MARINE_EXPERIENCE = (
            BOARDED_SHIPS['battleship'] * MARINE_EXPERIENCE_GAINS['battleship']
            + BOARDED_SHIPS['cruiser'] * MARINE_EXPERIENCE_GAINS['cruiser']
            + BOARDED_SHIPS['escort'] * MARINE_EXPERIENCE_GAINS['escort']
        )

        BOARDED_SHIPS = {
            'battleship': 0,
            'cruiser': 0,
            'escort': 0
        }


def reset_battle_losses():
    """
    Sets the values of all keys within PLAYER_BATTLE_LOSSES,
    PLAYER_DESTROYED_SHIPS,
    PLAYER_DAMAGED_SHIPS
    and ENEMY_BATTLE_LOSSES to 0
    """
    global PLAYER_BATTLE_LOSSES
    global PLAYER_DESTROYED_SHIPS
    global PLAYER_DAMAGED_SHIPS
    global ENEMY_BATTLE_LOSSES

    PLAYER_BATTLE_LOSSES = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    PLAYER_DESTROYED_SHIPS = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    PLAYER_DAMAGED_SHIPS = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    ENEMY_BATTLE_LOSSES = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }


def player_fleet_status():
    """
    Function that can be called at the start of each mission
    Displays the current status of the player's fleet
    As well as supplies, mines, missiles, crew and Marines
    Also displays the allied groups that have joined up
    """
    player_firepower = calculate_player_firepower(PLAYER_SHIPS)
    for key, value in PLAYER_SHIPS.items():
        print(f'Roth: We currently have {value} {key}')
    print('')
    print(f"Roth: We currently have {player_firepower} turrets")
    print(f'Roth: We have enough missiles for {MISSILE_VOLLEYS} barrages')
    print(f'Roth: We have enough mines for {MINE_STOCKS} mine-fields')
    print(f'Roth: We currently have {PLAYER_SUPPLIES} supplies\n')
    input('Press enter to continue\n')
    if (PLAYER_TOTAL_DESTROYED['battleships'] == 0 and
        PLAYER_TOTAL_DESTROYED['cruisers'] == 0 and
            PLAYER_TOTAL_DESTROYED['escorts'] == 0):
        print('Roth: None of our ships have been destroyed\n')
    else:
        for key, value in PLAYER_TOTAL_DESTROYED.items():
            print(f'Roth: {value} of our {key} have been destroyed')
        print('\n')
    if (PLAYER_TOTAL_DAMAGED['battleships'] == 0 and
        PLAYER_TOTAL_DAMAGED['cruisers'] == 0 and
            PLAYER_TOTAL_DAMAGED['escorts'] == 0):
        print('Roth: None of our ships have been damaged\n')
    else:
        for key, value in PLAYER_TOTAL_DAMAGED.items():
            print(f'Roth: {value} of our {key} have been damaged')
        print('\n')
    if (SALVAGED_SHIPS['battleships'] == 0 and
        SALVAGED_SHIPS['cruisers'] == 0 and
            SALVAGED_SHIPS['escorts'] == 0):
        print('Roth: No enemy ships have been salvaged\n')
    else:
        for key, value in SALVAGED_SHIPS.items():
            print(f'Roth: {value} enemy {key} have been salvaged')
        print('\n')
    if OSIRIS_FLEET_HELPED == 1:
        input('Press enter to continue\n')
        print('Roth: The Osiris defence forces have joined us\n')
        for key, value in OSIRIS_GROUP.items():
            print(f'Roth: They brought {value} {key}')
    if OSIRIS_MORE_SHIPS == 1:
        print('Roth: Osiris also released some more ships\n')
        for key, value in OSIRIS_EXTRA.items():
            print(f'Roth: They gave us {value} {key}')
    if ALLIED_CONVOY_JOINED == 1:
        print('Roth: The allied convoy from Medusa has joined up\n')
        for key, value in ALLIED_CONVOY.items():
            print(f'Roth: They brought us {value} {key}')
        print('\n')
    if LACONIA_SHIPS_HELPED == 1:
        print('Roth: The allied ships from Laconia have joined up\n')
        for key, value in LACONIA_SHIPS.items():
            print(f'Roth: They brought us {value} {key}')
        print('\n')
    input('Press enter to continue\n')
    print(f'Roth: We currently have {TOTAL_CREW} sailors in the fleet')
    if EXCESS_CREW <= 0:
        print('Roth: We cannot spare any crew for other duties')
    else:
        print(f'Roth: However, we can spare {EXCESS_CREW} for other duties\n')
    if PLAYER_EXPERIENCE == 1:
        print('Roth: Our crews are trained, but green and inexperienced\n')
    elif PLAYER_EXPERIENCE > 1 and PLAYER_EXPERIENCE <= 1.1:
        print('Roth: Our crews have gained some battle experience\n')
    elif PLAYER_EXPERIENCE > 1.1 and PLAYER_EXPERIENCE <= 1.2:
        print('Roth: Our crews are seasoned veterans\n')
    elif PLAYER_EXPERIENCE > 1.2:
        print('Roth: Our crews are hardened combat veterans\n')
    print(f'\nRoth: Our ships carry {MARINES} Marines')
    if MARINES < 1800:
        print('Roth: We have lost Marines in combat and to ship destruction')
    if MARINES > 1800:
        print('Roth: We have picked up some additional Marines')
    if MARINE_EXPERIENCE == 1.0:
        print('Roth: Our Marines are inexperienced in boarding actions\n')
    elif MARINE_EXPERIENCE > 1.0 and MARINE_EXPERIENCE <= 1.3:
        print('Roth: Our Marines have gained some combat experience\n')
    elif MARINE_EXPERIENCE > 1.3 and MARINE_EXPERIENCE <= 1.6:
        print('Roth: Our Marines are now seasoned veterans\n')
    elif MARINE_EXPERIENCE > 1.7:
        print('Roth: Our Marines are hardened veterans\n')
    input('Press enter to continue\n')


def ship_capabilities():
    """
    Function that displays the capabilities of each class of ship
    """
    print('Battleships are the monsters of space combat')
    print('Roth: They are heavily armoured and armed')
    print(f"Battleships have {SHIP_FIREPOWER['battleship']} turrets")
    print('Battleships have 4 missile launchers')
    print('Battleships have 2 mine-tubes')
    print(f"Battleships have {SHIP_CREW['battleship']} sailors")
    print('Battleships also carry 40 Marines\n')
    input('Press enter to continue\n')
    print('Cruisers are midweight combatants')
    print(f"Cruisers have {SHIP_FIREPOWER['cruiser']} turrets")
    print('Cruisers have 2 missile launchers')
    print('Cruisers have 1 mine-tube')
    print(f"Cruisers have {SHIP_CREW['cruiser']} sailors")
    print('Cruisers carry 20 Marines\n')
    input('Press enter to continue\n')
    print('Escorts are light screening ships, effective in numbers')
    print(f"Escorts have {SHIP_FIREPOWER['escort']} turrets")
    print('Escorts have 1 missile launcher')
    print('Escorts do not carry mine-tubes')
    print(f"Escorts have {SHIP_CREW['escort']} sailors")
    print('Escorts do not carry Marines\n')
    input('Press enter to continue\n')


def tactics():
    """
    Function that is called in new_game to inform the player of what tactics
    they can use in an engagement, what the tactic will do
    and what the consequences are
    """
    print('You: Broadly speaking, we can use 6 tactics:')
    for key, value in TACTICAL_LIBRARY.items():
        print(f'We can {value}')

    print('\n')
    print('You: Attacking 25% of the enemy has several advantages')
    print('You: We will greatly concentrate our firepower')
    print('You: We destroy many enemy ships')
    print('You: We should also face little return fire, so losses will be low')
    print("You: It's a good approach for facing down superior enemy numbers")
    print('You: However, there are disadvantages too')
    print('You: It will take a lot of fuel and ammo to wear down enemy forces')
    input('Press enter to continue\n')
    print('You: Attacking 50% of the enemy has advantages too')
    print('You: Our fire will be less concentrated')
    print('You: We will also be exposed to more enemy fire')
    print('You: So we could take heavier losses')
    print('You: But we will require fewer firing runs overall')
    print('You: So we be more efficient in terms of fuel and ammo')
    input('Press enter to continue\n')
    print('You: Striking 75% of the enemy has advantages as well')
    print('You: We will spread out out fire even more')
    print('You: And potentially be exposed to more enemy fire')
    print('You: We could suffer more casualties')
    print('You: But we could require far fewer firing runs')
    print('You: So, we should use less fuel and ammo')
    print('You: This is a could approach for weakened enemy groups')
    input('Press enter to continue\n')
    print('You: Finally, we could attack all of the enemy')
    print('You: This would be risky, throwing caution to the wind')
    print('You: Our fire will be very spread out')
    print('You: And we could suffer badly')
    print('You: But we will use very little fuel and ammo')
    print('You: This is the perfect tactic for smaller enemy groups')
    input('Press enter to continue\n')
    print('You: We could also choose to fire a barrage of missiles')
    print('You: Missiles are long range weapons')
    print('You: So, we will be safe from return fire')
    print('You: However, strong enemy groups could shoot down many missiles')
    print('You: That said, they are a good way of softening up enemy groups')
    print('You: Then we can go in with a conventional firing run')
    print('You: Our missile stocks are limited')
    print('You: So they should be used sparingly')
    input('Press enter to continue\n')
    print('You: We could also choose to lay a minefield')
    print('You: We can lay mines and the pull back')
    print('You: The enemy will then run into our mines')
    print('You: So, we will not face any return fire')
    print('You: Mines are potent and cannot be shot down')
    print('You: We do not have many mines')
    print('You: So we should carefully consider using them')
    input('Press enter to continue\n')
    print('You: Once the battle is done, some enemy ships may be salvageable')
    print('You: We will need to use our Marines to board them')
    print('You: They would make excellent additions to the fleet')
    print('You: However, we could lose many Marines')
    print('You: We would then be without an important capability')
    input('Press enter to continue\n')
    print('Roth: Thank you Admiral, that was informative')
    print('You: You are welcome Roth - watch and learn')
    print('Maybe you will command a fleet youself one day')
    input('Press enter to continue\n')


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
