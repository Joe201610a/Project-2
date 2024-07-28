import time
import random
import sys

totalscore = 0
backpack = []
Vengeance_Sword = False


def tprint(s):
    print(s)
    time.sleep(2)


def game_over():
    global totalscore
    totalscore = -5000
    print(". . . GAME OVER . . .")
    time.sleep(3)


def fight():
    global totalscore
    tprint("Your total score is " + str(totalscore))
    monsters = ['Omega dragon', 'weakminion']
    whichmonster = random.choice(monsters)
    if whichmonster == "Omega dragon":
        totalscore += omega_dragon()
    elif whichmonster == "weakminion":
        totalscore += weakminion()


def omega_dragon():
    tprint("Peto: OH NO IT IS THE OMEGA DRAGON WHAT SHOULD WE DO?!")
    print("* What will you do? *")
    print("1 - Run away")
    print("2 - Attack the monster")
    print("3 - Defend against the monster")
    choice = input()
    while True:
        if choice == "1":
            tprint("Peto: QUICK IMA THROW SOME ROCKS TO DISTRACT HIM!!")
            tprint("* you both run away from the dragon and lose 10 points *")
            return -10
        elif choice == "2":
            if "Omega Katana" in backpack:
                tprint(name + ": Do not fear for the Omega Katana is here")
                tprint("The monster is defeated with only one blow with the Omega Katana. Good job, you earn 200 points.")
                return 200
            else:
                tprint("* you strike the monster, but he is too strong . . . *")
                tprint("Peto: I am pretty sure we lost")
                tprint("* the monster defeats you with its fire breath *")
                return -1000
        elif choice == "3":
            tprint("Peto: I will defend myself")
            tprint("* you both defend against the monster *")
            tprint("Peto: I am pretty sure we are dead the monster is too strong")
            return -1000
        else:
            print("Peto: I do not think that is a choice")
            continue


def weakminion():
    global Vengeance_Sword
    tprint("* a small little cute creature comes out from under a rock *")
    choice = input("1 - say hi\n2 - run away\n3 - kill it\n4 - look at it so much until you die of its cuteness!\n")
    if choice == '1':
        minionstate = random.randint(1, 4)
        if minionstate == 3 and not Vengeance_Sword:
            tprint(name + ": hi there little guy...")
            tprint("Peto: he may be a little shy")
            tprint("* smiles cutely and gives you the Sword of Vengeance *")
            backpack.append("Sword Of Vengeance")
            Vengeance_Sword = True
            return 100
        else:
            tprint("* this little thing grows ten times its size and is ready to eat lunch *")
            tprint(name + "& Peto: AHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!")
            tprint("* you both run very quickly out of there and you lose 10 points *")
            return -10
    elif choice == '2':
        tprint("* you both run away safely and lose 50 points *")
        return -50
    elif choice == '3':
        tprint("* you easily defeat the weak minion *")
        return 50
    elif choice == '4':
        tprint("* you die of its cuteness *")
        return -1000
    else:
        print("Peto: I do not think that is a choice")
        return 0


def rock():
    tprint("* you found a rock *")
    backpack.append("rock")
    return 0


while True:
    name = input("Please enter your name: ")
    tprint("Oh, that's a beautiful name..")

    tprint("Once upon a time...")
    tprint("Two friends watching the news when suddenly...")
    print("BREAKING NEWS! SCIENTISTS HAVE DISCOVERED AN ASTEROID AS BIG AS A PLANET")
    time.sleep(1)
    print("AND IT'S COMING TOWARDS EARTH AT INCREASING SPEEDS OF VERY FAST SPEEDS FAST!!!!!!")
    tprint("...")
    tprint("...")
    tprint("...")
    tprint("Peto: What.. was.. that..")
    tprint(name + ": I DON'T KNOW WHAT WAS THAT")
    tprint(". . DON'T LOOK AT ME LIKE THAT")
    tprint("Peto: Don't you wanna try?")
    tprint("We are gonna die anyways if no one stopped it")

    while True:
        print("*What will you do?*")
        print("1 - Stay at home and eat nachos")
        print("2 - GO AND DESTROY THE ASTEROID!!")
        choice = input()
        if choice == "1":
            print("Why are you even here..")
            print("I'll give you another chance")
        elif choice == "2":
            break
        else:
            print("We don't have pizza here, sorry?")

    tprint(name + ": Well, you have a point. . .")
    tprint(name + ": Ok let's go gather some items to be able to fight")
    while True:
        tprint(name + ": So where should we go first?")
        print("1 - Look inside of your home and try to find something useful")
        print("2 - Go into the dangerous forest where there might be something valuable")
        choice = input()
        if choice == "1":
            tprint("Peto: Look over here I found your secret OMEGA katana!")
            tprint(name + ": oh yeah now we are going to be powerful and ready")
            backpack.append("Omega Katana")
            break
        elif choice == "2":
            tprint("Peto: Uh I think we will not find anything here I suppose we can just grab this rock")
            tprint(name + ": Well that is disappointing")
            backpack.append("rock")
            break
        else:
            print("Peto: I do not think that is a choice")

    tprint(name + ": Ok let's go fight monsters to level up and get stronger and destroy the asteroid")
    tprint("* you need a total score of 300 points to win this game and if you get less than -49 points you lose *")

    while totalscore < 300 and totalscore > -50:
        fight()

    if totalscore <= -50:
        game_over()
    elif totalscore >= 300:
        tprint("Peto: WE DESTROYED THE ASTEROID AND WE WON YAY")

    tprint("Do you want to play again?")
    print("1 - Yes")
    print("2 - No")
    choice = input()
    if choice == "1":
        totalscore = 0
        backpack.clear()
        Vengeance_Sword = False
    else:
        sys.exit()
