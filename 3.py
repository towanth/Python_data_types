list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

items1 = [j for i in list1 for j in i.items()]
items2 = [j for i in list2 for j in i.items()]

intersection = [i for i in items1 if i in items2]

print(intersection)

unique_1 = [i for i in items1 if i not in items2]
unique_2 = [i for i in items2 if i not in items1]

print(unique_1)
print(unique_2)
