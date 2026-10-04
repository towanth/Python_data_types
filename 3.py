list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

intersection = [i for i in list1 if i in list2]

print(intersection)

unique1 = [i for i in list1 if i not in list2]
unique2 = [i for i in list2 if i not in list1]

print(unique1)
print(unique2)
