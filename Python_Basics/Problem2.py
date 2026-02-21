# Problem Statement: Write a Python Program to input basic salary of an employee and calculate its Gross salary 
# according to following: 
# Basic Salary <= 10000 : HRA = 20%, DA = 80% 
# Basic Salary <= 20000 : HRA = 25%, DA = 90% 
# Basic Salary > 20000 : HRA = 30%, DA = 95%. 

base=int(input("Enter Base salary: "))
if base<=10000:
    hra=20/100*base
    da=80/100*base
elif base<=20000:
    hra=25/100*base
    da=90/100*base
else:
    hra=30/100*base
    da=95/100*base

gross = float(base) + da + hra
print("Your gross salary is : ",gross,"\n")
