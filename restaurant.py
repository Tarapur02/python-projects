

import pandas as pd

print("Welcome to our restaurant. Here's the menu:")

data = {
    "Idli": 30,
    "Dosa": 50,
    "Vada": 25,
    "Puri": 40,
    "Upma": 35,
    "Rice": 60,
    "Chapati": 10,
    "Paneer Curry": 120,
    "Chicken Curry": 150,
    "Veg Biryani": 110,
    "Chicken Biryani": 160,
    "Coffee": 20,
    "Tea": 15
}

food_items = pd.DataFrame(list(data.items()), columns=["Food Item", "Price"])

print(food_items)

def order():
    while True:
        user_input = input("Enter the food item you want: ").lower()

        if user_input == "idli":
            price = food_items.loc[food_items["Food Item"].str.lower() == "idli", "Price"].values[0]
            print("Price of Idli is:", price)
            user=input("would you like to order more (y/n):").lower()

            if user=="y":
                order()
            
            break
        else:
            print("Item not found. Please try again.")


order()


