import random
# python code goes here
a_food = [300]
d_food = [1000]
d_army_size = []
a_army_size = []
days = [1]
scout_number = 0
spy_number = 0
alive = True


print("  ____                 _")
print(" |  _ \               (_)")
print(" | |_) |   ___   ___   _    ___    __ _    ___")
print(" |  _ <   / _ \ / __| | |  / _ \  / _` |  / _ \\")
print(" | |_) | |  __/ \__ \ | | |  __/ | (_| | |  __/")
print(" |____/   \___| |___/ |_|  \___|  \__, |  \___|")
print("                                   __/ |")
print("                                  |___/")


def prepare_siege():
    """
    calculate the size of the army based on the choice of units
    """
    global spy_number
    global scout_number
    print("As attacker you will start with 300 units of food")
    print("at the end of each round you will have consumed")
    print("as many units of food as there are men on the field")
    print(f"{name},how many men will follow you?\n")

    spy_number = input("how many spy do you take?\n")
    check_user_input(spy_number)

    scout_number = input("how many scout do you take?\n")
    check_user_input(scout_number)
    MAX_SIZE = 200

    print("creating your army...")
    soldiers_number = MAX_SIZE - int(spy_number) * 10 - int(scout_number) * 5
    army_size = soldiers_number + int(spy_number) + int(scout_number)
    if soldiers_number > 0:
        print(f"Your army is {army_size} strong")
        print(f"the army is made up of {soldiers_number} regular soldiers")
        print(f"{spy_number} spies")
        print(f"{scout_number} scouts")
        print("You will start with 300 units of food")
        a_army_size.append(army_size)
        castle_garrison = random.randint(50, 100)
        d_army_size.append(castle_garrison)
        game_stage()

    else:
        print("""your army can't be less than 1 man:
remember 1 spy is euqal to 10 soldiers
1 scout to 5 soldiers""")
        tutorial()
        return


def take_wall():
    """
    go to attack() definition
    """
    global level
    level = 0
    level += 1
    print("sire we have taken the walls!")


def repelled():
    """
    go to attack() definition
    """
    print("they rejected us sir!")


def check_user_input(input):
    """
    Convert it into integer to be sure we dont have a string input
    """
    try:
        val = int(input)
        print("valid input")
    except ValueError:
        print("the game accepts only integer values")
        prepare_siege()


def attack():
    """
    based on how the attack went, it is estimated how many defend the castle.
    aa_army_size is for current/actual attaking army size.
    ad_army_size is for current/actual defending army size.
    If attack succeeded the player conquer the wall
    """
    if d_army_size[-1] > 90:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 25)/100)
        take_wall() if random.randint(1, 10) == 5 else print("they reject us")
        ad_army_size = int(d_army_size[-1] - (d_army_size[-1] * 5)/100)
    elif d_army_size[-1] > 80:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 20)/100)
        take_wall() if random.randint(1, 8) == 5 else print("they reject us")
        ad_army_size = int(d_army_size[-1] - (d_army_size[-1] * 8)/100)
    elif d_army_size[-1] > 60:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 15)/100)
        take_wall() if random.randint(1, 7) == 5 else print("they reject us")
        ad_army_size = int(d_army_size[-1] - (d_army_size[-1] * 10)/100)
    elif d_army_size[-1] > 30:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 10)/100)
        take_wall() if random.randint(1, 6) == 5 else print("they reject us")
        ad_army_size = int(d_army_size[-1] - (d_army_size[-1] * 12)/100)
    else:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 5)/100)
        take_wall() if random.randint(1, 5) == 5 else print("they reject us")
        ad_army_size = int(d_army_size[-1] - (d_army_size[-1] * 15)/100)
    a_army_size.append(aa_army_size)
    d_army_size.append(ad_army_size)

    print(f"the men returned from combat are {a_army_size[-1]}")
    a_stocks()
    d_stocks()


def foraging():
    """
    look for supplies. Attention! if you are attacked
    you have a 1 in 3 chance of losing men in a sortie
    """
    global scout_number

    if int(scout_number) > 0:

        if random.randint(0, 100) > 80:
            scout_number = int(scout_number) - 1
            print("our men have been intercepted!")
            print(f"now we have {scout_number} scouts...")

        else:
            food = a_food[-1] + int(scout_number) * random.randint(10, 50)
            a_food.append(food)
            print(f"now we have {food} unit of food!")

        a_stocks()
        d_stocks()

    else:
        print(f"sire {name} we have no more scout ... choose another approach")
        choice()
    a_army_size.append(a_army_size[-1])
    d_army_size.append(d_army_size[-1])


def discover():
    """
    go to spy() definition
    """
    global spy_number
    if random.randint(0, 100) > 50:
        spy_number = int(spy_number) - 1
        print("our man has not returned")
        print(f"now we have {spy_number} spy...")
    else:
        print("The army in the castle is", d_army_size[-1], "strong")
        resistance = int((d_food[-1]) / (d_army_size[-1]))
        print(f"They can resist {resistance} days")
    a_stocks()
    d_stocks()


def sabotage():
    """
    go to spy() definition
    """
    if random.randint(0, 100) <= int(int(spy_number) * 1.5):
        castle_supply = d_food[-1] - (random.randint(0, 10) * int(spy_number))
        d_food.append(castle_supply)
        supplies_destroyed = d_food[-2] - d_food[-1]
        print(f"sir {name},we destroyed {supplies_destroyed} supplies!")
        a_stocks()
        d_stocks()
    else:
        discover()


