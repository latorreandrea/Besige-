# BESIGE 

## Code Institute Portfolio 3 Project

![schermata iniziale](https://user-images.githubusercontent.com/80674568/129058183-cf9f274a-1410-4baf-81e3-d64b45684b72.png)

BESIGE is a Python terminal game, where the user lead an attak to a castle

A live version of the game can be found [here](https://besige.herokuapp.com/)

# How to play

## Scope

In this game you will lead the attack of a siege at the beginning of the game over the name and difficulty of the siege
you can choose how to compose your army and how to approach the siege "day by day" via input.

The aim of the game is to conquer the castle by force or to conquer it by wasting away.

You win when all the walls of the castle are conquered or when the defending garrison runs out of food.

![vincere](https://user-images.githubusercontent.com/80674568/129058926-cdf70830-e850-44ad-a2ad-da63716a1a34.PNG)

Attention! you could run out of food or men in that case you lose the game!

![perdere per mancanza di cibo](https://user-images.githubusercontent.com/80674568/129058171-ffe9c65b-05d5-4452-bce0-976bae499b6b.PNG)

## Set Army

Your army can have the maximum size of 200 points.
and you will start whit only 300 unit of food

the troops you can choose are two types:

- spy : their value is 10 points
- scout : their value is 5 points

the remaining points will be converted into regular soldiers:

- regular soldiers : their value is 1 point

### 200 point = soldiers + spy x 10point + scout x 5point

![controllo scelta armata](https://user-images.githubusercontent.com/80674568/129058167-2f8b8cd4-6f05-4a30-85f0-6dc5ac60e36e.PNG)

In the meantime the computer will have an army composed of a variable number of troops ranging from 50 to 100 soldiers.
The defenders were ready and have amassed 1000 units in their food supplies.

## Maintaining Unit:

At the end of each turn you will consume an amount of food equal to the size of your army.

Don't make it too big that you eat too much food quickly and not too small that you can't attack the walls.

![perdere per mancanza di cibo](https://user-images.githubusercontent.com/80674568/129058171-ffe9c65b-05d5-4452-bce0-976bae499b6b.PNG)

## Spy:

spy can tell to the user how many men defend the castle.
if the user is lucky he may be able to sabotage the computer's food supply.
Sabotage is related to the number of spies in the army!

Attention spying is a risky action and you could risk losing a spy in action.

![perdere una spia](https://user-images.githubusercontent.com/80674568/129058174-67159767-d1c9-45a8-8c7a-bc8de98a066b.PNG)

If you run out of spies, you will no longer be able to spy on your opponent

## Scout:

The scouts allow to forages at cost of one day of siege can give from 10 to 50 unit of food per scout

but remember you could be attacked in a defender sortie!
                        
## Regular soldier:

They are the meat of the slaughter, they number in the army, and as long as you have an army you can storm the castle
Attacking will allow you to try to conquer the walls by losing men.
but in the end you can get an estimate based on the men lost on how big the enemy army is:

![attacco e poi scelta](https://user-images.githubusercontent.com/80674568/129058162-e537d573-3237-4f1d-94cd-bd25d0aa52dc.PNG)

If the defenders are more than 90, you will lose 25% of your army

If the defenders are more than 80, you will lose 20% of your army

If the defenders are more than 60, you will lose 15% of your army

If the defenders are more than 30, you will lose 10% of your army

If the defenders are less than 30, you will lose 5% of your army


# Features:
## Existing Features:

- Player select his army:

![scelta esercito](https://user-images.githubusercontent.com/80674568/129058180-6999bd18-5dd6-4794-bfe9-2e2031446eaf.PNG)

- The player is forced to use spies to get information on the enemy:

![spionaggioriuscito](https://user-images.githubusercontent.com/80674568/129060421-3b07c00b-4422-4f04-97cc-503cf82b07d9.PNG)

- Required player name and game difficulty:

![scegli nome](https://user-images.githubusercontent.com/80674568/129058177-e1cbbb21-145d-479e-ad55-84e3ed403100.PNG)

- Inform the player of how many resources he has at the end of the turn and allow him to act accordingly:

![foraggiare e poi scelta](https://user-images.githubusercontent.com/80674568/129058168-291df478-b369-4945-9398-78ca9c3a5818.PNG)

- Input validation and and request of last input:

![controllo input](https://user-images.githubusercontent.com/80674568/129058163-ea0080d0-9c49-46e2-a1e9-aba19b0cce0c.PNG)
![controllo scelta armata](https://user-images.githubusercontent.com/80674568/129058167-2f8b8cd4-6f05-4a30-85f0-6dc5ac60e36e.PNG)

## Future Features:

- Implement functions that make the computer more aggressive
- Make the game actually more balanced
- Add other elements of randomness eg. the beginning of illnesses and the arrival of reinforcements for the besieged

# Data Model:

![Siedge Game in python!](https://user-images.githubusercontent.com/80674568/129062806-0d3aead7-9cc6-41b2-9585-9e903111c6ff.jpeg)

The game is divided into two main phases:
- Preparation phase (where the player and the pc choose which data to start with)
- Game stage (the loop phase that will repeat until the attackers run out of units or food or when the defenders run out of food or the attackers conquer the walls)

# Testing:

## Fixed Bugs

- I used [PEP8 online](http://pep8online.com/) to check code for PEP8 requirements. Bugs in writing the code were inherent in the unintentional creation of blanks.
Still impossible to remove this error results at the end of the code but this does not affect the functioning of the code

- Input for scout and spy: if i put casual strings the game stop to work so i had to create a function to control if the user use numbers instead strings

- The loop phase dont play as i aspected so i create a alive variable to check the loop phase and stop it properly.

## Existing bugs

- The analysis function does not always seem to correctly calculate the days in which the player chooses to forage

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

1. Fork or clone this repository

2. Create a new Heroku app

3. Set the buildbacks to Python and NodeJS in that order

4. Link the Heroku app to repository

5. Click on Deploy


# Credit

I thank my tutor Marcel who, as usual, gave me excellent practical indications and pushes me to find more elegant solutions in drafting the code.

A special thanks to the beers with friends that allow you to have some nice ideas.

Thank you for taking the time to read my project.