#Compute the average score for each subject across all students in all classes.
#Identify the student with the highest overall average score (across all subjects) in the school.
#For each class, list the top 2 students by total score.
import functools, collections, operator



school = [
    {
        "class_name": "10A",
        "students": [
            {"name": "Alice", "age": 15, "scores": {"math": 85, "science": 92, "english": 78}},
            {"name": "Bob", "age": 16, "scores": {"math": 90, "science": 88, "english": 81}},
            {"name": "Charlie", "age": 15, "scores": {"math": 75, "science": 85, "english": 80}},
        ]
    },
    {
        "class_name": "10B",
        "students": [
            {"name": "Carol", "age": 15, "scores": {"math": 95, "science": 82, "english": 85}},
            {"name": "Dave", "age": 16, "scores": {"math": 80, "science": 85, "english": 87}},
            {"name": "Eve", "age": 15, "scores": {"math": 88, "science": 90, "english": 90}},
        ]
    },
    {
        "class_name": "10C",
        "students": [
            {"name": "Frank", "age": 15, "scores": {"math": 78, "science": 80, "english": 75}},
            {"name": "Grace", "age": 16, "scores": {"math": 92, "science": 95, "english": 89}},
            {"name": "Hannah", "age": 15, "scores": {"math": 85, "science": 89, "english": 93}},
        ]
    }
]
#Compute the average score for each subject across all students in all classes.
def avg_of_each_subject(data: list):
    subjects_list = []
    counter = 0

    for dicts in data:
        for keys in dicts:
            for values in dicts[keys]:
                if isinstance(values, dict):
                    for dictionary in values:
                        if isinstance(values[dictionary], dict):
                            counter += 1
                            subjects_list.append(values[dictionary])

    my_dict = dict(functools.reduce(operator.add, map(collections.Counter, subjects_list)))

    new_dict = {}
    for key, value in my_dict.items():
        new_dict[key] = round(value / counter, 2)
    print(f"Average of each subject: {new_dict}")
avg_of_each_subject(school)

#Identify the student with the highest overall average score (across all subjects) in the school.
def highest_avg_of_student(data: list):
    marks_dict = {}

    for class_data in data:
        for student in class_data["students"]:
            marks_dict[student["name"]] = round(sum(student["scores"].values())/len(student["scores"]), 2)
    highest_avg = {"Name":max(marks_dict, key = marks_dict.get), "Average": max(marks_dict.values())}
    return highest_avg
print(highest_avg_of_student(school))

#For each class, list the top 2 students by total score.
def top2_in_each_class(data: list):
    student_dict = {}

    for class_data in data:
        for student in class_data["students"]:
            student["total_score"] = sum(student["scores"].values())
        top2_students = sorted(class_data["students"], key=lambda x: x["total_score"], reverse=True)[:2]
        student_dict[class_data["class_name"]] = [student["name"] for student in top2_students]
    print(student_dict)
top2_in_each_class(school)





