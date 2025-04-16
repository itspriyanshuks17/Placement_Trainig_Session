# Program to check if string contains only alphabets and concatenate them
# x = "codingcafe"
# y = ""

# for i in x:
#     if i.isalpha():
#         y+=i
#     else:
#         print("Entered string is not valid")
#         break
# print(y)


# Take the input from user and check if its alphanumeric : use if-else
# x = input("Enter the string : ")
# if x.isalnum():
#     print("Entered string is alphanumeric")
# else:
#     print("Entered string is not alphanumeric")


# Take input from the user and remove numericals from it
# x = input("Enter the string : ")
# y = ""
# for i in x:
#     if i.isalpha():
#         y+=i
# print(y)

# Take input from the user and check if it is a valid email id
# x = input("Enter the email id : ")
# if x.endswith("@gmail.com"):
#     print("Entered email id is valid")
# else:
#     print("Entered email id is not valid")

# Take input from the user and check if it is a valid mobile number
x = input("Enter the mobile number : ")

if x.isdigit() and len(x) == 10:
    print("Entered mobile number is valid")
else:
    print("Entered mobile number is not valid")
