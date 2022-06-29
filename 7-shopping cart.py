#Shopping cart experience

b=[]     #global variable
k=0      #k=0 -> no item in list.. #k=1 -> items present in the list
m=0
#individual functions

def cart_welcome():     #used for welcoming the user
    print('\nwelcome to BB Shopping world... one stop solution for all your shopping needs..\n')

def cart_list():        #used for displaying basic commmands
    print('---------------------------------------------------------------------------------------')
    print('here is our list of commands needed for operating the cart')
    print('--------------------------------------------------------------------------------------- \n')
    print('1. Add an item to the cart\n')
    print('2. Remove an item from the cart\n')
    print('3. Clear the whole cart\n')
    print('4. Show the items in the cart\n')
    print('5. Proceed to payment and ordering\n')
    print('6. Quit the shopping spree')
    print('--------------------------------------------------------------------------------------- \n')
    

def cart_add():         #used for adding items to the list
    a=int(input('for adding an item to the list, just enter the item number'))
    b.append(a)
    print('item number added successfully\n')
    print('--------------------------------------------------------------------------------------- \n')

def cart_remove():      #used for removing items from the list
    c=int(input('for removing an item from the list, just enter the item number'))
    b.remove(c)
    print('item number removed successfully\n')
    print('--------------------------------------------------------------------------------------- \n')

def cart_clear():       #used to clear the cart list
    print('this command is used for clearing the entire cart list')
    d.clear()
    print('cart list cleared successfully\n')
    print('--------------------------------------------------------------------------------------- \n')

def cart_show():        #used to display the cart list
    print('here is the list of items currently present in your cart: ',b)
    print('--------------------------------------------------------------------------------------- \n')

def cart_payment():     #used to proceed to payment page
    
    if len(b)==0:
        print('cannot proceed to payment page as list is empty... kindly use the commands and add items before proceeding to payment page')

    else:
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('you have opted for payment page.. \n')
        print('payment page is loading..\n')
        print('do not press any key, do not go back and do not click on refresh..\n')
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        print('\nenter your personal details: \n')
        f=input('enter your name: ')
        g=input('\nenter your address: ')
        h=input('\nenter your mobile number: ')
        i=input('\nenter your email id: ')
        print('\n ---------------------------------------------------------------------------------------')
        print('At present we do not offer online payment.. we accept cards offlie and COD..\n')
        print('rest assured, your order has been placed.... your items will be delivered in 2-3 days')
        print('thank you for choosing BB Shopping world..')
        print('\n ---------------------------------------------------------------------------------------')
        k=1
        
def cart_quit():        #used to quit the shopping spree

    if k==0:
        print('---------------------------------------------------------------------------------------')
        print('Hie..  sorry to see you go away without placing an order.. \n')
        l=input('We are new to this business and it would be helpful if you can give some feedback wherever you felt any sort of shortcomings from our end: ')
        print('\nthank you for your valuable feedback.. ')
        print('\nwe would love to see you soon on our platform .. ')
        print('---------------------------------------------------------------------------------------')

    elif k==1:
        print('---------------------------------------------------------------------------------------')
        print('Thank you for shopping with us \n')
        m=input('We are new to this business and it would be helpful if you can give some feedback wherever you felt any sort of shortcomings from our end: ')
        print('\nthank you for your valuable feedback.. ')
        print('\nwe would love to see you soon on our platform .. ')
        print('---------------------------------------------------------------------------------------')
              


#Amalgamation of functions

def bbsw():

    cart_welcome()

    cart_list()

    while True:
    
        m=int(input('Enter the code of operation: '))

        if m==1:

            cart_add()

        elif m==2:

            cart_remove()

        elif m==3:

            cart_clear()

        elif m==4:

            cart_show()

        elif m==5:

            cart_payment()

        elif m==6:

            cart_quit()
            
        else:
            print('invalid entry... enter the correct operation code')
            return True

        

#OP-

bbsw()
