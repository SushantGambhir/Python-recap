# D is a dictionary defined as D= {1:”One”, 2:”Two”, 3:”Three”, 4: “Four”, 5:”Five”}. 
# Write programs to
# 1. Add new entry in D; key=6 and value is “Six” 
# 2. Remove key=2. 
# 3. Check if 6 key is present in D. 
# 4. Count the number of elements present in D. 
# 5. Add all the values present D. 

d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
d[6]="Six"
print(d)

d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
d[6]="Six"
a=d.pop(2)
print(d)

d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
d[6]="Six"
a=d.pop(2)
if 6 in d.keys():
    print("Key value 6 present with the value ",d[6])
else:
    print("Not Present")
print(d)

d={1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
print("Total number of elements present in the dictionory are ",len(d))
print("Sum of all key values = ",sum(d))
