#  Create a basic function that returns True if the word 'dog' is contained in the input string. 

def contains_dog(text: str) -> bool:
    return 'dog' in text

print(contains_dog("I have a dog."))       # True
print(contains_dog("Dogs are great pets")) # False (case-sensitive, plural form)
print(contains_dog("No animals here"))     # False