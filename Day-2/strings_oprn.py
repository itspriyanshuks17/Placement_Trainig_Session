# String operations in python
# 1. Swapcase Function -> captilize lower case and lower case to upper case
print("Swapcase Function")
name="PriyanshuKSharma"
str1 = name.swapcase()
print(str1)

#  2. Title Function -> Capitalize first letter of each word
print("\nTitle Function")
name="priyanshu k sharma"
str1 = name.title()
print(str1)

# 3. isTitle Function -> Check if first letter of each word is capitalized
print("\nisTitle Function")
name="Priyanshu K Sharma"
str1 = name.istitle()
print(str1)

# 4. isAlpha Function -> Check if all characters are alphabets
print("\nisAlpha Function")
name="PriyanshuKSharma"
str1 = name.isalpha()
print(str1)

# 5. lstrip Function -> Remove leading whitespaces
print("\nlstrip Function")
name="  PriyanshuKSharma"
str1 = name.lstrip()
print(str1) 

# 6. rstrip Function -> Remove trailing whitespaces
print("\nrstrip Function")
name="PriyanshuKSharma  "
str1 = name.rstrip()
print(str1)

# 7. strip Function -> Remove leading and trailing whitespaces
print("\nstrip Function")  
name="  PriyanshuKSharma  "
str1 = name.strip()
print(str1) 

# isupper Function -> Check if all characters are upper case
print("\nisupper Function")
name="PriyanshuKSharma"
str1 = name.isupper()
print(str1)

# islower Function -> Check if all characters are lower case
print("\nislower Function")
name="PriyanshuKSharma"
str1 = name.islower()
print(str1)

#upper Function -> Convert all characters to upper case
print("\nupper Function")
name="PriyanshuKSharma"
str1 = name.upper()
print(str1)

#join Function -> Join a list of strings with a separator
print("\njoin Function")
name="PriyanshuKSharma"
str1 = name.join(" ")
print(str1)

# startswith Function -> Check if a string starts with a given substring
print("\nstartswith Function") 
name="PriyanshuKSharma"
str1 = name.startswith("Priyanshu")
print(str1)

# endswith Function -> Check if a string ends with a given substring
print("\nendswith Function")
name="PriyanshuKSharma"
str1 = name.endswith("Sharma")
print(str1)

# isdigit Function -> Check if all characters are digits
print("\nis digit Function")
name="1234567890"
str1 = name.isdigit()
print(str1)

# isalnum Function -> Check if all characters are alphanumeric
print("\nis alnum Function")
name="PriyanshuKSharma"
str1 = name.isalnum()
print(str1)

# replace Function -> Replace a substring with another substring  
print("\nreplace Function")
name="PriyanshuKSharma"
str1 = name.replace("Priyanshu","PriyanshuKSharma")
print(str1)

# find Function -> Find the index of a substring in a string
print("\nfind Function")
name="PriyanshuKSharma"
str1 = name.find("K")
print(str1)
