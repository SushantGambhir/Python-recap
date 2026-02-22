# 1. Write a function which takes principal amount, interest rate and time. This function returns 
# compound interest. Call this function to print the output. 
# 2. Save this function (as a module) in a python file and call it in another python file.   

def compound(amt,rate,time):
    ci=amt*(1+rate/100)**time-amt
    return ci

p=float(input("Enter the amount: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the number of years: "))

interest=compound(p,r,t)

print("Compound Interest = ",interest)
