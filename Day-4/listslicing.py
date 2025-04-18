# x=[101,102,103,104,105,106]

# print("For specific range")
# a=x[1:5]
# print(a)
# # for i in a:
# #   print(i)
# # print()

# print("\nFrom 0th to last")
# b=a[0:]
# print(b)


# print("\nNegative Slicing")
# c=x[-4:-1]
# print(c)


# print("\nReverse Negative Reversing")
# d=x[-1:-4]
# print(d) #Empty list


# print("\nReverse NR-2(n:m:-1)")
# e=x[-1:-4:-1]
# print(e)
# f=x[-4:-1:-1]
# print(f)


# print("\nStride 2")
# g=x[0:6:2]
# print(g)


# print("\nNegative and Positive Indexing in Nested List")
# y=[9,54,3,6,7,[12,13,14,[15,16]]]

# for i in range(len(y)):
#   print(y[i])

# print("\nSlicing of y")
# h=y[-4:-1]
# i=y[-1:-4:-1]
# j=y[3:4]
# k=y[5][3][1]
# l=y[5][3][0]
# m=y[5][2]
# n=y[5][3]
# o=y[5][3][0:]
# p=y[5][0:3]
# print("Negative Indexing",h)
# print("Negative indexing with slicing",i)
# print("Positive Indexing",j)
# print("Indexing inside nested list: ",k)
# print("Indexing inside nested list: ",l)
# print("Indexing inside nested list: ",m)
# print("Indexing inside nested list: ",n)
# print("Indexing inside nested list: ",o)
# print("Indexing inside nested list: ",p)

a=[10,20,30,[50,60]]
n=len(a)

# Time Complexity Analysis:
# - Outer loop runs n times where n is length of list a
# - For non-list elements: O(1) operation
# - For list elements: Inner loop runs m times where m is length of nested list
# - Overall Time Complexity: O(n*m) in worst case where m is max length of any nested list
# - Space Complexity: O(1) as only loop variables are used
for i in range(n):
  if type(a[i]) is list:
    if len(a[i])>1:
      m=len(a[i])
      for j in range(m):
        print(i,j,a[i][j])

  else:
    print(i,a[i])
