def membership_discount(New_price):
    membership_discount = final_price * 0.2
    return membership_discount

def Membership_card(Membership_card):
    if Membership_card == True:
         return True
    else:
         return False

def final_price(final_price):
    if Membership_card == True:
         final_price = final_price - membership_discount
         return final_price
    else:
         final_price = final_price
         return final_price
print(final_price(90))