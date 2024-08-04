
# 2 types of error = syntax & logical error
#syntax error can't be handled but logical error can be handled
""" 
# ZeroDivisionError
a=10
print(a/0)
# NameError
print(b) #var b not defined
# TypeError
print('10'+10) #concatenes b/w same types allowed.
# ValueError
c=int('buffer')
#IndexError
l=[1,2,3]
print(l[5]) #accessing index that is not available in list.
#KeyError
d={'name':'vijay',2:'saket'}
print(5) #passing wrong key
#ModuleNotFoundError
#ImportError 
"""
# Handling Exception = try block-code which can cause exception.except block-runs when exception occurs.
try: print(10/0)
except Exception as e: print(e)

#try else block. else is executed only if try was successful.
