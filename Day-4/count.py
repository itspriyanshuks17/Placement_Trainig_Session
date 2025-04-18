a=[10, 20, 30, 20, 10, 90, 'GeekyShow', 10, 30]
num=a.count(10)
print(num)

#only unique elements in new list

#My method
unique_list = []
for i in a:
  if a.count(i) >=  1 and i not in unique_list:
    unique_list.append(i)

print(unique_list)

#Saylees method
c=[10, 20, 30, 20, 10, 90, 'GeekyShow', 10, 30]
d=[]
for i in c:
  if c.count(i) >= 1:
    continue
  d.append(i)
print(d)
