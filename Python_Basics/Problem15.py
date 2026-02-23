# Concatenate two lists index-wise 
# list1 = ["M", "na", "i", "She"]  
# list2 = ["y", "me", "s", "lly"] 
# Expected Outcome: ['My', 'name', 'is', 'Shelly'] 

list1 = ["M", "na", "i", "She"]  
list2 = ["y", "me", "s", "lly"] 

result = [a + b for a, b in zip(list1, list2)]
print(result)