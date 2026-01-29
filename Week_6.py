import math


_userInput = int(input("What task to run? "))
match _userInput:
    case 1:
        students = ["Amir", "Sarah", "Tom", "Aisha", "Leo"]
        students.append("Shaggy")
        students.append("Scooby")
        students.pop()
        students.insert(0, "Cheesy")
        students.sort()
        print("Current students are ", students)
    case 2:
        favourite_games = [
            "Minecraft", "Fortnite", "Stardew Valley", "Apex Legends",
            "Rocket League", "Overwatch", "Valorant", "Terraria"]

        print("Current game list:")
        print(favourite_games)
        print()

        new_item = input("Add a game to the list: ")
        favourite_games.append(new_item)
        print("\nAdded successfully!")
        print(favourite_games)
        print()
        remove_item = input("Which game would you like to remove? ")
        if remove_item in favourite_games:
            favourite_games.remove(remove_item)
            print("\nRemoved successfully!")
        else:
            print("\nGame not found.")
        print()
        print("Here is your sorted game list:")
        for game in sorted(favourite_games):
            print(" - " + game)
