items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]

new_dict = {}

for i in items:
    if i[1] not in new_dict.keys():
        new_dict[i[1]] = []
    new_dict[i[1]].append(i[0])

print(new_dict)