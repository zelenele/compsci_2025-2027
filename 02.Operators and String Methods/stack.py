import random

Stack = []
def Stackpop():
   Stack.pop()
def Pushstack(value):
    Stack.append(value)
while len(Stack) != 10:
    Randomizer = random.randint(1,1000)
    Pushstack(Randomizer)


print(Stack)