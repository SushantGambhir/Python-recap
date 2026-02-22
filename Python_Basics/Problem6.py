# Create a list of 100 random numbers between 100 and 900. Count and print the:  
# 1. All odd numbers 
# 2. All even numbers 
# 3. All prime numbers 

import random
import math

n=[]

for i in range(100):
    n.append(random.randint(100,900))
    
print("\nOdd numbers: \n")
odd=0
for i in n:
    if(i%2!=0):
        print(i)
        odd+=1
print("Number of odd numbers = ",odd)

print("\nEven numbers: \n")
even=0
for i in n:
    if(i%2==0):
        print(i)
        even+=1
print("Number of even numbers = ",even)

print("\nPrime Numbers: \n")
prime=0
for i in n:
    for j in range(2, int(math.sqrt(i)+1)):
        f=0
        if i%j==0:
            f=1
            break
    if f==0:
        print(i)
        prime+=1
print("Number of prime numbers = ",prime)
