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

This project is a homage of sorts to the Lost Fleet series. The project therefore is a text-based tactical decisions game run in the terminal, with some strategic elements planned. The player takes the role of an admiral who has been placed in command of a fleet of naval spaceships. The player's objective is to take these ships and defend the Alliance against a large Syndicate Worlds attack across multiple fronts. If the player is successful enough, and meets the victory criteria, they may be able to launch a counter-attack to take advantage of the enemy's losses.

# Scope

The scope of this project is to create a text-based game that is run in the terminal. Players will be given information via the terminal and then presented with choices about how to proceed. They are then prompted to respond to these choices via key-presses. These decisions are then handled buy the code and the results displayed the user. 

# Audience

The intended audience is fans of military science fiction and fans of tactical choice-based games. 

# User Stories

Users must be able to understand the situation presented by game - strong inductory print statements

Users must be well-informed by the text content of the game - plenty of print statements with good informational text

Users must be able to respond to prompting from the game by key-presses - input statements

Responses to input prompts must handle incorrect / invalid inputs gracefully - While loops and Try / Except statements

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

If the player selected tactic 6, a mine field, the firepower_factor variable is instead calculated by dividing the number of mines the player can lay by the number of ships in the enemy group, and then dividing this by 2. This models the mines not being able to destroy more ships than there are mines, and a reasonable assertion on my part that two mines are needed to destroy a ship. 

Two functions are then called - update_enemy and update_player. The update_enemy function updates the enemy_group_strength dictionary and the global enemy_losses dictionary, and then returns the updated enemy_group_strength dictionary. The update_player function updates the global player_ships and global player_losses dictionaries, and then returns the updated player_ships dictionary. If either tactic 5 or 6 was selected, the losses factor is set to 0, since the enemy is out of range and hence unable to return fire. Hence, when the update_player function is called, no player ships will be lost. 

The outcome of the engagement is then printed to the terminal, with the player's ships and the enemy's ships displayed. The fight_battle function then checks to see if the current enemy group has any ships remaining. If so, the player is offered choice to either re-engage the enemy or disengage. If the disengage choice is selected, the enemy ships that have been ignored are added to the global enemy_bypassed dictionary, the mission function ends, and the next mission begins. 

If the re-engage choice is selected, the fight_engagement function is called again, and is passed the updated values of the player_ships and enemy_group_strength dictionaries. This looping set-up effectively allows the game to continuously offer the player the choice of re-engaging without additional functions. Once all values in the enemy_group_strength dictionary have been reduced to 0 (i.e, all enemy ships destroyed), the fight_battle function ends. The player is then informed that some enemy ships may be salvageable, and is offered the choice of whether to conduct boarding actions to capture these enemy ships. 

If the player decides to do so, the boarding_operation function is called. First, the function checks to see whether there are any enemy ships left to board, though the first time this function is called, this check will always pass, since the boarding_operation function can only be called if there are enemy ships to board. This check only exists to break out of the loop once the player has run out of ships to board. 

If there are ships to board, the function uses two for loops to print the number of ships that can be boarded, and the choice of what ship to board. The player is then prompted to enter a number to select what ship they want to board. This triggers an if / elif statement. The appropriate statement will then check to see if there are any enemy ships of that class to board and if the player has enough marines to make the attempt. If either of these fail, the function ends. If the checks pass, the else statement will remove a ship from the boardable_ships dictionary and add it to the player_ships dictionary. The value of the marines variable will be reduced, to model the casualties the player's marines suffer in that boarding action, and the value of the player's supplies variable will also be reduced, to model the fuel, ammunition and repair supplies needed to get the ship back into a useable condition. In addition, the appropriate value of the minimum_crew dictionary will be subtracted from the value of the excess_crew variable to reflect the sailors that have been transferred from the player's ships to the captured ships in order to crew them. The boarding_operation function will then be called again, which is where the first conditional check may trigger. Once there are either no more ships left to board, no more marines or no more crew available, the mission ends, and the next mission is started. 

The fight_battle function also reduces the player's supply count by 1, and checks to see if the player has supplies remaining. If the player runs out of supplies, the game ends. The fight_battle function also checks whether the player has run out of ships, and if so, the game ends.


# Development choices

When I first had the idea for this project, I planned to use a Google Sheets spreadsheet and the gspread Python library, as is used in the Love Sandwiches walkthrough project. The idea was to store the numbers of player and enemy ships, ammunition levels, supply levels and other such data in multiple worksheets which would be accessed using the methods of the gspread library. However, I considered that, should I want to distribute the project to other uses, such as to friends or via LinkedIn, this could become problematic, as multiple users might be pulling data from and sending data to the same spreadsheet at the same time, potentially breaking their games. 

