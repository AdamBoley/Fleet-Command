def mission_x():
    global player_experience
    print('\n  BEGIN MISSION X  \n')
    print('Roth: Do you want to review the fleet, Admiral?')
    fleet_status_decision = input('Please press y to see fleet status or n to begin the mission:\n')  # gonna need some input checking here
    if fleet_status_decision == 'y':
        player_fleet_status()
    else:
        print('Roth: Very well Admiral')
    enemy_group_X = {
        'battleships': 0,
        'cruisers': 0,
        'escorts': 0
    }

    enemy_firepower = enemy_firepower_calculator(enemy_group_three)
    player_firepower = calculate_player_firepower(player_ships)

    for key, value in enemy_group_x.items():
        print(f'Roth: The enemy has {value} {key}')
    print(f'Based on their numbers, the enemy have {enemy_firepower} turrets')

    firepower_difference = firepower_comparator(player_firepower, enemy_firepower)
    if firepower_difference < 0:
        print(f'Roth: We have {abs(firepower_difference)} fewer turrets than they do')
    else:
        print(f'Roth: We have {firepower_difference} more turrets than they do')

    print('Roth: This will be a tough battle, Admiral')
    print('Roth: Shall we engage?')
    engage_decision_mission_x = input('press y to engage, or n to disengage:\n')
    if engage_decision_mission_x == 'y':
        print('You: Indeed we shall, we cannot allow a force of this strength to roam free')
        fight_battle(enemy_firepower, enemy_group_x)
        player_experience += 0.1
    elif engage_decision_mission_x == 'n':
        print('You: I think not - follow-on forces should be able to handle them')
        update_enemy_bypassed(enemy_group_c)
    mission_x+1