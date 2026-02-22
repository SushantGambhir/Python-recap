import Python_Basics.Problem07A as Problem07A

p=float(input("Enter the amount: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the number of years: "))

interest= Problem07A.compound(p,r,t)

print("Compound Interest = ",interest)
