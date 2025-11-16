print("Untold hardship,let the game begin")
name=input("Enter your name rookie :  ").title()
item=[]
room = {
    "entrance": {
        "description": "You are at the entrance of an ancient temple.",
        "north": "hallway",
        "item": "map"
    },
    "hallway": {
        "description": "A long, dusty hallway with carvings on the wall.",
        "south": "entrance",
        "east": "library",
        "west": "armory",
        "north": "throne_room",
        "item": "torch"
    },
    "library": {
        "description": "A dark library full of old books and scrolls.",
        "west": "hallway",
        "item": "key"
    },
    "armory": {
        "description": "Rusty weapons and shields line the walls.",
        "east": "hallway",
        "item": "sword"
    },
    "throne_room": {
        "description": "A massive hall with a golden throne at the end.",
        "south": "hallway",
        "east": "treasure_room",
    },
    "treasure_room": {
        "description": "A locked room filled with treasure!",
        "west": "throne_room",
        "requires": "key",
        "item": "treasure"
    }
}
def main():
    while True:
        a=input("Enter start to start and enter exit to exit :  ").lower()
        if a=="start":
            print(f'Welcome {name},All eyes are on you ')
            print("Important rules are as follows")
            print("Enter the direction name to move in that direction")
            print("Enter item name to pick up that item in a particular area")
            print("Enter fight to fight an opponent  ")
            print("Remeber u will need specific items to fight or pick up other precious items")
            print(f"All the best {name}")
            entrance()
            break
        elif a=="exit":
            print(f"Thanks for playing {a},visit again")
            break
        else:
            print("Invalid input,please try again")   
def entrance():
    current=room["entrance"]
    print(current["description"])
    while True:
        a=input("Enter command :  ").lower()
        if a=="north":
            hallway()
            break
        elif a=="item":
            if "map" in item:
                print('You have already collected the map')
            else:
                print("You have picked up the map, congratulations ")
                item.append("map")
        else:
            print("Invalid command,please try again")
def hallway():
    current=room["hallway"]
    print(current["description"])
    while True:
        a=input("Enter command :  ").lower()
        if a=="north":
            throne()
            break
        elif a=="south":
            entrance()
            break
        elif a=="east":
            library()
            break
        elif a=="west":
            armory()
            break
        elif a=="item":
            if "torch" in item:
                print('You have already collected the torch')
            else:
                print("Congratulations, you have picked up a torch ")
                item.append("torch")
        else:
            print("Invalid command,please try again")
def library():
    current=room["library"]
    print(current["description"])
    while True:
        a=input("Enter command : ").lower()
        if a=="west":
            hallway()
            break
        elif a=="item":
            if "key" in item:
                print('You have already collected the key')
            else:
                print("Congratulations, you have picked up a key")
                item.append("key")
        else:
            print("Invalid command, please try again") 
def armory():
    current=room["armory"]
    print(current["description"])
    while True:
        a=input("Enter command :  ").lower()
        if a=="east":
            hallway()
            break
        elif a=="item":
            if "sword" in item:
                print('You have already collected the sword')
            else:
                print("Congratulations, you have picked up a sword")
                item.append("sword")
        else:
            print("Invalid command,please try again")
def throne():
    current=room["throne_room"]
    print(current["description"])
    while True:
        a=input("Enter command :  ").lower()
        if a=="south":
            hallway()
            break
        elif a=="east":
            treasure()
            break
        else:
            print("Invalid command,please try again")
def treasure():
    current=room["treasure_room"]
    print(current["description"])
    while True:
        a=input('Enter command').lower()
        if a=="west":
            throne()
            break
        elif a=="item":
            if "treasure" in item:
                print('You have already collected the treasure')
            else:
                if "key" in item:
                    print("Congratulations, you have picked up the treasure ")
                    item.append("treasure")
                    print("Congratulations, You have won the game")
                else:
                    print("Please collect the item key to unlock treasure")
        else:
            print("Invalid command.please try again")   
main()


