students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]

new_dict = {i.get("name"): sum(i.get("grades")) / len(i.get("grades")) for i in students}

print(new_dict)

max_grade = max(new_dict.values())

for s in new_dict.keys():
    if new_dict[s] == max_grade:
        print(s)