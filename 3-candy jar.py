#Bharat Tuppad
a=100

print("well well well.. .hello there... ")

print("Welcome to Willy Wonka's Crazy Candies")

while True:

    print("---------------------------------------------------------------------------")
    
    b=int(input("how many candies do u want ?"))
    
    if b<a:
        print("So u need: ", b," candies")
        print("Here is your packet filled with: ", b," candies")
        print("Thank you for shopping with us.. come next time too")
        a=a-b

    elif b==a:
        print("That is all we got for today")
        print("Here is your packet filled with: ",b," candies")
        print("Thank you for shopping with us..")
        print("All candies sold out.. good day....new stock comes tomo")
        break

    else:
        print("Well, we would love to give that many, but right now we have only: ",a," candies")
        print("So tell me, how much do you want")
        break