As a result, I decided to store all data used in the game (ship numbers, firepower ratings, etc) in the run.py file itself. When creating this data, I decided to use Python dictionaries to hold related data - the numbers of player ships are held in a dictionary, ship firepower ratings are held in another, and the numbers of ships in enemy groups are held in their own dictionaries. This decision was made for two reasons. First, dictionaries allow the data to be grouped sematically in the code, which increases readability. Secondly, storing each data point as a simple variable seemed too easy, and I used simple variables extensively in my JavaScript Project. I wanted to use this project to practice my ability to use and interact with Python data structures. Using dictionaries also allowed me to use For Loops to quickly print out the key - value pairs of dictionaries to update the user with battle results. I was particularly keen to use For Loops as I have, until now, never been particularly comfortable using them, and I did not use them in the JavaScript project, which was noted in the project feedback received on 27/4/22.  

Early on in development, I realised that the project was probably being too ambitious in scope, so I reduced the classes of ships from 5 (battleships, battlecruisers, heavy cruisers, light cruisers and destroyers) down to 3 (battleships, cruisers, escorts)
I also removed references to marines, crew, missiles and mines, instead focusing on getting the core mechanics of the game working, with a view to implementing these later if time permitted. The dictionaries containing marines, crew, mines and missiles were moved to a separate file for reference. 

In the update_enemy function, the math.ceil method was used so that enemy ship losses were consistently rounded up rather than down, as I foresaw endless rounding down causing battles to go on for far longer than they needed to, potentially driving a user to boredom. The actual difference in firepower is minimal. 

The decision to use 2 functions to update the enemy_group_strength, enemy_losses, player_ships and player_losses dictionaries was taken when I realised that the fight_engagement function had become very large, with much repetition. 

The decision to refactor the fight_engagement function so that the firepower_factor and losses_factor variables were calculated dynamically rather than being static depending on tactic and the value of the effective_firepower_difference variable was taken when I realised that adding IF / ELIF statements to capture a sufficient number of situations would make the function very large and difficult to tweak. The dynamic calculation solution is both smaller and far more elegant, with only the bare minimum of repetition. The dynamic calculation approach also models an engagement more realistically - when one side possesses overwhelming strength in numbers or firepower, it suffers very few casualties because enemy firepower is spread out over a large number of targets. When numbers are more even, the player suffers more casualties, which is an incentive to the player to whittle down the enemy numbers before 'going in for the kill', so to speak. 

When implementing the concept of experience through the player_experience variable and modification of the update_enemy function, I initially considered two methods of adding experience. The first method mimicked the method employed in many modern Role Playing Games such as the Fallout series, where each action, no matter how small, gives experience - picking a lock gains might give 10XP, whereas persuading a merchant to lower their prices might give 50XP. In Fleet Command, this method would add 0.01 to the player_experience variable each time the player decided to conduct a firing run, i.e. each time the fight_engagement was called. This would give the player's crews a small amount of experience each time they clashed with the enemy. The second method mimicked the method used in table-top roleplay games and wargames such as Dungeons & Dragons, where each player is awarded a set amount of experience points when a quest is completed, no matter what actions each player did. In Fleet Command, this method would add a flat value of 0.1 to the player_experience variable each time they decide to fight an enemy group via the fight_battle function, no matter how many times they engage via the fight_engagement function. Put simply - if the player fights, they gain experience. 

Ultimately, I went with the second method, as the first method would create an incentive for the player to always engage with option 1 - the safest approach. This would quickly bore a player. I also considered that any kind of experience in any field is often not gained in the heat of the moment, but only after a period of analysis and reflection, when new procedures, processes, doctrines and so on can be developed and implemented. 

I implemented the concept of experience as a way of balancing out the player's losses - when they fight, losses are pretty much inevitable due to the calculations, but the experience gained by the player's crews counters this. 

I decided to implement the boarding mechanic as another way of balancing out the player's losses, and to add flavour and additional choices to the game for the player to consider. I added the option to board all enemy ships at once when I noted that after the battle in the second mission, the calculations returned 16 enemy ships that could be boarded, which would be a boring slog for the player to board one after another. I added the option to abandon the boarding operation when I noted that a player might like to focus on adding certain ships to their fleet. 

When working on commit #60, which overhauled the update_player function so that Marines are lost when the player's cruisers and battleships are damaged or destroyed, I chose for:
A battleship to lose 20% of its 40 Marines when destroyed
A battleship to lose 10% of its 40 Marines when damaged
A cruiser to lose 30% of its 20 Marines when destroyed
A cruiser to lose 20% of its 20 Marines when damaged

I chose these values because Marines in the Lost Fleet setting wear vacuum rated combat armour that offers excellent personal protection. I considered that some of a capital ships' Marines would be lost, but that a considerable majority would survive and be rescued thanks to their armour. 

Towards the end of the project's development, I decided to tackle the numerous formatting errors that had cropped up. Since the project contains many long strings of text that help inform the player, reformatting was challenging. 

