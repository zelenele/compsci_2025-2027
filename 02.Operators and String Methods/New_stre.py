def Membership_discount(price):
    membership_discount_value = price * 0.1
    return membership_discount_value


def Membership_card(card):
    if card == True:
        return True
    else:
        return False

def Basket_price(price, card):
    New_price = price
    if Membership_card(card) == True and price > 100:
        New_price = (price - Membership_discount(price)) - price * 0.1
        return New_price
    elif Membership_card(card) == True:
        New_price = price - Membership_discount(price)
        return New_price
    elif price > 100:
        New_price = price - price * 0.1
        return New_price
    else:
        return New_price
price = int(input("Enter the price of your shopping: "))
New_price = price // 1
card = bool(int(input("Do you have a membership card? (1 for yes, 0 for no): ")))
print("Your final price is: ", Basket_price(New_price, card) // 1)
