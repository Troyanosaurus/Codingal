import random, re
from colourama import Fore, init

init(autoreset = True)

D = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
J = {
    "Whats up with the four kids in the back? Because its funny :D",
    "King Kong or she's to strong? She's to strong. Wrong, it was King Kong",
    "Why did the chicky cross the road? To get to the other chicky"
}

def n(x):
    return re.sub("\s+", " ", x.strip().lower())

def rec():
    while 1:
        p = n(input(Fore.YELLOW + "Beaches, mountains, or cities?"))
        if p not in D:
            print(Fore.RED + "Invalid type")
            continue
        s = random.choice(D[p])
        print(Fore.GREEN + f"How about {s}?")
        a = input("Like it? (yes/no): ").lower()
        if a == "yes":
            print(f"Awesome! Enjoy {s}!")
            return


def pack():
    l = n(input("Where to? "))
    d = input("How many days? ")



