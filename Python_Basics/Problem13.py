# Create a function that counts the number of times the word "dog" occurs in a string

def count_dog(text: str) -> int:
    return text.count('dog')

print(count_dog("dog dog DOG doghouse"))   # Output: 3
print(count_dog("I love my dog."))         # Output: 1
print(count_dog("No animals here."))       # Output: 0