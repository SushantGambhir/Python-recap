import Problem7A

p=float(input("Enter the amount: "))
r=float(input("Enter the rate: "))
t=float(input("Enter the number of years: "))

interest= Problem7A.compound(p,r,t)

print("Compound Interest = ",interest)
