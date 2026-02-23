# Given a Python list, remove all occurrence of 20 from the list 
# list1 = [5, 20, 15, 20, 25, 50, 20] 

list1 = [5, 20, 15, 20, 25, 50, 20]
result = [item for item in list1 if item != 20]
print(result)