import random

print("Welcome To The Word Guessing Game....")

Normal_words = [
    "cat", "dog", "sun", "pen", "hat", "run", "box", "car", "cup", "bat",
    "red", "map", "fan", "bed", "ice", "toy", "cow", "sky", "egg", "key"
]
Medium_words = [
    "book", "tree", "milk", "road", "fish", "time", "star", "wind", "door", "rain",
    "snow", "play", "ball", "lamp", "seat", "hand", "coin", "leaf", "ship", "fire"
]
Hard_words = [
    "apple", "chair", "bread", "plant", "stone", "cloud", "water", "earth", "river", "smile",
    "green", "light", "sound", "train", "house", "music", "phone", "glass", "dream", "night"
]
def normal(level_1):
    while True:
        user_input=input("Enter The Word: ")
        if user_input == level_1:
            print("Your Guess is Currect..")
            thank()
        elif user_input!= level_1:
            for i in range(len(level_1)):
                for j in range(len(user_input)):
                    if level_1[i] == user_input[j]:
                        print(f"The {user_input[i]} is Currect Position..  ")

def medium(level_2):
    while True:
        user_input=input("Enter The Word: ")
        if user_input == level_2:
            print("Your Guess is Currect..")
            thank()
        elif user_input!= level_2:
            for i in range(len(level_2)):
                for j in range(len(user_input)):
                    if level_2[i] == user_input[j]:
                        print(f"The {user_input[i]} is Currect Position..  ")

def hard(level_3):
    while True:
        user_input=input("Enter The Word: ")
        if user_input == level_3:
            print("Your Guess is Currect..")
            thank()
        elif user_input!= level_3:
            for i in range(len(level_3)):
                for j in range(len(user_input)):
                    if level_3[i] == user_input[j]:
                        print(f"The {user_input[i]} is Currect Position..  ")

def thank():
    while True:
        play=input("You Want Play More (Y/N): ") .lower()
        if play== "y":
            main() 
        else:
            print("Thank you Have a Good Day....")
            break


def main():
    user_input_level = input("Please Enter What difficulty Leval You what ex:(Normal,Medium,Hard) : ").lower()

    if user_input_level == "normal":
        level_1=random.choice(Normal_words)
        normal(level_1)
    elif user_input_level == "medium":
        level_2=random.choice(Medium_words)
        medium(level_2)
    elif user_input_level == "hard":
        level_3=random.choice(Hard_words)
        hard(level_3)
    else:
        main()
    

main()
