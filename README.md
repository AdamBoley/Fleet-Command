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

I enjoy military science fiction books. In particular, I tend to select books where the authors consider the realities of war in their plots, paying heed to such things as tactics, strategy and logistics. Perhaps one of my most favourite series are the Lost Fleet books, authored by retired US Navy officer John Hemry, writing under the pen name Jack Campbell. As a former naval officer, Campbell is able to give a more realistic depiction than most other authors of how a military force considers tactics, strategy and logistics in operations.

The basic plot of the Lost Fleet books involves a 100-year long war between two large interstellar human civilisations - the Alliance, and the Syndicate Worlds. This war is fought primarily using large fleets of space-craft. Since both combatant factions are roughly equally matched in population and industrial output, neither can gain a decisive advantage over the other, leading to the war dragging on for a century. Predictably, casualties on both sides have been huge, and this has led to a problem - officers are often poorly trained, having been rushed through training in order to replace losses. This has in turn led to the militaries of both side being rather poorly led, with both sides often resorting to simplistic tactics that lead to bloodbaths, the officers of both sides not skilled or experienced enough to use more advanced tactics. Into this mess of a war comes the series' protagonist, Captain John Geary, a highly skilled pre-war officer placed in cryogenic stasis in an escape pod when his ship was destroyed in the first battle of the war. Geary assumes command of an Alliance fleet and, using his pre-war skills and knowledge of advanced tactics, inflicts crushing defeats on the Syndicate Worlds, eventually winning the war. 

The series as a whole contains detailed battle sequences that a reader can easily picture in their head. Beyond this, Campbell takes pains to consider the strategic and logistical implications of Geary's actions - food, fuel and ammunition levels are mentioned at length, and these have an effect on Geary's decisions - sometimes Geary is forced to use an unorthodox or risky approach simply because his fuel and ammunitions reserves are too low, or his ships are too damaged to do otherwise. 

This project is a homage of sorts to the Lost Fleet series. The project therefore is a text-based tactical decisions game run in the terminal, with some strategic elements planned. The player takes the role of an admiral who has been placed in command of a fleet of naval spaceships. The player's objective is to take these ships and defend the Alliance against a large Syndicate Worlds attack across multiple fronts. If the player is successful enough, and has enough ships remaining in their fleet, they may be able to launch a counter-attack to take advantage of the enemy's losses. 

# Scope

The scope of this project is to create a text-based game that is run in the terminal. Players will be given information via the terminal and then presented with choices about how to proceed. They are then prompted to respond to these choices via key-presses. These decisions are then handled buy the code and the results displayed the user. 

# Audience

The intended audience is fans of military science fiction and fans of tactical choice-based games. 

# User Stories

Users must be able to understand the situation presented by game - strong inductory print statements

Users must be well-informed by the text content of the game - plenty of print statements with good informational text

Users must be able to respond to prompting from the game by key-presses - input statements

Users must be able to make informed tactical choices in the game - each decision point must have at least several ways of responding to it, each sufficiently different  

Users must be able to meaningfully influence the outcome of the game - users must be able to lose and win based on their decisions, making poor decisions loses the game, making good decisions wins the game





# Features

The Fleet Command game consists of a number of missions that the player must navigate.

# Function 

Each mission is handled with its own function. The first function, new_game, is the first function that is called. Here, the player is given some introductory information that is delivered using print statements and f-strings. As each mission presents the player with a group of enemy ships that must be overcome, a dictionary defining this group is the first task executed by each mission function. 

Each mission function then calls the enemy_firepower_calculator function, which is passed the dictionary containing the numbers of enemy ships. The enemy_firepower_calculator calculates the starting firepower of the enemy group and returns it to a variable called enemy_firepower. The value of the enemy_firepower variable and the dictionary containing the enemy group strength are then printed to the terminal along with some mission-specific story-telling text. This gives the user some content within which to make their decisions. 

Each mission function then contains an input and a related IF / ELSE statement that asks if they want to engage the enemy group. If the player chooses not to engage, the mission ends and the next mission function is called.

However, if the player chooses to engage, the fight_battle function is called. This is the core mechanic of the game, and is what allows the game to simulate space combat. 

The fight_battle function contains the fight_engagement function, which is where the user actually makes tactical decisions. Firstly, the user is prompted to enter a number between 1 and 5 to select the tactic they want to use, which determines the number of enemy ships the player's fleet will face. The difference in firepower rating between the player's ships and the number of enemy ships that the player has chosen to engage is then calculated.  

Two variables are then calculated - firepower_factor and losses_factor. Firepower_factor is calculated by dividing effective_firepower_difference by player_firepower, and is intended to model the combat power of the player's fleet. Losses_factor is calculated by dividing the effective_enemy_firepower by the effective_firepower_difference, and then furthering dividing by a number that depends on the tactic selected. 

If the player selected tactic 5, a missile barrage, the firepower_factor variable is instead calculated by dividing the value of the missiles_fired variable by the value of the effective_enemy_firepower variable, which is intended to model the weapons of ships in the enemy group being used as point defence to shoot down the player's missiles. The more missiles the player is able to fire, or the smaller the number of ships the missiles are being used against, the better the saturation - more missiles are able to get through the point defences, and hence more enemy ships are destroyed. 

