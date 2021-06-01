Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 17:00:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # lists,tuples and sets
>>> list_numbers=[20,30,40,49,50,60] #these can be changes ,they are mutable
>>> tuple_numbers(49,39,30,50,49) #these are immutabl they cannot be chnaged
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tuple_numbers(49,39,30,50,49) #these are immutabl they cannot be chnaged
NameError: name 'tuple_numbers' is not defined
>>> tuple_numbers=(49,39,30,50,49) #these are immutabl they cannot be chnaged
>>> 
>>> set_numbers={30,48,40,50,60,60,} #they are unique and not in oder
>>> 
>>> set_numbers={30,48,40,50,60,60} #they are unique and not in oder
>>> 
>>> print(set_numbers)
{40, 48, 50, 60, 30}
>>> print(tuple_numbers)
(49, 39, 30, 50, 49)
>>> print(list_numbers)
[20, 30, 40, 49, 50, 60]
>>> 
>>> # []These are lists, ()These are tuples {} these are sets
