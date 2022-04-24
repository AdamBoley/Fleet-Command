![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome AdamBoley,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!



# Fleet Command

## Code Institute Python command line interface application

Am I responsive thing goes here

# Table of Contents

# Background

When choosing video games to play, I find that I gravitate toward strategic wargames - titles like Command & Conquer, Homeworld, Panzer Corps, Wargame: Red Dragon, Distant Star: Revenant Fleet, Total War series, Hearts of Iron, XCOM and Company of Heroes. The one thing that ties these games together is that the developers have implemented various mechanics that mean that a player must consider the strategic layer when making decisions - things like supply lines, numbers of tanks and soldiers, resources, the movement of battlegroups and so on. This adds depth to a game that goes beyond tactical decisions - what targets to shoot, where tanks move and so on. 

Likewise, I enjoy military science fiction where the authors consider those same strategic issues in their plots - one of my favourites is a series called The Lost Fleet. The author is a former naval officer, and is as such well versed in such strategic issues. 

This project is a text-based tactical decisions game run in the terminal, with some strategic elements planned. The player takes the role of an admiral who has been placed in command of a fleet of naval spaceships. The player's objective is to take these ships and defend the Alliance against a large Syndicate Worlds attack across multiple fronts. If the player is successful enough, and has enough ships remaining in their fleet, they may be able to launch a counter-attack to take advantage of the enemy's losses. 

# Scope

The scope of this project is to create a text-based game that is run in the terminal. Players will be given information via the terminal and then presented with choices. They are then prompted to respond to these choices via key-presses. These decisions are then handled buy the code and the results displayed the user. 

# Audience

The intended audience is fans of military science fiction and fans of tactical choice-based games. 

# User Stories

Users must be able to understand the situation presented by game - strong inductory print statements

Users must be well-informed by the text content of the game - plenty of print statements with good informational text

Users must be able to respond to prompting from the game by key-presses - input statements

Users must be able to make informed tactical choices in the game - each decision point must have at least several ways of responding to it, each sufficiently different  

Users must be able to meaningfully influence the outcome of the game - users must be able to lose and win based on their decisions, making poor decisions loses the game, making good decisions wins the game





# Features

# Function 

# Development choices

Justify in-repo approach, no spreadsheet

Early on in development, I realised that the project was probably being too ambitious in scope, so I reduced the classes of ships from 5 (battleships, battlecruisers, heavy cruisers, light cruisers and destroyers) down to 3 (battleships, cruisers, escorts)
I also removed references to marines, crew, missiles and mines, instead focusing on getting the core mechanics of the game working, with a view to implementing these later if time permitted. The dictionaries containing marines, crew, mines and missiles were moved to a separate file for reference

in the fight_engagement function, math.ceil was used so that enemy ship total were consistently rounded up rather than down, as I foresaw endless rounding down causing battles to go on for far longer than they needed to. The actual difference in firepower is minimal


# Future Work

# Bugs

# Technologies

Github

Gitpod

Slack

Heroku

Black

# Deployment

# Testing

# Credits

The Lost Fleet series by Jack Campbell