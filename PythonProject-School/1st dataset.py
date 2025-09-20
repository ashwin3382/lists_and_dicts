# Grading Rules:
# 1. Grade out of 10, in increments of 0.5.
# 2. < 3.0 indicates the code fails to function altogether (FAIL).
# 3. 3.0 indicates the .py file works but the code is poorly written.
# 4. 3.5–5.0 indicates many bad practices or loopholes, code may run but is fragile.
# 5. 5.5–7.0 indicates acceptable code with some issues in style or edge cases.
# 6. 7.5–9.0 indicates good code with minor style or best-practice lapses.
# 7. 9.5–10.0 is reserved for excellent, clean, idiomatic, well-tested code.
#
# Issue Severity:
# - CRITICAL: Affects the entire code or dataset handling in all cases.
# - PRACTICE: Bad coding practice that could lead to errors or maintenance burden.

#Compute the average score for each subject across all students in all classes.
#Identify the student with the highest overall average score (across all subjects) in the school.
#For each class, list the top 2 students by total score.
import functools, collections, operator  # PRACTICE: Multiple imports on one line, not following PEP 8



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
def avg_of_each_subject(data: list):  # PRACTICE: Missing docstring
    subjects_list = []
    counter = 0

    for dicts in data:  # PRACTICE: Poor variable naming 'dicts' for class objects
        for keys in dicts:  # CRITICAL: Unnecessary loop - should directly access "students" key
            for values in dicts[keys]:  # CRITICAL: Will crash if key is not "students" (like "class_name")
                if isinstance(values, dict):  # CRITICAL: Unnecessary type check, students are always dicts
                    for dictionary in values:  # PRACTICE: Poor variable naming 'dictionary' for score keys
                        if isinstance(values[dictionary], dict):  # CRITICAL: This checks if scores dict exists, but logic is confusing
                            counter += 1
                            subjects_list.append(values[dictionary])  # CRITICAL: Appends entire scores dict, not individual scores

    my_dict = dict(functools.reduce(operator.add, map(collections.Counter, subjects_list)))  # CRITICAL: Overly complex approach using functools/operator

    new_dict = {}
    for key, value in my_dict.items():
        new_dict[key] = round(value / counter, 2)  # PRACTICE: Could use dict comprehension
    print(f"Average of each subject: {new_dict}")  # PRACTICE: Function should return, not print
avg_of_each_subject(school)

#Identify the student with the highest overall average score (across all subjects) in the school.
def highest_avg_of_student(data: list):  # PRACTICE: Missing docstring
    marks_dict = {}

    for class_data in data:  # PRACTICE: Good variable naming
        for student in class_data["students"]:  # CRITICAL: KeyError if "students" key missing
            marks_dict[student["name"]] = round(sum(student["scores"].values())/len(student["scores"]), 2)  # CRITICAL: KeyError if "name" or "scores" missing
    highest_avg = {"Name":max(marks_dict, key = marks_dict.get), "Average": max(marks_dict.values())}  # PRACTICE: Space issues around =
    return highest_avg  # PRACTICE: Good - returns instead of printing
print(highest_avg_of_student(school))

#For each class, list the top 2 students by total score.
def top2_in_each_class(data: list):  # PRACTICE: Missing docstring
    student_dict = {}

    for class_data in data:
        for student in class_data["students"]:  # CRITICAL: KeyError if "students" key missing
            student["total_score"] = sum(student["scores"].values())  # CRITICAL: Modifies original data structure, KeyError if "scores" missing
        top2_students = sorted(class_data["students"], key=lambda x: x["total_score"], reverse=True)[:2]  # PRACTICE: Good use of sorted and lambda
        student_dict[class_data["class_name"]] = [student["name"] for student in top2_students]  # CRITICAL: KeyError if "class_name" missing
    print(student_dict)  # PRACTICE: Should return instead of print
top2_in_each_class(school)


# ------ Grading Report ------
# Grade: 4.5 / 10

# Critical Issues:
# 1. First function has overly complex and fragile logic - uses nested loops that will crash
#    if the data structure doesn't match exactly. The loop "for keys in dicts" will iterate
#    over ALL keys including "class_name", causing crashes.
# 2. No error handling - functions will crash with KeyError if expected keys are missing.
# 3. Data mutation in third function - modifies the original data structure by adding
#    "total_score" field, which is a side effect.
# 4. First function uses unnecessarily complex functools/operator approach when simple
#    aggregation would work better.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. Inconsistent return vs print behavior across functions.
# 3. Poor variable naming in first function ('dicts', 'dictionary').
# 4. Multiple imports on single line violates PEP 8.
# 5. No input validation or type checking.
# 6. Formatting issues (spaces around operators).
# 7. Could use more Pythonic approaches (dict comprehensions).

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. Second and third functions have cleaner, more readable logic.
# 3. Good use of built-in functions like sum(), max(), sorted().
# 4. Third function uses lambda and list comprehension effectively.
# 5. Functions are named descriptively.
# 6. Round() function used appropriately for decimal precision.

# Detailed Analysis:
# The code has a mix of working and problematic sections:
#
# 1. PARTIAL SUCCESS - Functions 2 and 3 Work: The second and third functions actually
#    work correctly for the given dataset and produce the right results. They use
#    clean, readable logic.
#
# 2. CRITICAL ISSUE - Function 1 is Fragile: The first function has a major design flaw.
#    The nested loop structure "for keys in dicts" will iterate over ALL dictionary keys,
#    including "class_name". When it tries to iterate over the string "10A", it will work
#    because strings are iterable, but the logic becomes unpredictable and fragile.
#
# 3. CRITICAL ISSUE - No Error Handling: All functions assume the data structure is
#    perfect and will crash with KeyError if any expected keys are missing.
#
# 4. CRITICAL ISSUE - Side Effects: The third function modifies the original data by
#    adding "total_score" fields, which could affect other parts of a larger program.
#
# 5. DESIGN ISSUE - Inconsistent Interface: Functions have inconsistent behavior -
#    some print, some return, making them hard to use programmatically.
#
# Functionality Test Results:
# - Function 1: Works but is overly complex and fragile
# - Function 2: Works correctly and produces right results
# - Function 3: Works correctly but has side effects
#
# Recommendations:
# 1. Simplify the first function to directly access the "students" key
# 2. Add comprehensive error handling for missing keys
# 3. Make all functions return values instead of printing
# 4. Add proper docstrings and type hints
# 5. Remove data mutation from the third function
# 6. Add input validation
# 7. Use more consistent and Pythonic coding patterns
# 8. Follow PEP 8 style guidelines more strictly
#
# The code partially works (2 out of 3 functions work reliably) but has significant
# design flaws and fragility issues that prevent it from being production-ready.