# Problem Statement: A class with 10 students wants to produce some information from the results of the four standard 
# tests in Maths, Science, English and IT. Each test is out of 100 marks. The information output 
# should be the highest, lowest and average mark for each test and the highest, lowest and average 
# mark overall. Write a program in Python to complete this task. 

maths = []
science = []
english = []
it = []

for i in range(10):
    print("Enter detail of student ", i+1, ":")
    a=float(input("Enter marks in Maths: "))
    maths.append(a)
    a=float(input("Enter marks in Science: "))
    science.append(a)
    a=float(input("Enter marks in English: "))
    english.append(a)
    a=float(input("Enter marks in IT: "))
    it.append(a)

h = max(maths)
l=min(maths)
avg=sum(maths)/len(maths)

print("Highest marks in maths = ",h)
print("Lowest marks in maths = ",l)
print("Average marks in maths = ",avg)

h=max(science)
l=min(science)
avg=sum(science)/len(science)

print("Highest marks in science = ",h)
print("Lowest marks in science = ",l)
print("Average marks in science = ",avg)

h=max(english)
l=min(english)
avg=sum(english)/len(english)

print("Highest marks in english = ",h)
print("Lowest marks in english = ",l)
print("Average marks in english = ",avg)

h=max(it)
l=min(it)
avg=sum(it)/len(it)

print("Highest marks in it = ",h)
print("Lowest marks in it = ",l)
print("Average marks in it = ",avg)
