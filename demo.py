'''
print("hello world")

def fibo(n):

    if (n<=1 ):
        return n

    return fibo (n-1) + fibo (n-2) 
x= int(input())
for i in range(x):
    print(fibo(i))
'''
'''
import numpy as np 

a= np.random.random_sample((4,4))
print(a)

b=np.arange(20)
print (b)
'''
def number(n):

    c=0
    while ( n !=0):
        n=n//10
        c=c+1
    return c

print (number(52))