Two functions are then called - update_enemy and update_player. The update_enemy function updates the enemy_group_strength dictionary and the global enemy_losses dictionary, and then returns the updated enemy_group_strength dictionary. The update_player function updates the global player_ships and global player_losses dictionaries, and then returns the updated player_ships dictionary. If tactic 5 was selected, the losses factor is set to 0, since the enemy is out of range and hence unable to return fire. Hence, when the update_player function is called, no player ships will be lost. 

The outcome of the engagement is then printed to the terminal, with the player's ships and the enemy's ships displayed. The fight_battle function then checks to see if the current enemy group has any ships remaining. If so, the player is offered choice to either re-engage the enemy or disengage. If the disengage choice is selected, the enemy ships that have been ignored are added to the global enemy_bypassed dictionary, the mission function ends, and the next mission begins. 

If the re-engage choice is selected, the fight_engagement function is called again, and is passed the updated values of the player_ships and enemy_group_strength dictionaries. This looping set-up effectively allows the game to continuously offer the player the choice of re-engaging without additional functions. Once all values in the enemy_group_strength dictionary have been reduced to 0 (i.e, all enemy ships destroyed), the fight_battle function ends and then the mission ends, and the next mission is started. 

The fight_battle function also reduces the player's supply count by 1, and checks to see if the player has supplies remaining. If the player runs out of supplies, the game ends. The fight_battle function also checks whether the player has run out of ships, and if so, the game ends.


# Development choices

When I first had the idea for this project, I planned to use a Google Sheets spreadsheet and the gspread Python library, as is used in the Love Sandwiches walkthrough project. The idea was to store the numbers of player and enemy ships, ammunition levels, supply levels and other such data in multiple worksheets which would be accessed using the methods of the gspread library. However, I considered that, should I want to distribute the project to other uses, such as to friends or via LinkedIn, this could become problematic, as multiple users might be pulling data from and sending data to the same spreadsheet at the same time, potentially breaking their games. 

As a result, I decided to store all data used in the game (ship numbers, firepower ratings, etc) in the run.py file itself. When creating this data, I decided to use Python dictionaries to hold related data - the numbers of player ships are held in a dictionary, ship firepower ratings are held in another, and the numbers of ships in enemy groups are held in their own dictionaries. This decision was made for two reasons. First, dictionaries allow the data to be grouped sematically in the code, which increases readability. Secondly, storing each data point as a simple variable seemed too easy, and I used simple variables extensively in my JavaScript Project. I wanted to use this project to practice my ability to use and interact with Python data structures. Using dictionaries also allowed me to use For Loops to quickly print out the key - value pairs of dictionaries to update the user with battle results. I was particularly keen to use For Loops as I have, until now, never been particularly comfortable using them, and I did not use them in the JavaScript project, which was noted in the project feedback received on 27/4/22.  

Early on in development, I realised that the project was probably being too ambitious in scope, so I reduced the classes of ships from 5 (battleships, battlecruisers, heavy cruisers, light cruisers and destroyers) down to 3 (battleships, cruisers, escorts)
I also removed references to marines, crew, missiles and mines, instead focusing on getting the core mechanics of the game working, with a view to implementing these later if time permitted. The dictionaries containing marines, crew, mines and missiles were moved to a separate file for reference. 

In the update_enemy function, the math.ceil method was used so that enemy ship losses were consistently rounded up rather than down, as I foresaw endless rounding down causing battles to go on for far longer than they needed to, potentially driving a user to boredom. The actual difference in firepower is minimal. 

The decision to use 2 functions to update the enemy_group_strength, enemy_losses, player_ships and player_losses dictionaries was taken when I realised that the fight_engagement function had become very large, with much repetition. 

The decision to refactor the fight_engagement function so that the firepower_factor and losses_factor variables were calculated dynamically rather than being static depending on tactic and the value of the effective_firepower_difference variable was taken when I realised that adding IF / ELIF statements to capture a sufficient number of situations would make the function very large and difficult to tweak. The dynamic calculation solution is both smaller and far more elegant, with only the bare minimum of repetition. The dynamic calculation approach also models an engagement more realistically - when one side possesses overwhelming strength in numbers or firepower, it suffers very few casualties because enemy firepower is spread out over a large number of targets. When numbers are more even, the player suffers more casualties, which is an incentive to the player to whittle down the enemy numbers before 'going in for the kill', so to speak. 


# Future Work

armour rating

random number generator 

# Bugs

Early on in development, as I was focused on getting the core mechanics of the game working, I left out data validation when constructing the IF / ELSE conditional statements. During testing, this led to failures when I accidentally pressed the wrong keys. 

Commit #23 added functionality to the update_player_ships to check if the calculations had returned negative, and if so, to correct these to 0, since you cannot have a negative number of ships. If the player ran out of ships, i.e. they were all destroyed in a loop of the fight_engagement function, an IF statment added at the end of the fight_engagement function displayed a series of messages saying that the player had failed, and offered to restart the game. This actual caused a failure, since the new_game function was called, which required a player_name argument to be passed in. Since the player_name variable was not present in the fight_engagement function, the code failed. I decided to commit anyway, so as to dedicate the next commit to fixing the problem and hence adhere to best practices to keep commits atomic. Hence, the code contained in commit #23 will not work. Commit #24 fixed the bug by reworking the main and new_game functions. 

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

My Mentor Ronan McLelland

FD Bartholomew Boley - for his useful contributions to the development process