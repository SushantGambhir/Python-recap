# Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.  
# For example: seq = ['soup','dog','salad','cat','great'] 

seq = ['soup','dog','salad','cat','great']

result = list(filter(lambda word: not word.startswith('s'),seq))
print(result)