For function calls with several arguments, I placed all of the arguments onto indented new lines

For inputs assigned to variables, I used the backslash character to place the continuation text onto new lines

For strings, I tried several methods, such as string concatenation, but I ran into under-indentation and over-indentation errors. I found that indenting one tab and 2 spaces or 6 spaces solved this, but then noted that mixing spaces and tabs is not allowed in Python. This also produced very messy code. I eventually resorted to shortening my print statements so that none went over 79 characters. Whilst initially annoying, after a while I determined that I had probably been too verbose with my text. Reducing line lengths forced me to be clearer and more concise

# Future Work

armour rating

random number generator 

# Bugs

Early on in development, as I was focused on getting the core mechanics of the game working, I left out data validation when constructing the IF / ELSE conditional statements. During testing, this led to failures when I accidentally pressed the wrong keys. Once the major development work had been completed, with the mission functions written and the combat calculations properly implemented, I went back over the project implementing input validation using while loops with break statements, and try / except statements.  

Commit #23 added functionality to the update_player_ships to check if the calculations had returned negative values, and if so, to correct these to 0, since you cannot have a negative number of ships. If the player ran out of ships, i.e. they were all destroyed in a loop of the fight_engagement function, an IF statment added at the end of the fight_engagement function displayed a series of messages saying that the player had failed, and offered to restart the game. This actually caused a failure, since the new_game function was called, which required a player_name argument to be passed in. Since the player_name variable was not present in the fight_engagement function, the code failed. I decided to commit anyway, so as to dedicate the next commit to fixing the problem and hence adhere to best practices to keep commits atomic. Hence, the code contained in commit #23 will not work. Commit #24 fixed the bug by reworking the main and new_game functions. 

Commit #34 added the boarding mechanic, which allows players to board enemy ships after a battle has been won and add them to their fleet. Testing this mechanic with the first mission revealed that, whilst the player_ships dictionary updates properly, the player_firepower variable does not, since the value of player_firepower is calculated when the program runs for the first time, and is not updated. Further testing revealed that the value of player_firepower stays constant even when the player loses ships as a result of the fight_engagement / update_player loop. Commit #35 fixed this problem by using a new function called calculate_player_firepower to calculate the value of player_firepower dynamically. This function is called in the player_fleet_status function and at the start of the fight_engagement function.

Commit #39 broke the code due to insufficient testing. I removed the globl total_crew and excess_crew dictionaries without modifying the code in the calculate_total_crew and calculate_excess_crew functions. Commit #40 fixed this by adding those dictionaries back in, as well as adding the consideration of crew to the boarding mechanic. 

During some routine testing related to commit #44, I noted that when the battle in mission two was fought, it was possible for the enemy group to possess a negative number of enemy ships. I suspect that this is related to the player_experience modifier that increases the damage done by the player's ships in the update_enemy function. Commit #44 was dedicated to overhauling the boarding_operation function, so this bug was merely documented for later fixing. Commit #45 fixed this bug by appropriating the code used in the update_player function to solve a similar bug whereby the player could end up with a negative number of ships. This solution checks to see if the number of enemy ships of a specific class is less than 0, and if so, sets the number to 0. 

During testing related to commit #46, it was noted that when the game is failed and the option to start a new game is selected, the global dictionaries do not reset. Commit #46 was focussed on reworking the way in which the player's losses are calculated by adding the concept of damaged ships that will be repaired behind the lines and eventually returned to the player's fleet. This issue of dictionaries resetting is documented here, and will be dealt with in a future commit. 

During testing related to commit #49, which implemented the new_game_reset function, I was deliberately trying to lose the game in order to test that the new function was working as intended. To lose, I choose option 4 - the riskiest and most casualty heavy approach. I noted that the when the enemy ships outnumbered the player's ships, the firepower_factor variable was negative. This produced negative enemy loss values and negative player loss values, which had the effect of __adding__ ships to the enemy and player fleets. This will require some reworking of the calculations.  

Testing various solutions to this problem also revealed another bug - the calculation results for selecting tactic 4 when facing enemy_group_two in Mission Two were unexpectedly bad for the player. The player's firepower_factor was calculated as 0.34 or thereabouts, whereas the losses_factor was calculated as 0.56 or thereabouts, despite the player having more ships than the enemy, which would lead to a reasonable expectation of destroying more ships than they lose. The cause of this was the losses_factor calculation, and the result was a consequence of the value of the effective_enemy_firepower (1040) being greater than the value of effective_firepower_difference (610). 

The solution to this calculation problem was found in Lanchester's Square Law, which is a concept that helps mathematically model a battle in which one side possesses more 'combat power' than the other, either through superior numbers, technology, training, etc. Combat power is essentially a measure of how much damage both combatants can dish out in a given time. It shows that when one combatant possesses superior combat power, the result is lopsided, with the superior combatant suffering far fewer casualties than might be expected. With this approach, the values of player_firepower and effective_enemy_firepower are squared and then square root of the difference between them is calculated. This solved the problem of the results of tactic 4 being bad for the player. 

