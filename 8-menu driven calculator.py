#menu driven calculator

a=int(input("enter the 1st no: "))
b=int(input("enter the 2nd no: "))

print("------------------")

print("following are the available operations")
print("press 1 for addition and hit enter")
print("press 2 for subtraction and hit enter")
print("press 3 for multiplication and hit enter")
print("press 4 for division and hit enter")
print("press 5 for floor division and hit enter")
print("press 6 for exponent and hit enter")

print("------------------")

c=int(input("enter the code of operation: "))

print("------------------")

if c==1:
    add=a+b
    print("Ans = ",add)
elif c==2:
    sub=a-b
    print("Ans = ",sub)
elif c==3:
    mul=a*b
    print("Ans = ",mul)
elif c==4:
    divsn=a/b
    print("Ans = ",divsn)
elif c==5:
    fdiv=a//b
    print("Ans = ",fdiv)
elif c==6:
    power=a**b
    print("Ans = ",power)
else:
    print("invalid code")

