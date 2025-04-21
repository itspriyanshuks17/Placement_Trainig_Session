
# print("TO print first 3 and last 3 characters of a string")
# s = "Wonderful"
# num_chars = 3
# if len(s) <6:
#     print("")
# else:
#     new_string = s[:num_chars] + s[len(s)-num_chars:]
#     print(new_string)   



# print("to print char which are at even indices")
# s = "Coding"
# new_str=""
# for i in range(len(s)):
#     if i%2 == 0:
#         new_str += s[i]
# print(new_str)


# print("to skip the char at given index")
# s = "Ironman"
# n =1
# if (len(s) == 0 ) or (n>len(s)):
#     print("")
# else:
#     new_str = ""
#     for i in range(len(s)):
#         if i != n:
#             new_str += s[i]
#     print(new_str)  


# print("to replace a char with another char")
# s = "hello"
# new_s = ""
# cur_char = 'l'
# new_char = 's'

# for char in s:
#     if char == cur_char:
#         new_s += new_char
#     else:
#         new_s += char
# print(new_s)  

# print("replace with replace()")
# n = "Kumir"
# newchar = n.replace("i","a")
# print(newchar)


# print("to replace , with . in a string")
# string = "hello, world, how are you"
# char1 = ","
# char2 = "."
# new_string = ""

# for char in string:
#     if char == char1:
#         new_string += char2
#     else:
#         new_string += char
# print(string)
# print(new_string)

# print("to remove space in a string")
# s = "hello world"
# s = s.replace(" ","")
# print(s)

# s = "hello"
# prefix = "he"
# print(s.startswith(prefix))


# s = "hello"
# prefix = "he"
# print(s[:len(prefix)] == prefix)

# s = "hello world"
# wordlist = s.split()
# new_s=""

# for word in wordlist:
#     reversed_word = "".join(reversed(word))
#     print(reversed_word)
#     swapped_case_word = reversed_word.swapcase()
#     new_s += swapped_case_word + " "
# new_s = new_s.rstrip()
# print(new_s)    
# new_s = new_s.rstrip()
# print(new_s) 


# print("to find repeated char in a string")
# s = "hello"
# repeated_count = 0
# repeated_char = []

# for char in s:
#     if (s.count(char) > 1) and (char not in repeated_char):
#         if char not in repeated_char:
            
#             repeated_count += 1
#             repeated_char.append(char)

# print("Repeated characters:", repeated_char)
# print()



# print("to find factorial of a number")
# def factorial(n):
#     if n == 0 or  n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))



# print("to enter given numbers")

# def number(n):
#     if n==0 :
#         return 0
#     else:
#         print(n)
#         return number(n-1)
    
# print(number(5))


# def number(n):
#     if n==0 :
#         return 0
#     else:
#         print(n)
#         return number(n+1)
    
# print(number(1))



# print("To calculate sum of numbers in given list")

# def sum_list(lst):              
#     if len(lst) == 0:
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])
# print(sum_list([1, 2, 3, 4, 5]))


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(sum_list([1, 2, 3, 4, 5]))


def countdown(n):
    if n> 10:
        print("Blast off:")
        return 0
    else:   
        print(n)
        return countdown(n+1)
(countdown(1))

def num(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + num(list[1:])
    