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

school = [
    {
        "class_name": "10A",
        "homeroom_teacher": {"name": "Mrs. Smith", "email": "smith@school.edu"},
        "students": [
            {
                "name": "Alice",
                "age": 15,
                "scores": {
                    "math": {"midterm": 85, "final": 90, "extra_credit": 5},
                    "science": {"midterm": 92, "final": 85, "lab": 20},
                    "english": {"midterm": 78, "final": 81, "essay": 30},
                    "history": {"midterm": 88, "final": 87, "project": 40}
                },
                "attendance": {"present": 180, "absent": 5, "late": 3},
                "clubs": [
                    {"name": "Robotics", "role": "President"},
                    {"name": "Math Club", "role": "Member"}
                ]
            },
            {
                "name": "Bob",
                "age": 16,
                "scores": {
                    "math": {"midterm": 90, "final": 94},
                    "science": {"midterm": 88, "final": 95, "lab": 15},
                    "english": {"midterm": 81, "final": 79},
                    "history": {"midterm": 70, "final": 76}
                },
                "attendance": {"present": 175, "absent": 10, "late": 8},
                "clubs": [{"name": "Drama", "role": "Lead"}]
            },
            {
                "name": "Charlie",
                "age": 15,
                "scores": {
                    "math": {"midterm": 75, "final": 79, "extra_credit": 10},
                    "science": {"midterm": 85, "final": 80, "lab": 25},
                    "english": {"midterm": 80, "final": 82, "essay": 28},
                    "art": {"midterm": 95, "final": 99, "portfolio": 50}
                },
                "attendance": {"present": 178, "absent": 7, "late": 0},
                "clubs": []
            },
            {
                "name": "Priya",
                "age": 14,
                "scores": {
                    "math": {"midterm": 88, "final": 91, "extra_credit": 7},
                    "science": {"midterm": 91, "final": 93, "lab": 18},
                    "english": {"midterm": 92, "final": 94, "essay": 34},
                    "art": {"midterm": 85, "final": 87, "portfolio": 40}
                },
                "attendance": {"present": 182, "absent": 3, "late": 2},
                "clubs": [
                    {"name": "Art Club", "role": "Secretary"},
                    {"name": "Math Club", "role": "Member"}
                ]
            }
        ]
    },
    {
        "class_name": "10B",
        "homeroom_teacher": {"name": "Mr. Lee", "email": "lee@school.edu"},
        "students": [
            {
                "name": "Carol",
                "age": 15,
                "scores": {
                    "math": {"midterm": 95, "final": 91, "extra_credit": 6},
                    "science": {"midterm": 82, "final": 85, "lab": 16},
                    "english": {"midterm": 85, "final": 88, "essay": 25},
                    "history": {"midterm": 91, "final": 89, "project": 35}
                },
                "attendance": {"present": 181, "absent": 4, "late": 1},
                "clubs": [{"name": "Robotics", "role": "Member"}]
            },
            {
                "name": "Dave",
                "age": 16,
                "scores": {
                    "math": {"midterm": 80, "final": 78, "extra_credit": 3},
                    "science": {"midterm": 85, "final": 83, "lab": 17},
                    "english": {"midterm": 87, "final": 86, "essay": 24},
                    "history": {"midterm": 77, "final": 79, "project": 28}
                },
                "attendance": {"present": 176, "absent": 8, "late": 6},
                "clubs": []
            },
            {
                "name": "Eve",
                "age": 15,
                "scores": {
                    "math": {"midterm": 88, "final": 94, "extra_credit": 5},
                    "science": {"midterm": 90, "final": 91, "lab": 21},
                    "english": {"midterm": 90, "final": 92, "essay": 31},
                    "art": {"midterm": 98, "final": 99, "portfolio": 48}
                },
                "attendance": {"present": 183, "absent": 2, "late": 1},
                "clubs": [
                    {"name": "Drama", "role": "Member"},
                    {"name": "Art Club", "role": "President"}
                ]
            }
        ]
    },
    {
        "class_name": "10C",
        "homeroom_teacher": {"name": "Ms. Chen", "email": "chen@school.edu"},
        "students": [
            {
                "name": "Frank",
                "age": 15,
                "scores": {
                    "math": {"midterm": 78, "final": 81, "extra_credit": 2},
                    "science": {"midterm": 80, "final": 79, "lab": 14},
                    "english": {"midterm": 75, "final": 79, "essay": 20}
                },
                "attendance": {"present": 177, "absent": 6, "late": 4},
                "clubs": [
                    {"name": "Soccer", "role": "Captain"}
                ]
            },
            {
                "name": "Grace",
                "age": 16,
                "scores": {
                    "math": {"midterm": 92, "final": 93, "extra_credit": 9},
                    "science": {"midterm": 95, "final": 97, "lab": 23},
                    "english": {"midterm": 89, "final": 91, "essay": 33},
                    "history": {"midterm": 97, "final": 98, "project": 45}
                },
                "attendance": {"present": 184, "absent": 1, "late": 0},
                "clubs": [
                    {"name": "Math Club", "role": "Vice President"},
                    {"name": "Science Club", "role": "President"}
                ]
            },
            {
                "name": "Hannah",
                "age": 15,
                "scores": {
                    "math": {"midterm": 85, "final": 87, "extra_credit": 8},
                    "science": {"midterm": 89, "final": 91, "lab": 19},
                    "english": {"midterm": 93, "final": 95, "essay": 36},
                    "history": {"midterm": 87, "final": 89, "project": 37},
                    "art": {"midterm": 100, "final": 100, "portfolio": 60}
                },
                "attendance": {"present": 185, "absent": 0, "late": 1},
                "clubs": [
                    {"name": "Art Club", "role": "Member"}
                ]
            },
            {
                "name": "Isaac",
                "age": 16,
                "scores": {
                    "math": {"midterm": 83, "final": 85},
                    "science": {"midterm": 76, "final": 79},
                    "english": {"midterm": 80, "final": 82}
                },
                "attendance": {"present": 170, "absent": 12, "late": 8},
                "clubs": []
            }
        ]
    }
]
#Compute the average score for each subject across all students in all classes.
def avg_of_each_subject(data: list):  # PRACTICE: Missing docstring and input validation
    subjects_dict = {}
    for class_data in data:
        for student in class_data["students"]:  # CRITICAL: KeyError if "students" key missing
            for sub, score in student["scores"].items():  # CRITICAL: KeyError if "scores" key missing
                if sub not in subjects_dict:
                    subjects_dict[sub] = {"midterm_marks": 0, "final_marks": 0, "p/l/e/cred_marks": 0 , "term_count": 0, "p/l/e/cred_count": 0}

                if "midterm" in score:
                    subjects_dict[sub]["midterm_marks"] += score["midterm"]

                if "final" in score:
                    subjects_dict[sub]["final_marks"] += score["final"]
                    subjects_dict[sub]["term_count"] += 1

                for k, v in score.items():
                    if k not in "midterms" and k not in "finals":  # CRITICAL: Wrong string comparison - should be k != "midterm" and k != "final"
                        subjects_dict[sub]["p/l/e/cred_marks"] += v
                        subjects_dict[sub]["p/l/e/cred_count"] += 1

    subjects_avg = {}
    for subject, score in subjects_dict.items():
        subjects_avg[subject]= {"midterm_marks": round(score["midterm_marks"]/score["term_count"], 2),  # CRITICAL: Division by zero if no finals exist
                                "final_marks": round(score["final_marks"]/score["term_count"], 2),  # CRITICAL: Division by zero if no finals exist
                                "p/l/e/cred_marks": round(score["p/l/e/cred_marks"]/score["p/l/e/cred_count"], 2)}  # CRITICAL: Division by zero if no extra scores exist

    return subjects_avg