def spy():
    """
    tell us how many men defend the castle
    or they can sabotage food supplies
    """
    if int(spy_number) > 0:
        if random.randint(0, 100) >= 80:
            sabotage()
        else:
            discover()
    else:
        print(f"sire {name} we have no more spies ... choose another approach")
        a_stocks()
        d_stocks()
        choice()
    a_army_size.append(a_army_size[-1])
    d_army_size.append(d_army_size[-1])


def choice():
    """
    the user chooses what action to take for the current turn
    """
    print(f"Directions sir {name}?")
    choice = input("press:\n 1 to attack\n 2 to foraging\n 3 to spy\n")

    while choice not in ["1", "2", "3"]:
        print(f"sir {name} we wouldn't know how to do it ...")
        choice = input("press:\n 1 to attack\n 2 to foraging\n 3 to spy\n")

    if choice == "1":
        print("we are attacking the walls...")
        attack()
    if choice == "2":
        print("looking for supplies...")
        foraging()
    if choice == "3":
        print("infiltrating the castle...")
        spy()


def a_stocks():
    """
    Calculate the remaining food at the end of the day for the attakers
    """
    day = int(days[-1]) + 1
    days.append(day)
    a_today_stock = a_food[-1] - a_army_size[-1]
    a_food.append(a_today_stock)
    print(f"{a_today_stock} are the stocks in the end of this day")


    if a_today_stock < 1:
        end_game()


def d_stocks():
    """
    Calculate the remaining food at the end of the day for the defenders
    """
    d_today_stock = d_food[-1] - d_army_size[-1]
    d_food.append(d_today_stock)
    if d_today_stock < 1:
        end_game()


def end_game():
    global alive
    alive = False
    if a_food[-1] < 1:
        print("we are forced to withdraw! we have no more food!")
        print("You lose the besiege!")
    if d_food[-1] < 1:
        print("the enemy can no longer resist! they are short of food!")
        print("You win the besiege!")
    menu()


def tutorial():
    """
    Shows how to play.
    Shows the types of units and their peculiarities
    """
    tutorial_text = [
        (
            "In this game you will lead the attack of a siege\n"
            "at the beginning of the game over the name and difficulty\n"
            "you can choose how to compose your army\n"
        ), (
            "your army can have the maximum size of 200 points\n"
            "besides the regular soldiers that are worth only 1 point\n"
            "you can choose how many scouts and spy to take with you\n"
        ), (
            "the value of the spy is 10 points.\n"
            "the value of the scouts is 5 points\n"
            "the remaining points will be converted into regular soldiers\n"
            "up to an army value of 200 points\n"
        ), (
            "At the start of each turn, choose what your army will do\n"
            "the possible actions will be: Attack, forage and spy\n"
        ), (
            "attacking will allow you to conquer the walls by losing men.\n"
            "but in the end you can get an estimate based on the men lost\n"
            "on how big the enemy army is\n"
        ), (
            "forages at cost of one day of siege\n"
            "can give from 0 to 50 unit of food per scout\n"
            "but remember you could be attacked in a defender sortie!\n"
        ), (
            "spy can tell us how many men defend the castle\n"
            "or they can sabotage food supplies\n"
        )
    ]

    tutorial = input("press:1 to start tutorial 2 to start game\n")
    while tutorial not in ["1", "2"]:
        tutorial = input("press:1 to start tutorial 2 to start game\n")

    i = 0
    for text in tutorial_text:

        if tutorial == "1":            
            print(text)

        if tutorial == "2":
            start_game()

        tutorial = None

        while tutorial not in ["1", "2"]:
            tutorial = input("press:1 to continue tutorial 2 to start game\n")
        i += 1
        if i == len(tutorial_text):
            print("Actually, the tutorial is finished!")
            break

    start_game()


def game_stage():
    while alive is True:
        choice()
    if alive is False:
        menu()


def menu():
    """
    the user can choose whether to see
    the progress of the battle, restart or quit the game
    """
    global alive
    alive = False
    analyses = input(
        "press 1 to analyze match data\n"
        "press 2 to exit the game\n"
        "press 3 to restart the game\n"
    )
    while analyses not in ["1", "2", "3"]:
        analyses = input(
            "press 1 to analyze match data\n"
            "press 2 to exit the game\n"
            "press 3 to restart the game\n"
        )
    if analyses == "1":
        print("analyzing the battle...")
        
        for x, y, z in zip(a_army_size, a_food, days):
            print(f"Day{z}:you have {x} man, {y} food")

    if analyses == "2":
        print("exit from the game...")
        exit()

    if analyses == "3":
        print("restarting game...")
        alive = True
        restart()
        tutorial()


def start_game():
    print("game starting...")
    print("Who will lead the siege?")
    global name
    name = input("player name:\n")

    print(
        "how many walls will this castle have?\n"
        "(This will affect the difficulty of the game)\n")
    global difficulty

    difficulty = input("choose a numerical value between 1 and 3\n")

    while difficulty not in ["1", "2", "3"]:
        difficulty = input("choose a numerical value between 1 and 3\n")

    prepare_siege()


def conquer_walls():
    """
    if the player takes the walls as many times
    as the selected difficulty then he wins the game
    """
    if level == int(difficulty):
        print(
            f"Sir {name}! The castle is in our hands!"
            "You won the game"
            )
        menu()


def restart():
    d_army_size.clear()
    a_army_size.clear()
    global a_food
    a_food = [300]
    global d_food
    d_food = [1000]
    global days
    days = [1]
    global scout_number
    scout_number = 0
    global spy_number
    spy_number = 0


tutorial()