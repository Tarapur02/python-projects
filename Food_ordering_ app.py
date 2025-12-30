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

total_price = 0

def order():
    global total_price

    while True:
        user_input = input("Enter the food item you want: ").lower()
        how_many=int(input("How many plates do you want to order:"))
        

        if user_input == "idli":
            price = food_items.loc[food_items["Food Item"].str.lower() == "idli", "Price"].values[0]
            print("Price of Idli is:", price*how_many)
            total_price += price*how_many

        elif user_input == "dosa":
            price = food_items.loc[food_items["Food Item"].str.lower() == "dosa", "Price"].values[0]
            print("Price of Dosa is:", price*how_many)
            total_price += price*how_many

        elif user_input == "vada":
            price = food_items.loc[food_items["Food Item"].str.lower() == "vada", "Price"].values[0]
            print("Price of vada is:", price*how_many)
            total_price += price*how_many

        elif user_input == "puri":
            price = food_items.loc[food_items["Food Item"].str.lower() == "puri", "Price"].values[0]
            print("Price of Puri is:", price*how_many)
            total_price += price*how_many

        elif user_input == "upma":
            price = food_items.loc[food_items["Food Item"].str.lower() == "upma", "Price"].values[0]
            print("Price of Upma is:", price*how_many)
            total_price += price*how_many

        elif user_input == "rice":
            price = food_items.loc[food_items["Food Item"].str.lower() == "rice", "Price"].values[0]
            print("Price of Rice is:", price*how_many)
            total_price += price*how_many

        elif user_input == "chapati":
            price = food_items.loc[food_items["Food Item"].str.lower() == "chapati", "Price"].values[0]
            print("Price of Chapati is:", price*how_many)
            total_price += price*how_many

        elif user_input == "paneer Curry":
            price = food_items.loc[food_items["Food Item"].str.lower() == "paneer Curry", "Price"].values[0]
            print("Price of Paneer Curry is:", price*how_many)
            total_price += price*how_many

        elif user_input == "veg Biryani":
            price = food_items.loc[food_items["Food Item"].str.lower() == "veg Biryani", "Price"].values[0]
            print("Price of Veg Biryani is:", price*how_many)
            total_price += price*how_many

        elif user_input == "paneer Curry":
            price = food_items.loc[food_items["Food Item"].str.lower() == "paneer Curry", "Price"].values[0]
            print("Price of Paneer Curry is:", price*how_many)
            total_price += price*how_many

        elif user_input == "chicken Biryani":
            price = food_items.loc[food_items["Food Item"].str.lower() == "chicken Biryani", "Price"].values[0]
            print("Price of Chicken Biryani is:", price*how_many)
            total_price += price*how_many

        elif user_input == "coffee":
            price = food_items.loc[food_items["Food Item"].str.lower() == "coffee", "Price"].values[0]
            print("Price of coffee is:", price*how_many)
            total_price += price*how_many
        elif user_input == "tea":
            price = food_items.loc[food_items["Food Item"].str.lower() == "tea", "Price"].values[0]
            print("Price of Tea is:", price*how_many)
            total_price += price*how_many

        else:
            print("Item not found. Please try again.")
            continue

        user = input("Would you like to order more (y/n): ").lower()
        if user != "y":
            print(f"Total Price is: {total_price}")
            break

order()
