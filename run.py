# python code goes here
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

tutorial()


print("Who will lead the siege?")
name = input("player name:\n")

print("how many walls will this castle have?")
difficulty = input("choose a numerical value between 1 and 3\n")


def prepare_siege():
    '''
    calculate the size of the army based on the choice of units
    '''
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
    return army_size

starting_army = prepare_siege()

def choice():
    '''
    the user chooses what action to take for the current turn
    '''
    print(f"Directions sir {name}?")
    choice = input("press:\n 1 to attack\n 2 to foraging\n 3 to spy\n")
    if choice == "1":
        print("we are attacking the walls...")
        #attack()
    if choice == "2":
        print("looking for supplies...")
        #foraging()
    if choice == "3":
        print("infiltrating the castle...")
        #spy()

'''
def stocks():
    '''
    #calculate the remaining food at the end of the day
    '''
    INITIAL_STOCKS = 300
    first_day_stock = INITIAL_STOCKS - starting_army
    today_stock = first_day_stock - army
    print(f"{today_stock} are the stocks in the end of this day")

stocks()    
'''
def start_game():
    prepare_siege()

start_game()

"""
day = 1
while True:
   choose = input("What do you want to do, my lord?")
   print(f"{day} you did {choose}")
   day = day + 1
"""