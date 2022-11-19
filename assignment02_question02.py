import string

alphabet_list = list(string.ascii_lowercase)

lst1 =alphabet_list
lst2 = []
for i in lst1:
    ascii = ord(i)
    lst2.append(ascii)
# print(lst1)
# print(lst2)
dict1 =dict(zip(lst1,lst2))
print("output :\n",dict1)
