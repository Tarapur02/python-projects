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

print(random.choice(Medium_words))


while True:
    user_input_leval= input("Please Enter What difficulty Leval You what ex:(Normal,Medium,Hard) : ").lower()
    count=0
    if user_input_leval == "normal":
        leval_1=random.choice(Normal_words)
        for i in range(len(leval_1)):
            print(leval_1[i])
        print(leval_1)

        break
    elif user_input_leval == "medium":
        leval_2=random.choice(Medium_words)
        print(leval_2)
        break
    elif user_input_leval == "hard":
        leval_3=random.choice(Hard_words)
        print(leval_3)
        break
    else:
        print("Please Enter valied Input : ")
    
        


    
