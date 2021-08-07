import random
# python code goes here

a_food = [200]
d_food = [1000]
d_army_size = []
a_army_size = []
scout_number = 0
spy_number = 0


print("  ____                 _")
print(" |  _ \               (_)")
print(" | |_) |   ___   ___   _    ___    __ _    ___")
print(" |  _ <   / _ \ / __| | |  / _ \  / _` |  / _ \\")
print(" | |_) | |  __/ \__ \ | | |  __/ | (_| | |  __/")
print(" |____/   \___| |___/ |_|  \___|  \__, |  \___|")
print("                                   __/ |")
print("                                  |___/")


def tutorial():
    """
    Shows how to play.
    Shows the types of units and their peculiarities
    """
    print('''    In this game you will lead the attack of a siege
    at the beginning of the game over the name and difficulty of the siege
    you can choose how to compose your army\n''')

    print('''    your army can have the maximum size of 200 points
    besides the regular soldiers that are worth only 1 point
    you can choose how many scouts and spy to take with you\n''')

    print('''    the value of the spy is 10 points.
    the value of the scouts is 5 points
    the remaining points will be converted into regular soldiers
    up to an army value of 200 points\n''')

    print('''    At the start of each turn, you can choose what your army will focus on.
    the possible actions will be: Attack, forage and spy\n''')

    print('''    attacking will allow you to try to conquer the walls by losing men.
    but in the end you can get an estimate based on the men lost
    on how big the enemy army is\n''')

    print('''   forages at cost of one day of siege
    can give from 0 to 50 unit of food per scout\n''')

    print('''   spy can tell us how many men defend the castle
    or they can sabotage food supplies\n''')


#tutorial()


print("Who will lead the siege?")
name = input("player name:\n")

print("how many walls will this castle have?")
difficulty = input("choose a numerical value between 1 and 3\n")


def prepare_siege():
    '''
    calculate the size of the army based on the choice of units
    '''
    global spy_number
    global scout_number
    print("As attacker you will start with 200 units of food")
    print("at the end of each round you will have consumed")
    print("as many units of food as there are men on the field")
    print(f"{name},how many men will follow you?\n")

    spy_number = input("how many spy do you take?\n")
    scout_number = input("how many scout do you take?\n")
    MAX_SIZE = 200

    print("creating your army...")
    soldiers_number = MAX_SIZE - int(spy_number) * 10 - int(scout_number) * 5
    army_size = soldiers_number + int(spy_number) + int(scout_number)
    print(f"Your army is {army_size} strong")
    print(f"the army is made up of {soldiers_number} regular soldiers")
    print(f"{spy_number} spies")
    print(f"{scout_number} scouts")
    print("You will start with 200 units of food")
    
    a_army_size.append(army_size)
    castle_garrison = random.randint(50, 100)
    d_army_size.append(castle_garrison)


def take_wall():
    print("sire we have taken the walls!")
def repelled():
    print("they rejected us sir!")

def attack():
    '''
    based on how the attack went, it is estimated how many men defend the castle.
    aa_army_size is for current/actual attaking army size.
    If attack succeeded the player conquer the wall
    '''
    if d_army_size[-1] > 90:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 25)/100)
        take_wall() if random.randint(0, 10) == 5 else print("they rejected us")
    elif d_army_size[-1] > 80:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 20)/100)
        take_wall() if random.randint(0, 8) == 5 else print("they rejected us")
    elif d_army_size[-1] > 60:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 15)/100)
        take_wall() if random.randint(0, 7) == 5 else print("they rejected us")
    elif d_army_size[-1] > 30:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 10)/100)
        take_wall() if random.randint(0, 6) == 5 else print("they rejected us")
    else:
        aa_army_size = int(a_army_size[-1] - (a_army_size[-1] * 5)/100)
        take_wall() if random.randint(0, 5) == 5 else print("they rejected us")
    a_army_size.append(aa_army_size)
    print(f"the men returned from combat are {a_army_size[-1]}")


def foraging():
    '''
    look for supplies. Attention! if you are attacked
    you have a 1 in 3 chance of losing men in a sortie
    '''
    food = a_food[-1] + int(scout_number) * random.randint(10, 50)
    a_food.append(food)
    print(f"now we have {food} unit of food!")


def discover():
    if random.randint(0, 100) >= 50:
        spy_number -= 1
    else print ("the enemy have" + d_army_size[-1] + "soldiers!")

def sabotage():
    
def spy():
    '''
    tell us how many men defend the castle or they can sabotage food supplies
    '''
    if random.randint(0, 100) >= 80:
        sabotage()
    else discover()

def choice():
    '''
    the user chooses what action to take for the current turn
    '''
    print(f"Directions sir {name}?")
    choice = input("press:\n 1 to attack\n 2 to foraging\n 3 to spy\n")
    if choice == "1":
        print("we are attacking the walls...")
        attack()
    if choice == "2":
        print("looking for supplies...")
        foraging()
    #if choice == "3":
        #print("infiltrating the castle...")
        #spy()    


#def stocks():
    '''
    Calculate the remaining food at the end of the day
    '''
#    stock = [300]    
#    today_stock = stock[-1] - army
#    print(f"{today_stock} are the stocks in the end of this day")

#stocks()    

def start_game():
    starting_army = prepare_siege()
    choice()

start_game()
