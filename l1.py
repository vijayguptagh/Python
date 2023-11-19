lowerRange = int(input('Enter lower value = '))
upperRange = int(input('enter higher value = '))
#sinxce all inputs are string ins python that means in loop we have to convert this string to int in order to do i++
for i in range(lowerRange,upperRange):
    if(i%2 == 1) :
        print('odd no is ',i)
    if(i%2 == 0):
        print('even no is ',i)
    i = i+1

