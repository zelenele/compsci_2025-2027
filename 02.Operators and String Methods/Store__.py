   

def membership_discount(price):
     membership_discount_value= price * 0.2
     return membership_discount_value

def Membership_card(Membershipp_card):
     if Membershipp566565_card == True:
          return True
     else:
          return False

def final_price(New_price, Membershipp_card):
     if Membershipp_card == True:
          New_price = price - membership_discount(price)
          return New_price
     else:
          
          return final_price

   
     
price = float(input("Enter the price of your shopping: "))
Membershipp_card = Membership_card(bool(int(input("Do you have a membership card? (1 for yes, 0 for no): "))))
membership_discount = membership_discount(price)
final_price = final_price(price, Membershipp_card)
print("Your final price is: ", final_price())