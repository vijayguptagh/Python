# File Input/Output
# writing a file
#ref is ref var that points to newfile in memory & through this ref var we called write method.
ref = open('file.txt','w')
data = ref.write("My name is Python.")
data = ref.write('\nLearn Python One Video in Hindi:')
data = ref.write('\n13 Python chapters and 3 Python Projects.')
ref.close()

#mode = 'a' will append content at end of file.
""" ref = open('file.txt','a')
data = ref.write("Python is easy programming language.")
ref.close() """

#Reading a file
ref = open('file.txt','r')
data = ref.read()
print(data)
ref.close()

#note that for each different type operation u have to seperately open & close file.
ref = open('file.txt','r')
newdata1 = ref.read(5) #reading 1st 5 characters
print(newdata1)

ref = open('file.txt','r')    
newdata2 = ref.readline() #reading 1st line.
print(newdata2) #after print statement a empty line also prints bcz newline method contains \n
ref.close() #ref is ref var that points to file.if in 2nd statement we use ref var for storing value readed by file then in further we can't access the file.so use another var for storing data.

# with statement = no need to close file.
with open('anotherfile.txt','r') as f:
    a = f.read()
    print('value of anotherfile.txt = ',a)