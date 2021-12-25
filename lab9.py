#Write a Python program to create the colon of a tuple.
from copy import deepcopy
tuple = ("a", 'e', []) 
tupleColon = deepcopy(tuple)
tupleColon[2].append(50)
print(tupleColon)