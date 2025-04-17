# a=[10,20,-50,21.3, 'Geekyshows']
# print(a)

# # print(id(a))
# # a.append("x")
# # print(a)
# # print(id(a))

# # print(a[0])
# # print(a[1])
# # print(a[2])


# a=[1,2,3,4,5,6]
# print(a, id(a))

# a=[1,2,3,4,5,6]
# print(a, id(a))

# # print(a, id(a))
# # a[0]=40
# # print(a, id(a))

# #for loop to print
# print("\nTo print elements")
# for e in a:
#   print(e)

# print("\nTo print elements in reversed order")
# for e in reversed(a):
#   print(e)


# #while loop
# print("\nusing while loop")
# i=0
# while i<len(a):
#   print(i,"=",a[i])
#   i+=1

# #Deleting elements
# print("After deletion")
# del a[1]
# print(a)

# #to delete entire list
# del a


#Appending list using user inputs
# a=[]
# n=int(input("Enter no. of elements: "))

# for i in range(n):
#   a.append(input("Enter element:"))
#   if len(a)>10:
#     break
# print(a)


#Creating Empty List using list function

# for elements in dir(list):
#   # print(elements)
#   if "__" in elements:
#     continue
#   print(elements)


#insert() method

# a=[10,20,-50,21.3, 'Geekyshows']
# print("Before:", a)

# a.insert(2, "Entered")
# print("After:",a)

#pop() method
# a=[10,20,-50,21.3, 'Geekyshows']
# print("Before POP:", a)

# a.pop() #removes last element
# a.pop(3) #removes at index

# print("After POP: ",a)

#remove() method
# a=[10,20,-50,21.3,10, 'Geekyshows']
# print("Before remove:",a)

# a.remove(10)
# print("After remove:", a)

# Practice question->
# list=[9,5,4,3,8,5,7]

# nstr = str  # Get the string type
# m = map(nstr, list)  # Convert each element to string
# num_string = "".join(m)  # Join all strings together
# print(int(num_string))

# def process_list(list):
#     for i in range(len(list)):
#         if list[i]==5:
#             print("index of 5s:", i)

#     #Removing 5 which will occur first
#     list.remove(5)
#     str=""
#     for e in list:
#         str += f"{e}" 
#     num1=int(str)
#     print(num1)
#     print(type(num1))

#     #Removing 5 which will occur last
#     list.insert(1,5)
#     list.pop(5)
#     str=""
#     for e in list:
#         str += f"{e}" 
#     num2=int(str)
#     print(num2)
#     print(type(num2))

#     #Comparing num1 and num2
#     if num1>num2:
#         print("num1 is greater than num2")

#     elif num1<num2:
#         print("num2 is greater than num1")

#     else:
#         print("They are equal")

# process_list(list)

#Using reusable function
# def sorting(n):
#   list=[9,5,4,3,8,5,7]
#   list.pop(n)
#   return list

# number1=sorting(int(input("Enter the 1st index to rmove: ")))
# num1=int("".join(map(str, number1)))


# number2=sorting(int(input("Enter the 2st index to rmove: ")))
# num2=int("".join(map(str, number2)))
# print(num1, num2)

# if num1>num2:
#   print("num1 is greater than num2")

# elif num1<num2:
#   print("num2 is greater than num1")

# else:
#   print("They are equal")


#Reverse method
a=[10,20,30,10,90,'GeekyShows']
b=[100,200,300]

print("Before extend:", a)

a.extend(b)
print("After extend:", a)

a.append(b)
print("After append:", a)

index=0
for e in range(len(a)-1, -1, -1):
  index=e  

  num=int(input("Enter the index to find: "))
  if index==num:
    print(index)

print(a[index],"->",index)

  