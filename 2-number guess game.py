#Bharat Tuppad
#guess the number

import random

a=random.randint(0,99)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("Welcome to Jack Sparrow's Number guessing game")

print("well, the rules are simple mate:")

print("========================================================")

print("RULE NO 1: the number lies between 0 to 99")

print("RULE NO 2: Now i may be cruel, but, i am gonna go easy on you, you can have as many attempts as you want my friend")

print("RULE NO 3: ummmm.... i dont remember.. okay .. enough with the rules.. lets playyyyy....")

print("*********************************************************")

while True:

    b=int(input("come on mate, guess the number: "))

    if b<a:
        print("ooooo.... that was low..go a little higher")
        
    elif b>a:
        print("you went too high mate... you better not be on something fishy..go a little lower")

    else:
        break
        

print("BINGOOOOO... you did hit the bulls eye mate")

print("GAME OVER... Thanks for playing")   


