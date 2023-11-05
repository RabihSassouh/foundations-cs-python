quantity=0
finalBill=0
FinalList=['0']
#coupon=0
#NewOrder
def NewOrder():
    listOfItems=[]
#coupon=0
    bill=0
    order=True
    while order ==True:
        print("""Enter:
            1- To add a new item.
            2- To check the total of the bill
            3- To delete an item from your list.
            4- To add a coupon
            5- To checkout.
            """)
        choice=int(input(""))
        if choice==1:
            print("""Choose the item you want to add:
                1- Tomato * 1 kg for 2$ *
                2- Orange * 1 kg for 3$ *
                3- Potato * 1 kg for 1$ *
                4- Carrot * 1 kg for 1.5$ *
                5- Banana * 1 kg for 2.5$ *
                6- Olive * 1 kg for 4$ *
                """)
            choice=int(input(""))
            quantity=int(input("please enter the quantity you want to buy in kg: "))

            if choice==1:
                bill=bill + 2*quantity
                listOfItems=listOfItems+[str(quantity) + " kg of tomato"]
                print(listOfItems)
                print(bill)
            elif choice==2:
                bill=bill + 3*quantity
                print(bill)
                listOfItems=listOfItems+[str(quantity) + " kg of orange"]
                print(listOfItems)
            elif choice==3:
                bill=bill + quantity
                listOfItems=listOfItems+[str(quantity) + " kg of potato"]
                print(listOfItems)
                print(bill)
            elif choice==4:
                bill=bill + 1.5*quantity
                listOfItems=listOfItems+[str(quantity) + " kg of carrot"]
                print(listOfItems)
                print(bill)
            elif choice==5:
                bill=bill + 2.5*quantity
                listOfItems=listOfItems+[str(quantity) + " kg of banana"]
                print(listOfItems)
                print(bill)
            elif choice==6:
                bill=bill + 4*quantity
                listOfItems=listOfItems+[str(quantity) + " kg of olive"]
                print(listOfItems)
                print(bill)
            else:
                print("invalid input!")
            
#Main menu
def MainMenu():
    choice=0
    while choice !=2:        
        print("""Enter:
        1- To start a new order
        2- To close the program
        """)
        choice=int(input(""))
        if choice==1:
            NewOrder()
        elif choice==2:
            print("bye bye!")
        else:
            print("invalid value, please enter 1 or 2!")
MainMenu()
#NewOrder()

    
    
'''
    print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)

    print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
    print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
    print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)

#New order
def NewOrder():
        
            print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
            NewOrder()
    elif choice==2:
        print("your total bill is: ", bill)
        print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
        NewOrder()
    elif choice==3:
        print("choose the item you want to delete: ",listOfItems)
        delete=input("")
        print("your item has been deleted.")
        print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
        NewOrder()
    elif choice==4:
        print("please enter the value of your coupon: ")
        coupon=input("")
        print("the value of your coupon will be discounted from your final bill.")
        print("""Enter:
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
        NewOrder()
    elif choice==5:
        print("your bought items:",listOfItems)
        print("your total bill without any coupon is: ",bill)
        print("the total of your coupons is: ",coupon)
        print("your final bill is: ", finalBill)
        MainMenu()
    else:
        print("invalid input!")
        NewOrder()'''
#MainMenu()
#NewOrder()