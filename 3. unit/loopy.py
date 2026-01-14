Dispatch_line = []
Truck = []
while True:
    print("chose an option from below")
    print("1. Place order")
    print("2. Move order to loading bay")
    print("3. Remove your last package")
    decision = input("Input your choice ")
    
    if decision == "1":
        Order = input("what is your product ")
        Dispatch_line.append(Order)
        print(f"You added {Order} was added to the Dispatch line ")

    elif decision == "2":
        if not Dispatch_line:
            print("You have nothing to put in a truck")
        else :
           
            Order = Dispatch_line.pop(0)
            Truck.append(Order)
            print(f"Your {Order} is in the truck")
    elif decision == "3":
        if not Truck:
            print("The truck is empty")
        else:
            last_item = len(Truck) - 1
            returned_item = Truck.pop(last_item)
            Dispatch_line.append(returned_item)
            print(f"Your {returned_item} is back at dispatch line")