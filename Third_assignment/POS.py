listOfItems=[]
def MainMenu():
    choice=0
    while choice !=1 and choice !=2:
        print("Enter:")
        print("""
            1- To start a new order
            2- To close the program
            """)
        choice=int(input(""))
        if choice==1:
            print("Enter:")
            print("""
                1- To add a new item.
                2- To check the total of the bill
                3- To delete an item from your list.
                4- To add a coupon
                5- To checkout.
                """)
        elif choice==2:
            print("bye bye!")
        else:
            print("invalid value, please enter 1 or 2!")
MainMenu()