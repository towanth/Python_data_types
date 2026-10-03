data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]

subjects = {}

for i in data:
    if i["subject"] not in subjects.keys():
        subjects[i["subject"]] = {}
    subjects[i["subject"]][i["student"]] = i["grade"]

print(subjects)