#Identify the student with the highest overall average score (across all subjects) in the school.
def highest_avg_of_student(data: list):  # PRACTICE: Missing docstring
    total_each_kid = []

    for class_data in data:
        for student in class_data["students"]:  # CRITICAL: KeyError if "students" key missing
            total = 0
            count = 0
            for score in student["scores"].values():  # CRITICAL: KeyError if "scores" key missing
                count += 1
                total += sum(score.values())
                avg = round(total / count, 2)  # CRITICAL: Wrong calculation - should calculate avg AFTER the loop
            total_each_kid.append({"Name": student["name"], "Average": avg})  # CRITICAL: KeyError if "name" key missing

    return max(total_each_kid, key=lambda x: x["Average"])  # CRITICAL: ValueError if total_each_kid is empty

#For each class, list the top 2 students by total score.
def top2_in_each_class(data: list):  # PRACTICE: Missing docstring
    student_dict = {}

    for class_data in data:
        for student in class_data["students"]:  # CRITICAL: KeyError if "students" key missing
            total = 0
            for score in student["scores"].values():  # CRITICAL: KeyError if "scores" key missing
                total += sum(score.values())
            student["total_score"] = total  # CRITICAL: Modifies original data structure
        top2_students = sorted(class_data["students"], key=lambda x: x["total_score"], reverse=True)[:2]
        student_dict[class_data["class_name"]] = [student["name"] for student in top2_students]  # CRITICAL: KeyError if "class_name" missing
    return student_dict


