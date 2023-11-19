class person:
    def __init__(self,a,b,c):
        self.fname = a
        self.lname = b
        self.age = c
    def __str__(self):
        return self.fname+" "+self.lname+' '+str(self.age)#to concatenate a string with no-convert no to string
class employee(person):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.id = d
    def __str__(self):
        return super().__str__()+' '+str(self.id)
a = person('Ajay','Gupta',22)    
b = employee('Rahul','Chaubey',18,101)   
#to print directly passing object we have to define inbuilt display fun- __str__ 
print(a) 
print(b)

    