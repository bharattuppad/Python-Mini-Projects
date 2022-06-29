#Bharat Tuppad
#pizza ordering system


print('----------------------------------------------------------')

print('Welcome to Mamma Mia Pizza store')
print('\n')
print('All pizza sizes are regular (10"). Following is our menu along with price per qty')

print('----------------------------------------------------------')

menu={'ID:1 > Margherita Pizza': 300.00, 'ID:2 > Chicken Sausage Pizza': 350.00, 'ID:3 > Fresh Veggie Pizza': 380.00, 'ID:4 > Cheese and Corn Pizza': 380.00, 'ID:5 > Mexican Green Wave Pizza': 349.00, 'ID:6 > Peppy Paneer Pizza': 460.00,'ID:7 > Non Veg Loaded Pizza': 389.00, 'ID:8 > Paneer Loaded Garlic Bread': 189.00,'ID:9 > Pepsi 650ml': 50.00,'ID:10 > Tomato Ketchup Sachet': 2.00}
item_link={1:'Margherita Pizza', 2:'Chicken Sausage Pizza', 3:'Fresh Veggie Pizza', 4:'Cheese and Corn Pizza', 5:'Mexican Green Wave Pizza', 6:'Peppy Paneer Pizza', 7:'Non Veg Loaded Pizza', 8:'Paneer Loaded Garlic Bread', 9:'Pepsi 650ml',10:'Tomato Ketchup Sachet'}
money_link={1:300, 2:350,3:380, 4:380, 5:349, 6:460, 7:389, 8:189, 9:50, 10:2}

d=list() #saves pizza id
e=list() #saves qty
f=list() #saves total price of given qty

while True:

        
    print(menu)
    print('\n')
    print('--------------------------------------------------------------------')
    a=int(input("enter the ID number of pizza u want: "))

    
    d.append(a)
    h=len(d)
    
    
    b=int(input("enter the qty of that item: "))
    
    
    e.append(b)
    
    bill=(money_link.get(a))*b

    
    f.append(bill)
    
    print("",item_link.get(a)," QTY: ",b," Cost: ",bill," Rupees\n")
    
    c=input('do u want to order another item, Press Y for yes and N for no: \n')

    if c.upper()=='Y':
        True

    else:
        break


print('Your order is: \n')

for i in range(h):
    print('Item: ',item_link.get(d[i]),'--- QTY:',e[i],'--- Cost: ',f[i],end='')
    print('\n')
    i=i+1

cost=sum(f)

print("Bill before taxes: ",cost," Rupees")

partial_bill=(cost)+((cost)*.025)+((cost)*.025)+((cost)*.05)

print("Taxes as Applicable: \n")
print("CGST: 2.5%")
print("SGST: 2.5%")
print("Service Tax: 5% \n")

print("bill after taxes: ",partial_bill," Rupees\n")

if partial_bill<500:
    print("Delivery charges applicable: 50 Rupees\n")
    
    payable_bill=(partial_bill)+50
    print('=======================================================')
    print("Bill payable is: ",int(payable_bill)," Rupees")
    print('=======================================================')
    
else:
    print("Delivery charges not applicable")
    print('\n')
    payable_bill=partial_bill
    print('=======================================================')
    print("Bill payable is: ",int(payable_bill)," Rupees")
    print('=======================================================')


print('------------------------------------------------------------------------')
print('|  Thank you for visiting us. Hope you will love our pizza.            |')
print('|  We are new and open to suggestions and feedback.                    |')
print('|  Feel free to reach out to us at mmpizzastore@gmail.com              |')
print('|  Our other Social handles are:                                       |')
print('|  FB: MMPizzaOfficial                                                 |')
print('|  Insta: MMPizzaOfficial                                              |')
print('------------------------------------------------------------------------')




































