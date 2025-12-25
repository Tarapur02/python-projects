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

def show_hint(secret, guess):
    for i in range(min(len(secret), len(guess))):
        if guess[i] == secret[i]:
            print(f" '{guess[i]}' is in the correct position")

def normal(word):
    count=0
    while True:
        user_input = input("Enter The Word: ").lower()
        if user_input == word:
            print("Your Guess is Correct!")
            thank()
        else:
            show_hint(word, user_input)
        count +=1
def medium(word):
    while True:
        user_input = input("Enter The Word: ").lower()
        if user_input == word:
            print("Your Guess is Correct!")
            thank()
        else:
            show_hint(word, user_input)

def hard(word):
    while True:
        user_input = input("Enter The Word: ").lower()
        if user_input == word:
            print("Your Guess is Correct!")
            thank()
        else:
            show_hint(word, user_input)

def thank():
    while True:
        play = input("You Want Play More (Y/N): ").lower()
        if play == "y":
            main()
            return
        elif play == "n":
            print("Thank you Have a Good Day....")
            exit()
        else:
            print("Please enter Y or N")

def main():
    user_input_level = input(
        "Please Enter What difficulty Level You want (Normal / Medium / Hard): "
    ).lower()

    user = input("You want any Hint (Y/N): ").lower()

    if user == "y":
        if user_input_level == "normal":
            print("Hint: Length of Word is 3")
        elif user_input_level == "medium":
            print("Hint: Length of Word is 4")
        elif user_input_level == "hard":
            print("Hint: Length of Word is 5")

    if user_input_level == "normal":
        normal(random.choice(Normal_words))
    elif user_input_level == "medium":
        medium(random.choice(Medium_words))
    elif user_input_level == "hard":
        hard(random.choice(Hard_words))
    else:
        print("Invalid level. Try again.")
        main()

main()
