# This is line comment. 
''' This is 
multiline comment. '''


var1 = 12  
var2 = 'ajay' 
print(type(var1))
print("hi Today's date is ",var1,"my name is",var2)
# + is used to concatenate this substatements and type must be string - so here for var1 u cant use +
# , is used for seperator of this statements, and hv a space character - statements can be of any type
print(id(var1)) #id fun is used to get location of variable.
print(3*var1) #for integer multiplies value to thrice and for string prints thrice.
print(3*var2) 

# Range function
for i in range(2,5) :
    print('1 = ',i) #it prints no from 2-5 including 2 & excluding 5. in new line each
for i in range(2,12,4): #including 2 excluding 12 with update +4 after each iteration.
     print('2 = ',i)
for i in range(6) :
    print('3 = ',i) #it prints no from 0-5 
    

# Pass statement
#pass is null statement in python which is used to do nothing.
varp=[1,2,3]
for item in varp:
        pass  
print("without pass,when we don't write any code the program will throw an error.")


#Number system
v1=25
print(bin(v1)) #here in output 0b indicates that it is a binayr value.
print(oct(v1)) #here in output 0o indicates that it is a octal value.
print(hex(v1)) #here in output 0x indicates that it is a hexadecimal value.

# Swapping - 1]using temp var 2]using sum, diff function 3rd way available only in python- a,b=b,a
a,b=2,10
print('a = ',a,'b = ',b)
a,b=b,a
print('a = ',a,'b = ',b)


# function
def sum(n1=100,n2=200): #if u want to pass default values then provide this values.
    print('sum = ',n1+n2)
#def sum(n1=10): 
 #   print('10') 
 
# python doesn't support function overloading. It remembers latest function only.
# input function return string-and using this string will not produce sum, so convert input into integer
n1 = int(input("enter number 1 = "))
n2 = int(input("enter number 2 = "))
sum(n1,n2)
sum() #passing default values.


'''

#python doesn't support  direct method/constructor overloading.
# to achieve this some methods are their
# 1.using none keyword
class area:
    def findArea(self,a=None,b=None):
        if a!=None and b!=None: #findArea(a,b)
            print('Area of Triangle = ',(a*b))
        elif a!=None: #findArea(a)
            print('Area of Triangle = ',(a*a))
        else: #findArea()
            print('Area of Triangle = 0')
o1 = area()
o1.findArea()
o1.findArea(12)
o1.findArea(4,6)

#method 2-using dispatch method
from multipledispatch import dispatch
class product:
    @dispatch(int,int,int)
    def findProduct(self,l,b,h):
        print('volume = ',l*b*h)
    @dispatch(int,int)
    def findProduct(self,l,b):
        print('volume = ',l*b)
    @dispatch(int)
    def findProduct(self,l):
        print('volume = ',l)
    @dispatch()
    def findProduct(self):
        print('volume = 1')
o2 = product()
o2.findProduct()
o2.findProduct(13)
o2.findProduct(2,6)
o2.findProduct(3,4,5)
 

'''


