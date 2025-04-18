# 1. Printing frequency of each character in string
# x="Thecodingcafe"
# dict={}
# for i in x:
#   if i not in dict:
#     dict[i]=1
#   else:
#     dict[i]+=1
# print(dict)

# y = "Priyanshukumarsharma"
# dict1 = {}

# for m in y:
#     if m not in dict1:
#         dict1[m] = 1
#     else:
#         dict1[m] += 1

# print(dict1)

# # 2. in list
# a=[1, 2, 3, 4, 5, 6, 7, 4, 6, 7]
# dict2={}

# for n in a:
#   if n not in dict2:
#     # dict2[n]=a.count(i)
#     dict2[n]=1
#   else:
#     dict2[n]+=1

# print(dict2)


#Swapcase: - HackerRank
# def swap_case(s):
#     new_swap = ""

#     for i in range(len(s)):
#         if s[i].islower():
#             new_swap += s[i].upper()
#         else:
#             new_swap += s[i].lower()

#     return new_swap

# if __name__ == '__main__':
#     print("Enter your string: ")
#     s = input()
#     result = swap_case(s)
#     print(result)


#if substring is present in string 
def issubsequence(string, substring):
  i=0
  j=0

  while i < len(substring) and i < len(string):
    if substring[i] == string[j]:
      i+=1

    j+=1

  return i==len(substring)

string="abcdefghij"
substring="adi"
result=issubsequence(string, substring)
print(result)

