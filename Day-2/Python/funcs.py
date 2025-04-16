# def display():
#     print("Welcome to the game!")

# display()


#Defining a function with parameter
# def add(y):
#     x =10
#     y=10
#     c = x+y
#     # print("The sum is : ",c)
#     return c

# add(20) # This will not work as we are not returning anything from the function
# print("The sum is : ",add(20))


# Nested Function Example
# def disp():
#     def show():
#         print("Show function")
#     show()
#     print("Display function")
#     show()

# disp()


# Nested Function with Return Value Example
# def disp():
#     def show():
#         return "Show function"
#     result = show() + " " + "Display function"
#     return result
#     return show()

# print(disp())


# Nested Function with Parameter Example
# def disp(st):
#     def show():
#         return "Show function"
#     result = show() + " " + st + " "+"Display function"
#     return result

# print(disp("Priyanshu"))


# Positional Arguement
# def pw(x,y):
#     z=x**y
#     return z

# print(pw(y=2,x=3))


# Keyword Arguments
# Example 1

# def show(name, age):
#     print(f"Name: {name}, Age: {age}")

# show(name="Priyanshu", age=22)  # Keyword arguments
# show(age=22, name="Priyanshu")  # Keyword arguments
# show("Neha",21)
# show(21,"Neha")
# show(age=21, name="Neha")


# Example 2
# def show(name, age=21):
#     print(f"Name: {name}, Age: {age}")

# show(name="Priyanshu", age=22)  # Keyword arguments
# show(age=22, name="Priyanshu")  # Keyword arguments
# show("Priyanshu")  # Default argument

#Arbitary Arguments
# Non-Keyword Variable Length Arguments -> Stores in a tuple
# Example 1
# def show(*num):

#     z=num[0]+num[1]+num[2]+num[3]+num[4]
#     return z

# print(show(1,2,3,4,5))

# Example 2
# def show2(*num):
#     z=0
#     for i in num:
#         z=z+i
#     return z

# print(show2(1,2,3,4,5))
# # Taking multiple inputs from user, converting to integers and passing as arguments
# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# print(show2(*numbers))


# Example 3 -> first positional argument and then arbitary arguments
# This is a combination of positional argument and non-keyword variable length argument (*args)
# x is a positional argument that must be provided
# *num is a variable length argument that accepts any number of additional arguments and stores them in a tuple
# def add(x, *num):
#     z=x+num[0]+num[1]
#     return z

# print(add(1,2,3))


# Keyword Variable Length Arguments -> Stores in a dictionary
def show(**var):
    for key, value in var.items():
        print(f"{key}: {value}")

show(name="Priyanshu", age=22, city="Delhi")  # Keyword arguments
show(name="Neha", city="Delhi")  # Keyword arguments