# ------ Grading Report ------
# Grade: 3.0 / 10

# Critical Issues:
# 1. ALGORITHM ERROR in first function: Uses "k not in 'midterms'" which checks if character 
#    'k' exists in string "midterms". This means "midterm" and "final" will be incorrectly 
#    included because 'm' is in "midterms" and 'f' is in "finals". Should be k != "midterm".
# 2. DIVISION BY ZERO: First function will crash if any subject has no final scores or 
#    no extra credit scores when calculating averages.
# 3. WRONG CALCULATION in second function: Calculates average inside the loop instead of 
#    after collecting all scores, producing incorrect results.
# 4. DATA MUTATION: Third function modifies original data by adding "total_score" field.
# 5. NO ERROR HANDLING: All functions will crash with KeyError if expected keys are missing.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Poor variable naming ("p/l/e/cred_marks" is unclear).
# 4. No handling of edge cases (empty data, missing scores).
# 5. Functions don't follow single responsibility principle.

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. Functions return values instead of printing (mostly).
# 3. Good use of dictionary structures for organizing data.
# 4. Clean variable names in most places.
# 5. Proper use of round() for decimal precision.
# 6. Efficient use of built-in functions like sum(), max(), sorted().

# Detailed Analysis:
# This code attempts to handle a more complex nested data structure but has several 
# critical flaws that make it unreliable:
#
# 1. CRITICAL FAILURE - String Comparison Logic: The condition "k not in 'midterms'" 
#    is fundamentally wrong. It checks if the character exists anywhere in the string.
#    So "midterm" matches because 'm' is in "midterms", and "final" matches because 
#    'f' is in "finals". This causes midterm and final scores to be double-counted.
#
# 2. CRITICAL FAILURE - Average Calculation Error: In the second function, the average 
#    is calculated inside the subject loop, so it's being recalculated with each subject.
#    This produces completely wrong results - it should calculate total first, then average.
#
# 3. CRITICAL FAILURE - Division by Zero: The first function doesn't handle cases where 
#    subjects might not have certain types of scores, leading to division by zero errors.
#
# 4. CRITICAL FAILURE - Data Structure Assumptions: All functions assume perfect data 
#    structure without any validation or error handling.
#
# Test Case Analysis:
# - First function: Will incorrectly include midterm/final in extra credit calculations
# - Second function: Will produce wrong averages due to loop placement
# - Third function: Works correctly but modifies original data
#
# Example of Second Function Error:
# For a student with math: 100, science: 80:
# - After math: total=100, count=1, avg=100
# - After science: total=180, count=2, avg=90
# - Returns avg=90 (correct by coincidence)
# But for subjects with different score structures, results will be wrong.
#
# Recommendations:
# 1. Fix string comparison to use != instead of "not in"
# 2. Move average calculation outside the subject loop
# 3. Add zero-division checks in first function
# 4. Add comprehensive error handling for missing keys
# 5. Remove data mutation from third function
# 6. Add proper input validation and edge case handling
# 7. Add comprehensive docstrings and comments
# 8. Use more descriptive variable names
# 9. Add unit tests to verify correctness
#
# The code shows understanding of the problem but has fundamental logical errors that 
# make it produce incorrect results. It's in the "works but poorly written" category.