Whilst useful, the application of Lanchester's Square Law did not solve the problem encountered when the player is facing an effective enemy strength that is greater than their own fleet strength, and in fact made it worse. Where before the calculations would technically work, even though they produced strange results, the calculations with the Square Law gave ValueErrors, since the square root function was being performed on negative numbers.

This problem was solved by reworking the fight_engagement function so that the firepower_factor and losses_factor are calculated differently if the player is outnumbered during a firing run (i.e. they choose to engage superior enemy numbers). If the enemy outnumbers the player in a firing run, the calculations are effectively switched around - the firepower_factor is calculated using the original losses_factor equation and the losses_factor is calculated using the original firepower_factor calculation. This gives the enemy an advantage, and so they will destroy more of the player's ships and lose fewer of their ships. 

During some routine testing, it was noted that the player_fleet_status function works properly, but can give misleading information when called. I noticed that when viewing the fleet status before beginning mission 2 after losing 1 cruiser and 5 escorts in mission 1 and also boarding 2 escorts and 1 cruiser that the function displayed that the fleet had 20 battleships, 50 cruisers and 147 escorts, but was also displaying that 1 cruiser and 3 escorts had been destroyed and that 2 escorts had been damaged. This could cause players to lose confidence in the game and to think that the game was not properly tracking their fleet status. 

I attempted to solve this by creating a salvaged_ships dictionary, which is updated in the boarding_operation function, and which tracks how many ships the player has salvaged and added to their fleet, and then using a loop to display the values of this dictionary in the player_fleet_status function. However, testing this solution revealed that option 5 - the option to board all enemy ships at once - was not working properly, as it was not properly updating the dictionaries. 
Further inspection of the code in the boarding_operation function revealed the answer as to why - when updating the escort key in the boarded_ships and salvaged_ships dictionaries, I had accidentally set the number of escorts to be increased by the number of cruisers.  

It was also noted that the number of the player's marines does not update based on how many ships they have lost - as ships are destroyed or damaged, the player would expect their marine strength to go down. This was fixed with some additional code in the update_player function that subtracts marines if any of the player's battleships or cruisers are destroyed. 

It was also noted that the enemy_battle_losses dictionary that is printed at the end of a battle now no longer contains the correct values. I initially put this down to the effect of the new approach to the calculation of the firepower_factor variable from the application of Lanchester's Square Law, but this was not the case. 

Investigation of this bug revealed that the source was the modifier applied to the three update_enemy calculations by the player_experience variable. This was determined when the game was played twice. The first time, I skipped the first mission, thereby not increasing the player_experience variable, and hence effectively not applying the modifier in the calculations for the second mission. In the second mission, the calculations produced results that were expected - I could not destroy more ships than I engaged. The second time, I played the first mission, thereby increasing the player_experience variable and applying a +10% modifier to the update_enemy calculations. With this modifier, I was able to destroy more ships than I engaged, confirming the existence of the bug. 
The player_experience modifier was effectively increasing the value of the firepower_factor variable, in some cases taking it above 1. Since the firepower_factor is used in the calculations directly, if it rises above a value of 1, then more enemy ships can be destroyed than exist. 

To solve this bug, I initially considered moving the application of player_experience from the update_enemy function to the fight_engagement function, using it to modify the value of firepower_factor there before passing firepower_factor to update_enemy
However, since there are 6 tactics and three calculations for determining the value of firepower_factor in each (depending on the values of player and enemy combat power) this would require at least 6 and possibly 18 additions to modify the value of firepower_factor. This seemed excessive and a violation of DRY principles. 

I then realised that I had dealt with a similar issue before, when writing the calculations for tactics 5 and 6, the missile barrage and mine-field tactics. In those cases, when firing many missiles or laying many mines from many ships against a small number of enemy ships, it was sometimes possible for the firepower_factor calculated there to be greater than 1. In those cases, I thought of this as being unrealistic, and the equivalent to destroying more ships than you have missiles or mines. Hence, I applied a small conditional check that checks to see if the value of firepower_factor is greater than 1, and if so, correct firepower_factor to 1. This is similar to the conditional checks in update_enemy and update_player, which check to see if the player_ships and enemy_group_strength dictionaries have negative numbers of ships, and if so, correct these to 0. 

Hence, I decided to create a new variable in update_enemy called damage_factor, which multiplies the passed value of firepower_factor and player_experience together. A conditional check checks to see if the value of damage_factor is greater than 1 and if so, corrects it to 1. The damage_factor is then used in the calculations where firepower_factor and player_experience were. This solution worked and had the desired effect of not being able to destroy more enemy ships than are present. 

