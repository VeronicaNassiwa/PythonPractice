def multiplying(num1,num2):
    return num1* num2

anser =multiplying(4,7)
#print(anser) 

grade_list=[40,50,90,60,]
grade_tuple=(50,70,80,90)
grade_set={40,60,20,100}
grade_set2={40,60,30,70,100}

#advanced set operations
#print(grade_set.intersection(grade_set2))
#print(grade_set.union(grade_set2))
#print(grade_set.difference(grade_set2))

#adding values to list,tuples and sets
#grade_list.append(71)
#grade_tuple=grade_tuple + (71,)
#grade_set.add (71)
#print(grade_set)

#list comprehension
print([x for x in range(10)])

#loops (for loop and if statement)
my_variable="myhussein"
for character in my_variable:
        #print(character)                                    
        
#if statement

    my_bond = {"benz","spacio","lambogin","rangerover"}
customer_choice = input("Enter a car of your choice")
if customer_choice in my_bond:
    #print("{} is availabe".format(customer_choice))

#else:
    #print("{}is not available".format(customer_choice))        