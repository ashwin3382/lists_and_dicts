school = [
    {
        "class_name": "10A",
        "students": [
            {
                "name": "Alice",
                "age": 15,
                "scores": {"math": 85, "science": 92, "english": 78, "history": 88},
                "clubs": ["Robotics", "Math Club"]
            },
            {
                "name": "Bob",
                "age": 16,
                "scores": {"math": 90, "science": 88, "english": 81},
                "clubs": ["Drama"]
            },
            {
                "name": "Charlie",
                "age": 15,
                "scores": {"math": 75, "science": 85, "english": 80, "art": 95},
                "clubs": []
            },
            {
                "name": "Priya",
                "age": 14,
                "scores": {"math": 88, "science": 91, "english": 92, "art": 85},
                "clubs": ["Art Club", "Math Club"]
            }
        ]
    },
    {
        "class_name": "10B",
        "students": [
            {
                "name": "Carol",
                "age": 15,
                "scores": {"math": 95, "science": 82, "english": 85, "history": 91},
                "clubs": ["Robotics"]
            },
            {
                "name": "Dave",
                "age": 16,
                "scores": {"math": 80, "science": 85, "english": 87, "history": 77},
                "clubs": []
            },
            {
                "name": "Eve",
                "age": 15,
                "scores": {"math": 88, "science": 90, "english": 90, "art": 98},
                "clubs": ["Drama", "Art Club"]
            }
        ]
    },
    {
        "class_name": "10C",
        "students": [
            {
                "name": "Frank",
                "age": 15,
                "scores": {"math": 78, "science": 80, "english": 75},
                "clubs": ["Soccer"]
            },
            {
                "name": "Grace",
                "age": 16,
                "scores": {"math": 92, "science": 95, "english": 89, "history": 97},
                "clubs": ["Math Club", "Science Club"]
            },
            {
                "name": "Hannah",
                "age": 15,
                "scores": {"math": 85, "science": 89, "english": 93, "history": 87, "art": 100},
                "clubs": ["Art Club"]
            },
            {
                "name": "Isaac",
                "age": 16,
                "scores": {"math": 83, "science": 76, "english": 80},
                "clubs": []
            }
        ]
    }
]
#Compute the average score for each subject across all students in all classes.
import functools, collections, operator
def avg_of_each_subject(data: list):
    subjects_list = []
    subject_name_list = []
    for dicts in data:
        for keys in dicts:
            for values in dicts[keys]:
                if isinstance(values, dict):
                    for dictionary in values:
                        if isinstance(values[dictionary], dict):
                            subjects_list.append(values[dictionary])
                            for key in values[dictionary]:
                                subject_name_list.append(key)
    my_dict = dict(functools.reduce(operator.add, map(collections.Counter, subjects_list)))
    subject_count = dict(collections.Counter(subject_name_list))
    new_dict = {}
    for key, value in my_dict.items():
        for subject, count in subject_count.items():
            if key == subject:
                new_dict[key] = round(value / subject_count[subject], 2)

    print(new_dict)


#Identify the student with the highest overall average score (across all subjects) in the school.
def highest_avg_of_student(data: list):
    marks_dict = {}

    for class_data in data:
        for student in class_data["students"]:
            marks_dict[student["name"]] = round(sum(student["scores"].values())/len(student["scores"]), 2)
    highest_avg = {"Name":max(marks_dict, key = marks_dict.get), "Average": max(marks_dict.values())}
    return highest_avg

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