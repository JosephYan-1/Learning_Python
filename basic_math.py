#this program will do 
#div, add, sub, mult
#remainders 
#factorials
import math 

arr = [] #will be used for factorials 

a = 1
b = 2

c = a + b #add
print("A+B=",c) #print 3

c -= a #sub
print("C-A=",c) # print 2

if (c == b): #just doiing bool test
    print("C and B are equal")

c *= b #mult
print (c) #prints 4

print("C/B=",c // b) #prints 2 (// is floor, / is floating point)


#basic arithmetic is done

#remainder

print("C%3=", c % 3) #should print 1

#factorial using b and c

b = 0
c = 1
while b <= 7: #will possibly make a function out of this in the future
    if (b != 0 and b != 1):
        c = (c * b)
    print(f"{b}!= {c}")
    b+=1