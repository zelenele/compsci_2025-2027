print("Welcome to aloha bar")
price = 0
Count = 0
while True:
    Drink = input("What juice would you like to order?")
    if Drink.lower() == "done":
        print(f"your bill is {price}$,for {Count} drinks, have a nice day")
        break
    else:
        Cost = input(f"How much does a {Drink} juice cost")
        Cost = float(Cost)
        price += Cost
        print(f"Your bill is {price}")
        Count += 1

    