As the project was nearing completion, testing of the many user input decisions was undertaken. Several bugs were noted, mostly input statements requiring input validation and needing new line commands. These were noted but not fixed during the commit that added the testing and results. 


# Technologies

Github

Gitpod

Slack

Heroku

Black

# Deployment

As the project was nearing completion, Heroku and Github suffered security breaches, forcing Heroku to suspend the feature that allows direct linkage to a Github repository for deployment. 

# Testing

As Fleet Command is a tactical choice-based game that relies heavily on user input, it must be thoroughly tested to ensure that there are no errors that could cause a crash. 

The game must also be balanced, to ensure that a player can both win and lose the game based on their choices. The player cannot just stick to one option when fighting battles. Players who pick tactics 3 or 4 (the riskiest, most casualty-heavy, but quickest approaches) must run out of ships quickly. Players who rely on tactics 1 and 2 (the safer, slower approaches) must run out of supplies. 

## Function testing

This section covers the testing of the basic functionality of the game. Does it work as intended? Does it respond to player inputs? How does it handle incorrect / invalid inputs?

I have chosen to hold the result of this testing in a markdown table. Column 1 is the mission or feature in which the choice takes place. Column 2 is the choice itself. Column 3 is the response to the choice. Column 4 is the outcome. 

Main and new game functions
Choice                 | Response                      | Expected Outcome                               | Actual Outcome                                 |
-----------------------| ----------------------------- | ---------------------------------------------- | -----------------------------------------------|
Start new game         | Yes - key press y             | Start new game - enter username prompt         | Start new game - enter username prompt         |
Start new game         | No - key press n              | Loop back through main function                | Loop back through main function                |
Start new game         | Invalid - key press != y or n | Restate input prompt                           | Restate input prompt                           |
Enter player name      | Enter 'Adam'                  | Prints 'Good Morning Admiral Adam'             | Prints 'Good Morning Admiral Adam'             |
Enter flagship name    | Enter 'Dragon'                | Prints 'Welcome aboard the Battleship 'Dragon' | Prints 'Welcome aboard the Battleship 'Dragon' |
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew  | View player ships, marines, supplies and crew  |
See fleet status       | No - key press n              | Prompt fleet capabilities decision             | Prompt fleet capabilities decision             |
See fleet status       | Invalid - key press != y or n | Restate input prompt                           | Restate input prompt                           |
See fleet capabilities | Yes - key press y             | View capabilities of player ships              | View capabilities of player ships              |
See fleet capabilities | No - key press n              | Prompt tactics decision                        | Prompt tactics decision                        |
See fleet capabilities | Invalid - key press != y or n | Restate input prompt                           | Restate input prompt                           |
See tactics            | Yes - key press y             | See tactics player can employ in battle        | See tactics player can employ in battle        |
See tactics            | No - key press n              | Begin mission 1, stop at engage decision       | Begin mission 1, stop at engage decision       |
See tactics            | Invalid - key press != y or n | Restate input prompt                           | Restate input prompt                           |

M1
Choice                 | Response                      | Expected Outcome                                       | Actual Outcome                                         |
-----------------------| ----------------------------- | ------------------------------------------------------ | -------------------------------------------------------|
Engage / disengage     | Engage - key press y          | Launch fight_battle function, stop at tactic selection | Launch fight_battle function, stop at tactic selection |
Engage / disengage     | Disengage - key press n       | Launch mission 2, stop at fleet status decision        | Launch mission 2, stop at fleet status decision        |
Engage / disengage     | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |

M2
Choice                 | Response                      | Expected Outcome                                       | Actual Outcome                                               |
-----------------------| ----------------------------- | ------------------------------------------------------ | -------------------------------------------------------------|
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew          | View player ships, marines, supplies and crew                |
See fleet status       | No - key press n              | Proceed to mission narrative, stop at engage decision  | Proceed to mission narrative, stop at engage decision        |
See fleet status       | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                         |
Engage / disengage     | Engage - key press y          | Launch fight_battle function, stop at tactic selection | Launch fight_battle function, stop at tactic selection       |
Engage / disengage     | Disengage - key press n       | Launch mission 3, stop at fleet status decision        | Launch mission three, stop at fleet status decision          |
Engage / disengage     | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                         |



