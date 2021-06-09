import time
import random

mylist = ["Genie", "Tinkerbell", "Casper"]


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def start():
    start = input("Welcome to the game,would you like to play? (y/n)")
    if start == "n":
        print("Ok good-bye")
    elif start == "y":
        print("Welcome to the game")
        intro()


def intro():
    print_pause("You were walking home from a party, late one summer night.")
    print_pause("You danced and sang, under the stars that shone so bright")
    print_pause("It was late and you needed to get home really really quick")
    print_pause("you decided to take a shortcut up the alley,")
    print_pause("by the house on the road made of yellow brick")
    alley()


def alley():
    print()
    print_pause("you find yourself staring at a man standing beside two doors")
    print_pause("He called you over and said which adventure will be yours?")
    choose_doors()


def choose_doors():
    print()
    print_pause("There are two doors, one with a picture of a magic carpet")
    print_pause("the other a magic lamp.")
    print()
    response = input("Which door do you choose. The carpet or the lamp? ")
    if response == "carpet":
        print_pause("carpet it is. enjoy the ride!")
        print()
        print_pause("You open the door and see a flying carpet")
        print_pause("two meters long.")
        print_pause("It\'s tattered and torn, do you dare to get on?")
        carpet_ride()
    elif response == "lamp":
        print_pause("lamp it is. May it lead you home!")
        print()
        print_pause("You open the door, and there is a magic lamp laying")
        print_pause("on the floor.")
        print_pause("You rub the lamp, and")
        print(random.choice(mylist))
        print_pause("pops out")
        print_pause("giving a hell of a shout! WHAT WILL IT BE")
        print_pause("Back into the alley, or take a chance with me?")
        magic_lamp()
    else:
        repeat()


def carpet_ride():
    print()
    answer = input("Please choose yes or no.")
    print()
    if answer == "yes":
        print_pause("You are whisked away, flying into the air.")
        print_pause("Back and forth, you seem to be flying everywhere.")
        print_pause("You fly into a thunderstorm the carpet slowly unravels")
        carpet_help()
    else:
        alley()
        choose_doors()


def magic_lamp():
    print()
    answer = input("What is your choice alley or chance ")
    if answer == "chance":
        print_pause("you are granted a wish, and fly's you back home.")
        print_pause("You made it in time, the spell is broken and at last")
        print_pause("it\'s all ova")
        print_pause("and you are back to being Pricess Fiona")
        print_pause("Congratulations - game over")
        start()
    else:
        alley()
        choose_doors()


def repeat():
    response = input("You need to choose carpet or lamp ")
    if response == "carpet":
        print_pause("carpet it is. enjoy the ride!")
    elif response == "lamp":
        print_pause("lamp it is. May it lead you home!")
    else:
        print_pause("Good-bye, better luck next time!")
        start()


def carpet_help():
    print_pause("Do you scream for help or continue on your travels?")
    scream = input("Please choose help or continue ")
    if scream == "help":
        print_pause("You scream for help and and Aladin appears,")
        print_pause("he is a master of tricks and he has no fears.")
        print_pause("And faster than you can say Oh My Salley!,")
        print_pause("he has guided you safely back into the alley")
        choose_doors()
    else:
        carpet_continue()


def carpet_continue():
    print_pause("You continue on on your travels,")
    print_pause("as the carpet slowely unravels. You find yourself falling")
    print_pause("and you land back at home. The sun has risen,")
    print_pause("and time is over, you unfortunately turn back")
    print_pause("into an ugly green Ogre.")
    print_pause("You loose, better luck next time!")
    start()


def play_game():
    start()


play_game()
