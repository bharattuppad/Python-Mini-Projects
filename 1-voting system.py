#Bharat Tuppad
#vote counting system

print("Welcome to 2024 Elections !!!")

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

print("Enter T for Mr Trump or Enter B for Mr Biden or Enter Q to end and display the result")
Tcount=0
Bcount=0

while(True):
    a=input("Enter the code for the candidate you want to vote for: ")

    if a.upper()=='T':
        Tcount=Tcount+1

    elif a.upper()=='B':
        Bcount=Bcount+1

    elif a.upper()=='Q':
        print("The voting ends")
        break

    else:
        print("Invalid entry")

print("=============================================================")

print("The election has ended. Mr Trump has received: ", Tcount ," votes")

print("The election has ended. Mr Biden has received: ", Bcount ," votes")
      
print("=============================================================")

if Tcount>Bcount:
    diff=Tcount-Bcount
    print("Mr Trump has won by: ", diff," votes")

elif Bcount>Tcount:
    diff=Bcount-Tcount
    print("Mr Biden has won by: ", diff," votes")

else:
    print("It's a draw...")



