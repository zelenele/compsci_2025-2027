def shoping_experience():
    total_spent = 0
    # it Keeps track of the spendings later
    print("Welcome to Target")
    Wallet = int(input("How much money do you have "))
    # Asks user how much money he has

    #Loops the program until the user 
    while True:
        Shoping = input("What would you like to buy ").lower()
        if Shoping == "done":
            # If user types "done" the program quits 
            print(f"Thank you for your money, you have spent {total_spent}")
            break
        else:
            Cost = input(f"How much does {Shoping} cost ")
            Cost = int(Cost)
            if Wallet == 0:
                print(f"brokie you have no money left, you have spent {total_spent} int the shop")
                break
              # if user has no money the program will quit
            
            
            elif Wallet < Cost:
                print("Invalid funds")
                
            # if user has not enough money the program will see it and 
           
          
            else:
                Wallet -= Cost
                total_spent += Cost
                # subtracts the money from the user and also keeps count of how many he has spent
                print(f"{Shoping} was added to your cart")
            print(f"Your balance is {Wallet}")


print(shoping_experience())