M3
Choice                 | Response                      | Expected Outcome                                                        | Actual Outcome                                                           |
-----------------------| ----------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------|
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew                           | View player ships, marines, supplies and crew                            |
See fleet status       | No - key press n              | Proceed to mission narrative, stop at decision on which group to engage | Proceed to mission narrative, stop at decision on which group to engage  |
See fleet status       | Invalid - key press != y or n | Restate input prompt                                                    | Restate input prompt                                                     |
Engage / disengage     | Engage - key press y          | Proceed to mission narrative, stop at decision on which group to engage | Proceed to mission narrative, stop at decision on which group to engage  |
Engage / disengage     | Disengage - key press n       | Launch mission four, stop at fleet status decision                      | Launch mission four, stop a fleet status decision                        | 
Engage / disengage     | Invalid - key press != y or n | Restate input prompt                                                    | Restate input prompt                                                     |
Which group to engage  | key press 1                   | Engage sub-group 1                                                      | Engage sub-group 1                                                       |
Which group to engage  | key press 2                   | Engage sub-group 2                                                      | Engage sub-group 2                                                       |
Which group to engage  | Invalid - key press != 1 or 2 | Restate input prompt                                                    | Restate input prompt                                                     |



M4
Choice                     | Response                      | Expected Outcome                                                       | Actual Outcome                                                         |
---------------------------| ----------------------------- | ---------------------------------------------------------------------- | -----------------------------------------------------------------------|
See fleet status           | Yes - key press y             | View player ships, marines, supplies and crew                          | View player ships, marines, supplies and crew                          |
See fleet status           | No - key press n              | Proceed to mission narrative, stop at engage decision                  | Proceed to mission narrative, stop at engage decision                  |
See fleet status           | Invalid - key press != y or n | Restate input prompt                                                   | Restate input prompt                                                   |
Engage / disengage         | Engage - key press y          | Launch fight_battle function, stop at tactic selection                 | Launch fight_battle function, stop at tactic selection                 |
Engage / disengage         | Disengage - key press n       | Launch mission five, stop at fleet status decision                     | Launch mission five, stop at fleet status decision                     |
Engage / disengage         | Invalid - key press != y or n | Restate input prompt                                                   | Restate input prompt                                                   |
Trade sailors for supplies | Yes - key press y             | Add supplies, remove crew - must be inspected at start of next mission | Add supplies, remove crew - must be inspected at start of next mission |
Trade sailors for supplies | No - key press n              | Move to next mission                                                   | Move to next mission                                                   |
Trade sailors for supplies | Invalid - key press != y or n | Restate input prompt                                                   | Restate input prompt                                                   |

M5
Choice                 | Response                      | Expected Outcome                                       | Actual Outcome                                         |
-----------------------| ----------------------------- | ------------------------------------------------------ | -------------------------------------------------------|
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew          | View player ships, marines, supplies and crew          |
See fleet status       | No - key press n              | Proceed to mission narrative, stop at join-up decision | Proceed to mission narrative, stop at join-up decision |
See fleet status       | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Join-up decision       | Yes - key press y             | Add ships to player fleet, reduce supplies             | Add ships to player fleet, reduce supplies             |
Join-up decision       | No - key press n              | No reinforcements, proceed to engage decision          | No reinforcements, proceed to engage decision          |
Join-up decision       | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Engage / disengage     | Engage - key press y          | Launch fight_battle function, stop at tactic selection | Launch fight_battle function, stop at tactic selection |
Engage / disengage     | Disengage - key press n       | Launch mission six, stop a fleet status decision       | Launch mission six, stop a fleet status decision       |
Engage / disengage     | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |


M6
Choice                  | Response                      | Expected Outcome                                       | Actual Outcome                                         |
------------------------| ----------------------------- | ------------------------------------------------------ | -------------------------------------------------------|
See fleet status        | Yes - key press y             | View player ships, marines, supplies and crew          | View player ships, marines, supplies and crew          |
See fleet status        | No - key press n              | Proceed to mission narrative, stop at engage decision  | Proceed to mission narrative, stop at engage decision  |
See fleet status        | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Engage / disengage      | Engage - key press y          | Launch fight_battle function, stop at tactic selection | Launch fight_battle function, stop at tactic selection |
Engage / disengage      | Disengage - key press n       | Launch mission 7, stop a fleet status decision         | Launch mission 7, stop a fleet status decision         | 
Engage / disengage      | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Counter-invade decision | Yes - key press y             | Counter-invade Laconia                                 | Counter-invade Laconia                                 |
Counter-invade decision | No - key press n              | Move to salvage damaged ships decision                 | Move to salvage damaged ships decision                 |
Counter-invade decision | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Salvage damaged ships   | Yes - key press y             | Salvage damaged ships, add to player fleet             | Salvage damaged ships, add to player fleet             |
Salvage damaged ships   | No - key press n              | Move to next mission                                   | Move to next mission                                   |
Salvage damaged ships   | Invalid - key press != y or n | Restate input prompt                                   | Restates input prompt                                  |


