import random


# Yogurt = input("how many yogurts do you want?")
# print(int(Yogurt))
# for x in range (int(Yogurt)):
#     print(f"You have {x} yogurts in your basket adding one more")
#     x += 1
# print(f"You have {Yogurt} yogurts in your basket") 
seth_curry = True

choice = [1,2,3,4,5,6,7,8,9,10]
gamble = random.choice(choice)
while seth_curry == True:
    
    if gamble == 1 :
        Seth_curry = True
        print ("Seth curry is the best player in the NBA")
        break
    
    else:
        Seth_curry = False
        print("Seth curry is the worst player in the NBA")
        break



    