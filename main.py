
import time
import random
import sys

totalscore = 0
backpack = []

def tprint(s):
    print(s)
    time.sleep(2)

def game_over():
    print(". . . GAME OVER . . .")
    time.sleep(3)
    sys.exit()

def fight():
    monsters = ['Omega dragon', 'weakminion', 'groupofweakminion', 'big zombie','rock']
    whichmonster = random.choice(monsters)
    if whichmonster=="Omega dragon":
        totalscore += omega_dragon()
        
def omega_dragon():
    tprint("Peto: OH NO IT IS THE OMEGA DRAGON WHAT SHOULD WE DO?!")
    print("* What will you do? *")
    print("1 - Run away")
    print("2 - Attack the monster")
    print("3 - Defend against the monster")
    choice = input()
    if choice == "1":
        tprint("Peto: QUICK IMA THROW SOME ROCKS TO DISTRACT HIM!!")
        tprint("* you both run away from the dragon *")
        return 0
    elif choice == "2":
        if "Omega Katana" in backpack:
            tprint(name + "Do not fear for the omega katana is here")
            tprint("The monster is defeated with only one blow with the omega katana good job you earn 200 points")
            return 200
        else:
            tprint("* you strike the monster, but he is too strong . . . *")
            tprint("Peto: i am pretty sure we lost")
            tprint("* the monster defeats you with its fire breath *")
            game_over()
    else:
        print ("Peto: I do not think that is a choice")

def weakminion():
    tprint("* a small litte cute creature comes out from under a rock *")
    choice = input("1 - say hi\n2- run away\n3 - kill it\n4 - look at it soo much untill you die of its cuteness!")
    if choice == '1':
        minionstate = random.randint(1,4)
        if minionstate == 3:
            tprint(name + ": hi there little guy...")
            tprint("Peto: he may be a little shy")
            tprint("* smiles cutely and gives you the sword of vengeance")
            backpack.append(["Sword Of Vengeance", "Special powers: can kill an asteroid"])
        else:
            tprint("* this little thing grows ten times its size and is ready to eat lunch *")
            tprint(name "& Peto: AHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!")
            tprint("")

l = 0
while l == 0:

    name = input("Please enter your name: ")
    tprint("Oh, that's a beautiful name..")

    tprint("Once upon a time...")
    tprint("Two friends watching the news when suddenly...")
    print("BREAKING NEWS! SCIENTISTS HAVE DISCOVERED AN ASTEROID AS BIG AS MAYBE A RELATIVE OF YOURS!!!")
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
    tprint(name + ": Ok lets go gather some items to be able to fight")
    while True:
        tprint(name + ": So where should we go first?")
        print("1 - Look inside of your home and try to find something useful")
        print("2 - Go into the dangerous forest where there might be something valuable")
        choice=input()
        if choice == "1":
            tprint("Peto: Look over here i found your secret OMEGA katana!")
            tprint(name + ": oh yeah now we are going to be powerful and ready")
            backpack.append(["Omega Katana", "Special powers: its a katana - its cool - kills maybe"])
            break
        elif choice == "2":
            tprint("Peto: Uh i think we will not find anything here i suppose we can just grab this rock")
            tprint(name + ": Well that is disappointing")
            backpack.append(["rock","Special powers: can be thrown to distract monsters - its beautiful"])
            break
        else:
            print ("Peto: I do not think that is a choice")
    tprint(name + ": Ok lets go fight monsters to level up and get stronger and destroy the asteroid")
    