M7
Choice                 | Response                      | Expected Outcome                                         | Actual Outcome                                           |
-----------------------| ----------------------------- | -------------------------------------------------------- | ---------------------------------------------------------|
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew            | View player ships, marines, supplies and crew            |
See fleet status       | No - key press n              | Proceed to mission narrative, proceed to tactic decision | Proceed to mission narrative, proceed to tactic decision |
See fleet status       | Invalid - key press != y or n | Restate input prompt                                     | Restate input prompt                                     |
Launch counter attack  | Yes - key press y             | Launch mission 8                                         | Launch mission 8                                         |
Launch counter attack  | No - key press n              | Call campaign report and see data related to campaign    | 
Launch counter attack  | Invalid - key press != y or n | Restate input prompt                                     | Restate input prompt                                     |

M8
Choice                 | Response                      | Expected Outcome                                       | Actual Outcome                                         |
-----------------------| ----------------------------- | ------------------------------------------------------ | -------------------------------------------------------|
See fleet status       | Yes - key press y             | View player ships, marines, supplies and crew          | View player ships, marines, supplies and crew          |
See fleet status       | No - key press n              | Proceed to mission narrative, stop at engage decision  | Proceed to mission narrative, stop at engage decision  |
See fleet status       | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |
Engage / disengage     | Engage - key press y          | Launch fight_battle function, stop at tactic selection | Launch fight_battle function, stop at tactic selection |
Engage / disengage     | Disengage - key press n       | Call campaign report and see data related to campaign  | Call campaign report and see data related to campaign  |
Engage / disengage     | Invalid - key press != y or n | Restate input prompt                                   | Restate input prompt                                   |

Fighting battles in the fight_battle and fight_engagement functions
Choice                 | Response                               | Expected Outcome                                                    | Actual Outcome                                                      |
-----------------------| -------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------|
Select tactic          | Key press 1, 2, 3, or 4                | Prints information about the battle, stops at confirmation decision | Prints information about the battle, stops at confirmation decision |
Select tactic          | Key press 5 with missiles remaining    | Prints information about the battle, stops at confirmation decision | Prints information about the battle, stops at confirmation decision |
Select tactic          | Key press 5 with no missiles remaining | Prints that no missiles remain, prompts user to select a tactic     | Prints that no missiles remain, prompts user to select a tactic     |
Select tactic          | Key press 6 with mines remaining       | Prints information about the battle, stops at confirmation decision | Prints information about the battle, stops at confirmation decision |
Select tactic          | Key press 6 with no mines remaining    | Prints that no mines remain, prompts user to select a tactic        | Prints that no mines remain, prompts user to select a tactic        |
Select tactic          | Invalid - key press NaN or number > 6  | Return to tactic selection                                          | Return to tactic selection                                          |
Confirm tactic         | Yes - key press y                      | Carries out attack, prints results, stops at re-engage decision *   | Carries out attack, prints results, stops at re-engage decision *   |
Confirm tactic         | No - key press n                       | Return to tactic selection                                          | Return to tactic selection                                          |
Re-engage decision     | Yes - key press y                      | Calls fight_engagement function, stops at tactic selection          | Calls fight_engagement function, stops at tactic selection          |
Re-engage decision     | No - key press n                       | Move to next mission, stops at first decision                       | Move to next mission, stops at first decision                       |
Re-engage decision     | Invalid - key press != y or n          | Restates input prompt                                               | MOVES TO NEXT MISSION                                               |

*Only when the attack will leave enemy ships remaining. If no enemy ships remain, will prompt the user to decide whether to initiate a boarding operation. 

Boarding enemy ships in the boarding_operation function
Choice                      | Response                                                       | Expected Outcome                                     | Actual Outcome                                       |
----------------------------| -------------------------------------------------------------- | ---------------------------------------------------- | -----------------------------------------------------|
Initiate boarding operation | Yes - key press y                                              | Initiate boarding operation, stop at choice of ship  | Initiate boarding operation, stop at choice of ship  | 
Initiate boarding operation | No - key press n                                               | Move to next mission, or decision if applicable      | Move to next mission, or decision if applicable      |
Initiate boarding operation | Invalid - key press != y or n                                  | Restate input prompt                                 | Restate input prompt                                 |
Choose a ship to board      | key press 1 - Board a battleship with a battleship remaining   | Move battleship from available ships to player ships | Move battleship from available ships to player ships |
Choose a ship to board      | key press 2 - Board a cruiser with a cruiser remaining         | Move cruiser from available ships to player ships    | Move cruiser from available ships to player ships    |
Choose a ship to board      | key press 3 - Board an escort with an escort remaining         | Move escort from available ships to player ships     | Move escort from available ships to player ships     |
Choose a ship to board      | key press 1 - Board a battleship with no battleships remaining | Restate input prompt                                 | Restate input prompt                                 |
Choose a ship to board      | key press 2 - Board a cruiser with no cruisers remaining       | Restate input prompt                                 | Restate input prompt                                 |
Choose a ship to board      | key press 3 - Board an escort with no escorts remaining        | Restate input prompt                                 | Restate input prompt                                 |
Choose a ship to board      | key press 4 - stop boarding ships                              | Move to next mission                                 | Move to next mission                                 |
Choose a ship to board      | key press 5 - Board all remaining enemy ships                  | Move all available ships to player ships             | Move all available ships to player ships             | 
Choose a ship to board      | Any valid key press with insufficient Marines remaining        | Restate input prompt                                 | Restate input prompt                                 |
Choose a ship to board      | Any valid key press with insufficient supplies remaining       | Restate input prompt                                 |                                  |
Choose a ship to board      | Invalid key press - NaN or key press > 5                       | Restate input prompt                                 | Restate input prompt                                 |


