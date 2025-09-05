## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
str = "Azzy"
for i in str:
    print(i)

## For Loop with Sets
s = {1, 2, 3, 4, 5}
for i in s:
    print(i)

## For Loop with Dictionaries
d = {'Name': 'Azzy', 'Age': 19, 'City': 'Karachi'}
for i in d:
    print(i)  # Prints keys of the dictionary       
for i in d.values():
    print(i)  # Prints values of the dictionary
for i in d.items():
    print(i)  # Prints key-value pairs as tuples
for i, j in d.items():
    print(i, j)  # Unpacking key-value pairs
for i in d.keys():
    print(i)  # Prints keys of the dictionary

