# BESIGE 

## Code Institute Portfolio 3 Project

![Logo](put here an image of a besige!)

BESIGE is a Python terminal game, where the user lead an attak to a castle

A live version of the game can be found [here](insert link)

![immagineschermi](link to other image)

# How to play

## Scope

In this game you will lead the attack of a siege at the beginning of the game over the name and difficulty of the siege
you can choose how to compose your army and how to approach the siege "day by day" via input.

The aim of the game is to conquer the castle by force or to conquer it by wasting away.

You win when all the walls of the castle are conquered or when the defending garrison runs out of food.

Attention! you could run out of food or men in that case you lose the game!

## Set Army

Your army can have the maximum size of 200 points.
and you will start whit only 300 unit of food

the troops you can choose are two types:

- spy : their value is 10 points
- scout : their value is 5 points

the remaining points will be converted into regular soldiers:

- regular soldiers : their value is 1 point

### 200 point = soldiers + spy x 10point + scout x 5point

In the meantime the computer will have an army composed of a variable number of troops ranging from 50 to 100 soldiers.
The defenders were ready and have amassed 1000 units in their food supplies.

## Maintaining Unit:

At the end of each turn you will consume an amount of food equal to the size of your army.

Don't make it too big that you eat too much food quickly and not too small that you can't attack the walls.

## Spy:

spy can tell to the user how many men defend the castle.
if the user is lucky he may be able to sabotage the computer's food supply.
Sabotage is related to the number of spies in the army!

Attention spying is a risky action and you could risk losing a spy in action.

If you run out of spies, you will no longer be able to spy on your opponent

## Scout:

The scouts allow to forages at cost of one day of siege can give from 10 to 50 unit of food per scout

but remember you could be attacked in a defender sortie!
                        
## Regular soldier:

They are the meat of the slaughter, they number in the army, and as long as you have an army you can storm the castle
Attacking will allow you to try to conquer the walls by losing men.
but in the end you can get an estimate based on the men lost on how big the enemy army is:

If the defenders are more than 90, you will lose 25% of your army

If the defenders are more than 80, you will lose 20% of your army

If the defenders are more than 60, you will lose 15% of your army

If the defenders are more than 30, you will lose 10% of your army

If the defenders are less than 30, you will lose 5% of your army


# Features:
# Future Features:

# Data Model

# Testing

# Deployment

This project was deployed using Code Institute's mock terminal for Heroku.

1. Fork or clone this repository

2. Create a new Heroku app

3. Set the buildbacks to Python and NodeJS in that order

4. Link the Heroku app to repository

5. Click on Deploy


# Credit

Thank you for taking the time to read my project. 