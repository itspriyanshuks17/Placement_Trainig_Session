#Dictionary
# Indexing is not possible in dictionary
# {key:"values"}


#Creating dictionary with items
stud={101:"Rahul",102:"Raj",103:"Sonam"}
fees={'rahul':2000,'raj':3000,'sonam':8000}

print(stud)
# print(fees)
# print(stud[101])
# print(stud[102])


# "Modifying Dictionary"
stud[101]="Neha"
print("Modified Dictionary: ", stud)

stud[104]="Dhanraj"
print("Modified Dictionary: ", stud) #It will add {key:"values"} if not available in dict

#Deleting entire dict
# del stud
# print(stud)

#Copying dict
dup=stud.copy()
print("Duplicate dict: ",dup)


#items() Method
# Returns a list containing a tuple for each key-value pair in the dictionary
print("Dictionary items:", stud.items())

# Can be used to iterate over dictionary key-value pairs
for k,v in stud.items():
    print(f"Key: {k}, Value: {v}")

#update() Method - Used to update the dictionary with elements from another dictionary or from key-value pairs
#Syntax: dict.update([other])
#Can also update specific key using: dict.update({key: new_value})stud.update(fees)
print("Updated Dictionary: ", stud)
print(id(stud))

#Printing dictionary using for loop
print("Printing dictionary using for loop")
for i in stud:
    print(i, end=" ")#Printing keys of dictionary
print()
for i in stud:
    print(stud[i], end=" ")#Printing values of dictionary
print()

x="Thecodingcafe"
dict={}
for i in x:
  if i not in dict:
    dict[i]=1
  else:
    dict[i]+=1
print(dict)