New game decision


## Balance testing

This section covers testing of how easy or difficult it is to play, win and lose the game. A variety of scenarios were tested.<br>

Scenario - player avoids engaging enemy groups by pressing n when presented with engage decision. <br>
Outcome - Player is forced to engage in mission 7, as intended. Player is informed that they have lost the game when victory conditions are checked after the fight in mission 7. Player is then taken to campaign report function<br>

Scenario - player chooses to engage, but never follows through, breaking off with enemy ships still present<br>
Outcome - Player is informed that they have lost the game when victory conditions are checked after the fight in mission 7. Player is then taken to campaign report function<br>

Scenario - player only chooses to engage with tactic 1, the least risky, but slowest tactic. Player does not make use of the boarding mechanic. Player chooses not to take on additional supplies if given the choice. Player does not accept reinforcements if given the choice<br>
Outcome - Player destroys all enemy groups up to end of mission 7. Player has 19 supplies at end of mission 7. Player has good numbers of battleships and cruisers, but very low numbers of escorts. Player can actually make it through the bonus mission without running out of supplies. The game also takes a long time to complete, and it quite monotonous in the doing. <br>
Conclusion - Player starts with too many supplies. Also, the calculations are set up in such a way that every time the player conducts a firing run, they will lose at least 1 escort. This accounts for the high escort losses. However, the player's battleships and cruisers take few losses due to those calculations. This keeps the player's firepower rating quite high, allowing them to keep an advantage over the small effective enemy numbers. Hence, the player never needs to . <br>
Outcome after correction - 

Scenario - player only chooses to engage with tactic 2, a riskier, but faster tactic than tactic 1. Player does not make use of the boarding mechanic<br>
Outcome - This test proved very interesting. I got to mission 7 and took very heavy casualties as predicted, but then got reduced to 1 battleship and 1 cruiser. Repeated firing runs using tactic 2 continued to destroy small numbers of enemy ships, but failed to sustain more casualties. The test was eventually abandoned after several of these firing runs, as I could see that these last player ships would not be destroyed. <br>
Conclusion - Clearly the calculations underpinning the game require tweaking. The calculations that determine the losses of player cruisers and battleships use the math.floor method, which was used to represent the armour of cruisers and battleships allowing them to shrug off hits that destroy escorts. This may need to be converted to math.ceil, or additional condtional checks may need to be implemented that check to see if the player has a very low number of ships, and if so, have them all destroyed in the next firing run, since once the player has so few ships, the enemy can concentrate all of their fire on those few ships and destroy them easily.<br>
Outcome after correction - 

Scenario - player only choose to engage with tactic 3, a risker, but faster tactic than tactic 2. Player does not make use of the boarding mechanic<br>
Outcome - Again, this test proved interesting. Heavy casualties were sustained, but when I was reduced to 1 cruiser and 1 battleship, I was unable to lose these. Again, this test was abandoned<br>
Conclusion - Same as conclusion to tactic 2 testing
Outcome after correction -

Scenario - player only chooses to engage with tactic 4, the riskiest but fastest tactic. Player does not make use of the boarding mechanic<br>
Outcome - Same outcome as tests with tactics 2 and 3<br>
Conclusion - Same conclusion to tactic 2 and 3
Outcome after correction -

Scenario - player only chooses to engage with mines and missiles <br>
Outcome - Player runs out of mines and missiles after 6 firing runs<br>

Scenerio - player tries to win by using a variety of tactics to balance damage inflicted with supply consumption and ship losses, but does not attempt to board enemy ships<br>
Outcome - <br>

Scenario - player tries to win by using a variety of tactics to balance damage inflicted with supply consumption and ship losses, and makes use of the boarding mechanic<br>
Outcome - <br>
<br>

Overall conclusion - 


A handful of times, the battles didn't end when all enemy ships were destroyed. 

# Credits

The Lost Fleet series by Jack Campbell

https://www.freecodecamp.org/news/if-name-main-python-example/ - dunder name = dunder main
for demonstration of best practices
Allows run.py to be imported to other files

Lanchester's Square Law - for combat power calculations

My Mentor Ronan McLelland

FD Bartholomew Boley - for his useful contributions to the development process