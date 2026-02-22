# Write a Python program to check the validity of password input by users.  
# Validation:  
# 1. At least 1 letter between [a-z] and 1 letter between [A-Z].  
# 2. At least 1 number between [0-9].  
# 3. At least 1 character from [$#@].  
# 4. Minimum length 6 characters.  
# 5. Maximum length 16 characters. 

import re
password = input("Enter password: ")
p1="[a-z]"
p2="[A-Z]"
p3="[0-9]"
p4="[$#@]"
if (re.search(p1,password) and re.search(p2,password) and re.search(p3,password) and re.search(p4,password) and len(password)>=6 and len(password)<=16):
    print("Valid password\n")
else:
    print("Invalid password\n")
