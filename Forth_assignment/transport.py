cities=["beirut","saida","batroun","zgharta","aley","zahle","sour","tripoli","akkar"]
drivers=[{'name':'alex','route':['beirut','saida','sour']},
{'name': 'rawad','route':['beirut','aley','zahle']},
{'name': 'jhony', 'route': ['beirut','batroun','zgharta']},
{'name':'mohamad', 'route' : ['zgharta','tripoli','akkar']}]

print(drivers)
# #the function that validate if a city is valid.
# def check_city():
#     city=input("")
#     city=city.lower()
#     city_list=[city]
#     if len(city)>58:
#         print("Please enter a valid city name!")
#         return
#     for i in range (len(city_list)):
#         if city_list[i].isalpha() or city_list[i]==" ":
#             if city not in cities:      #O(len(cities))
#                 cities.append(city)     #O(1)  
#                 return
#             # else:
#             #     print("The city you entered already exists in the list!") #O(1)
#             #     print(cities)  
#             #     return
#         else: 
#             print("Please enter a valid city name!")
#             return

#the function that will add a city to the list of cities.
#O(len(cities))
def add_city():
    print("Please enter the name of the city you want to add: ") #O(1)
    city=input("")
    city=city.lower()
    city_list=[city]
    if len(city)>58:
        print("Please enter a valid city name!")
        return
    for i in range (len(city_list)): #O(len(cities))
        if city_list[i].isalpha() or city_list[i]==" ": #O(len(cities))
            if city not in cities:      #O(len(cities))
                cities.append(city)     #O(1)
                print(cities)           #O(1)
                return
            else:
                print("The city you entered already exists in the list!") #O(1)
                print(cities)  
                return
        else: 
            print("Please enter a valid city name!")
            return

#the function that will add a new driver to the list of drivers.
def add_driver():
    print("Please enter the name of the driver you want to add: ")
    driver=input("")
    for i in range (len(drivers)):
        if drivers[i]['name']!=driver:
            print("Please enter the cities you want to add to",driver,"route separated by a coma ',': ")
            new_route=input("")
            new_route=new_route.lower()
            new_route=[new_route]
            for i in new_route:
                new_route=i.split(',')
                for j in range (len(new_route)):
                    if new_route[j].isalpha() or new_route[j]==" ":
                        if new_route[j] not in cities:
                            cities.append(new_route[j])
                    else:
                        print("Please enter a valid city name!")
        else:
            print("The driver you entered is already a part of our community!")
            return
            
        dic={'name':driver, 'route':new_route}
        drivers.append(dic)
        print(cities)
        print(drivers)
        return
    

#
def add_route():
    print("Please enter the name of the driver that you want to add a city to his route: ")
    driver=input("")
    for i in range (len(drivers)):
        if driver in drivers[i]['name']:
            print("Please enter the name of the city that you want to add to this driver's route: ")
            new_city=input("")
            new_city=new_city.lower()
            city_list=[new_city]
            if len(city_list)>58:
                print("Please enter a valid city name!")
                
            else:
                for i in range (len(city_list)): #O(len(cities))
                    if city_list[i].isalpha() or city_list[i]==" ": 
                        if new_city not in cities: #O(len(cities))
                            cities.append(new_city)     #O(1)
                            print(cities)           #O(1)
                            if new_city not in drivers[i]['route']:
                                drivers[i]['route'].append(new_city)
                                print(drivers)
                                return
                            else:
                                print("the name of the city that you entered is already on this driver's route.")
                                return
                    else: 
                        print("Please enter a valid city name!")
                        return
        else:
            print("The driver's name you enter is not available in our driver's list.")
            return    
    
# #
def remove_city():
    print("Please enter the name of the driver that you want to remove a city from his route: ")
    driver=input("")
    for i in range (len(drivers)):
        if drivers[i]['name'] != driver:
            print("The driver's name you enter is not available in our driver's list.")
            return
        else:
            print("Please enter the name of the city that you want to remove from",driver,"route.")
            delete_city=input("")       
            if delete_city not in drivers[i]['route']:
                print("The city you entered is already not in the route of ",driver)
                return
            else:
                drivers[i]['route'].remove(delete_city)
                print(drivers)
                return
            
# #
def remove_driver():
    print("Please enter the name of the driver who you want to remove from the list of drivers.")
    delete_driver=input("")
    for i in range (len(drivers)):
        if drivers[i]['name'] != delete_driver:
            print("The name you entered is not a driver in our company.")
            return
        else:
            del drivers[i]
            print(drivers)
            return

#
def check_deliver():
    print("Please enter the name of the city that you want to check who delivers to it: ")
    deliver=input("")
    if deliver not in cities:
        print("We are sorry, the city you enter is not in any of our routes.")
    else:
        print("The driver(s) who reach",deliver,"is/are: ")
        for i in range (len(drivers)):
            if deliver in drivers[i]['route']:
                print(drivers[i]['name'])
                
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
        elif user_input==3:
            add_route()
        elif user_input==4:
            remove_city()
        elif user_input==5:
            remove_driver()
        elif user_input==6:
            check_deliver()
        elif user_input==7:
            print("closing the program!...")
        else:
            print("Invalid input, please enter a number between 1 and 6")
main()        