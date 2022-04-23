total_crew = (
    (player_ships['battleships'] * ship_crew['battleship'])
    + (player_ships['cruisers'] * ship_crew['cruiser'])
    + (player_ships['escorts'] * ship_crew['escort'])
)

marines = (
    (player_ships['battleships'] * 40)
)

mines = (
    (player_ships['battleships'] * 10)
)

missiles = (
    (player_ships['battleships'] * 20)
    + (player_ships['cruisers'] * 15)
)

fleet_assets = {
    'Marines': marines,
    'Mines': mines,
    'Missiles': missiles
}

experience = 1