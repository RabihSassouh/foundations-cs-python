cities=["beirut","saida","batroun","zgharta","aley","zahle"]
drivers=["alex","rawad","jhony","mohamad"]
#the function that will add a city to the list of cities.
#O(len(cities))
def add_city():
    print("Please enter the name of the city you want to add: ") #O(1)
    city=input("")
    if city not in cities:      #O(len(cities))
        cities.append(city)     #O(1)
    else:
        print("The city you entered already exists in the list!") #O(1)
    print(cities)       #O(1)

#
def add_driver():
    print("Please enter the first and last name of the driver you want to add: ")
    driver=input("")
    if driver not in drivers:
        drivers.append(driver)
    else:
        print("The driver you entered is already a part of our community!")
    print(drivers)

#the function that will run the main page.
#
def main():
    user_input=0
    while user_input !=7:
        print("""Enter:
            1- To add a city to the list of cities.
            2- To add a driver to the list of drivers.
            3- To add a city to the route of a driver.
            4- To remove a city from a driver's route.
            5- To remove a driver from list of drivers.
            6- To check the deliverablity of a package.
            7- To close the program.""")
        user_input=int(input(""))
        if user_input==1:
            add_city()
        elif user_input==2:
            add_driver()
        # elif user_input==3:
        #     add_route()
        # elif user_input==4:
        #     remove_city()
        # elif user_input==5:
        #     remove_driver()
        # elif user_input==6:
        #     check_deliver()
        elif user_input==7:
            print("closing the program!...")
        else:
            print("Invalid input, please enter a number between 1 and 6")
main()        