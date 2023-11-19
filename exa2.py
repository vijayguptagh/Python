
# String Funcions
var2 = 'advertisement is key value'
print('1 = '+var2[3:8]) # [a:b] means include a & exclude b  #in py +/, both can be used.
print('2 = '+var2[:4]) #[:b] = [0:b] & [a:] = [a:lastIndex]
print('3 = '+var2[2:10:3]) #[a:b:c] means print[a:b] with skip each cth value.means here vertiseme-skip each 3rd = means index 2+print each 3rd value after this.
print('4 = ',len(var2)) 
print('5 = ',var2.endswith('ment')) 
print('6 = ',var2.count('t'))
print('7 = ',var2.capitalize())#it capitalizes the 1st letter of each word but doesn't saves changes to actual string.
print('8 = ',var2.find('key')) #it find 1st occurence of string & gives its index(index of 1st letter)
print('9 = ',var2.find('key',18)) #this will find index of is while searching wrt index 10.
#var2.index('a' is same as find method only diff is that when string not getted in find it will return -1 & index will through error.
print('10 = ',var2.replace('is','are'))
print('11 = ',var2) #changes not saved in var.To save changes in var do this 
var2 = var2.replace('is','are')
print('12 = ',var2) 

var3='nayan123'
print(var3.isalpha()) #return true if string consist of all alphabets(no special char,space,underscore)
print(var3.isdigit()) #returns true if string consist of digits only.(no special char,space,underscore)
print(var3.isalnum()) #return true if string consist digit or alphabet or both.(no special char,space,underscore)
#finding asci & char value-can pass only 1char
print(chr(89))
print(ord('a'))
#converting string to list
#each word(seperated by spaces) is converted into list element.

print(var2.split())

# List
list = [1,2,3,4,5]
list.append(60);    print('1 = ',list) # adds value at end
#to add multiple statements in 1line u must have to use ; else u will get error.
list.insert(2,20);  print('2 = ',list) #note that try to print after fun use seperately else u will get none bcz some fun doesn't return actual list after operation.
 #insert value at index a
list.remove(1); print('3 = ',list) #deletes this value from list
list.pop(); print('4 = ',list) #deletes value at index
list.pop(2);    print('5 = ',list) 
del(list[1:3]); print('6 = ',list)  #deletes values from index 1inclusive to 3exclusive
#changes are saved into list & in string,tuple,list these changes are not saved bcz they are nonmutable.
list.extend([101,102,103]); print('7 = ',list)  #insert this values at end of list(note : inside [ ] )
list.reverse(); print('8 = ',list)  
# print(list.clear()) #to empty list
#for homogenous below fun defined
list.sort(); print(list)
print(sorted(list))
print(len(list))
print(sum(list))
# print(min(list))
# print(max(list)) 


# Tuple
tuple = (1,"aj")
print(tuple)
# tuple[0]=22 #it gives error bcz tuple, can't alter.
#tuple with single value 
t1 = (1);   print(t1) #wrong way to define bcz 1 directly prints
t2 = (1,);   print(t2)


# Dictionary
dic = {
    101:"Vijay",
    "Python":"A fast programming language",
    "CN":[2,5,9],
    "2nd":{'harry':"coder", "Traversy":"channel", "yourAge":20}
}
print(dic)
print(dic["2nd"]) #it prints value corresponding to key = 2nd
#since list is mutable so we can update list values. 
dic["CN"] = [1];    print(dic["CN"]);   print(dic)
dic['xyz'] = 'xyz'#if dic doesn't contain this key then it adds this value.
print(dic)
#dic keys %& values
print(dic.keys())
print(dic.values())
print(type(dic.values())) #type is class dict_values
print(type(dic.keys())) #type is class dict_keys
print(dic.items())#it prints (key,value) pair
print(dic.update({'friend':'Raza','Class':'SE'})) #this doesn't works. so try to print seperately
dic.update({'friend':'Raza','Class':'SE'}) #in dictionary duplicate keys not allowed.When duplicate keys used it will throw error.
print(dic)

#.get & []
print(dic.get("CN"))
print(dic["CN"]) #here both gives value associated with key.but diff lies is that when we pass wrong key .get will print none & [] will throw error.
print(dic.get("CNND"))
# print(dic["CNND"])

# Zip function
# Dictionary of lists
list1 = [1,2,3,4,5,6]
list2 = ['a','b','c','d']
d = dict(zip(list1,list2)) #a dictionary with key till 4 created.
print(d)
# 1.to iterate for loop using 2 var
l1=[1,2,3,4]
l2=[100,200,300,400,500,600]
for a,b in zip(l1,l2):
    print(a,b) #zip fun ignores values that doesn't form pair. Means here 500,600 of l2 not prints.

 
# Set
s1 = {1,2,3,4,5,6}
#s1.add({100});  print(s1) #this gives error bcz defined set can't be updated.We can overrite & not update in set,tuple.
#s1.clear() #it makes set s1 empty
s1.remove(3);   print(s1)
s1.pop();   print(s1) #pop fun doesn't take arguments & removes arbitrary element from set.
print(s1.union({11,12,13})) #union fun returns a new set with all items from both sets.
print(s1.intersection({3,4})) #union fun returns a new set which have common items from both sets.


