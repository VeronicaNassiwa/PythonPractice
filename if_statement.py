# IS STATEMENTS IN PYTHON
cars_in_bond=["benz","spacio","jeep","raum"]

customers_choice=input("enter a car of your choice")

if customers_choice in cars_in_bond:
    print("{} is available" .format(customers_choice) ) 
 
else:
    print("{}  is not available" .format(customers_choice))     
    