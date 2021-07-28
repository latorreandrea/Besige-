# python code goes here
print("  ____                 _")
print(" |  _ \               (_)")
print(" | |_) |   ___   ___   _    ___    __ _    ___")
print(" |  _ <   / _ \ / __| | |  / _ \  / _` |  / _ \\")
print(" | |_) | |  __/ \__ \ | | |  __/ | (_| | |  __/")
print(" |____/   \___| |___/ |_|  \___|  \__, |  \___|")
print("                                   __/ |")
print("                                  |___/")

role = input("in this siege will you attack or defend?\n")

difficulty = input("how many walls will this castle have?\nchoose a numerical value between 1 and 3\n")

day = 1
while True:
   choose = input("What do you want to do, my lord?")
   print(f"{day} you did {choose}")
   day = day + 1