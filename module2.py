# Modules in Python - used to reuse class,method,var
#Defining userdefined modules
# filename is modulname

# way 1:importing module & accessing methods by dot
import module1
print('Sum of no 3 & 5 are ',module1.sum(3,5))

#importing all methods of module & accesing directly
from module1 import *
print('Sum of no 13 & 7 are ',sum(13,7))

# method 3-importing a specific method 
from module1 import prod
print('Product of no 3 & 5 are ',prod(3,5))

#method 4-accessing module with diff name
import module1 as m
print('Sum of no 23 & 15 are ',m.sum(23,15))
