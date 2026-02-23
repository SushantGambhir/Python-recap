# Concatenate two lists in the following order 
# list1 = ["Hello ", "take "] 
# list2 = ["Dear", "Sir"] 
# Expected Output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] 

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

result = [x + y for x in list1 for y in list2]

print(result)