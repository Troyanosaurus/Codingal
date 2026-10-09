while True:
    name = input("\nHello what is your name?\n")
    print("Nice to meet you", name)

    mood = input("How are you feeling today? (good/neutral/bad)\n")

# Good mood
    if mood == "good":
        hobbie = input("Thats good, what are you hobbies?\n")
        print("Thats cool")
        food = input("What is your favourite food?\n").title()
        if food != "Butter Chicken":
            print("ew")
        else:
            print("Yum")
        print(f"\n{name}:\nHobbies: {hobbie}\nFavourite food: {food}")
        while True:
            restart = input("Do you want to keep chatting? (Y/N)\n")
            if restart == "Y":
                break
            elif restart == "N":
                print("\nBye bye")
                exit()
            else:
                print("Please enter Y or N")

# Netural mood
    elif mood == "neutral":
        today = input("Thats pretty neutral, what did you do today?\n")
        print("Ok")
        bones = int(input("How many bones have you broken in your life?\n"))
        if bones <= 20:
            print("Ok")
        else:
            print("Wow!")
        print(f"\n{name}:\nDid today: {today}\nBones broken: {bones}")
        while True:
            restart = input("Do you want to keep chatting? (Y/N)\n")
            if restart == "Y":
                break
            elif restart == "N":
                print("\nBye bye")
                exit()
            else:
                print("Please enter Y or N")

# Bad mood
    elif mood == "bad":
        why = input("Thats pretty bad, why?\n")
        print("Thats to bad")
        friends = input("Do you have an friends? (Y/N)\n")
        if friends == "Y":
            friends = "yes"
            print("Good")
            print(f"\n{name}:\nReason for feeling bad: {why}\nHas friends?: {friends}")
            while True:
                restart = input("Do you want to keep chatting? (Y/N)\n")
                if restart == "Y":
                    break
                elif restart == "N":
                    print("\nBye bye")
                    exit()
                else:
                    print("Please enter Y or N")

        if friends == "N":
            friends = "No"
            print("How sad, thats to bad")
            print(f"\n{name}:\nReason for feeling bad: {why}\nHas friends?: {friends}")
            while True:
                restart = input("Do you want to keep chatting? (Y/N)\n")
                if restart == "Y":
                    break
                elif restart == "N":
                    print("\nBye bye")
                    exit()
                else:
                    print("Please enter Y or N")
        
