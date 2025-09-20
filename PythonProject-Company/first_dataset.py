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

company = {
    "name": "Headquarters",
    "employees": [{"name": "CEO", "salary": 250000}],
    "sub_departments": [
        {
            "name": "Engineering",
            "employees": [
                {"name": "Lead", "salary": 150000},
                {"name": "Dev1", "salary": 110000},
                {"name": "Dev2", "salary": 115000}
            ],
            "sub_departments": [
                {
                    "name": "QA",
                    "employees": [
                        {"name": "Test1", "salary": 90000},
                        {"name": "Test2", "salary": 95000}
                    ],
                    "sub_departments": []
                },
                {
                    "name": "DevOps",
                    "employees": [
                        {"name": "Ops1", "salary": 105000}
                    ],
                    "sub_departments": []
                }
            ]
        },
        {
            "name": "HR",
            "employees": [
                {"name": "HR1", "salary": 60000},
                {"name": "HR2", "salary": 65000}
            ],
            "sub_departments": []
        },
        {
            "name": "Marketing",
            "employees": [
                {"name": "Mark1", "salary": 70000}
            ],
            "sub_departments": []
        }
    ]
}


# Compute the total salary budget for the entire company.
def total_salary_budget(data: dict):  # PRACTICE: Missing docstring and input validation
    budget = 0
    for employee in data["employees"]:  # CRITICAL: KeyError if "employees" key doesn't exist
        budget += employee["salary"]  # CRITICAL: KeyError if "salary" key doesn't exist
    for sub_department in data["sub_departments"]:  # CRITICAL: KeyError if "sub_departments" key doesn't exist
        for employee in (sub_department["employees"]):  # PRACTICE: Unnecessary parentheses
            budget += employee["salary"]
        for unit in (sub_department["sub_departments"]):  # PRACTICE: Hard-coded to 2 levels only
            for employee in unit["employees"]:
                budget += employee["salary"]
    return budget

# Find the department (at any nesting level) with the highest average employee salary.
def dept_with_highest_avg_salary(data: dict):  # PRACTICE: Missing docstring
    avg_salary_dict = {}

    for sub_department in data["sub_departments"]:  # CRITICAL: Doesn't include root department in calculation
        avg_salary_sub_dept = 0
        for unit in sub_department["sub_departments"]:
            avg_salary_unit = 0
            for employee in (unit["employees"]):  # CRITICAL: Wrong calculation - divides each salary by total employees
                avg_salary_unit += employee["salary"] / len(unit["employees"])  # CRITICAL: Should sum salaries first, then divide
                avg_salary_dict[unit["name"]] = avg_salary_unit  # CRITICAL: Overwrites value in each iteration
        for employees in (sub_department["employees"]):  # CRITICAL: Wrong variable name and calculation
            avg_salary_sub_dept += employees["salary"] / len(sub_department["employees"])  # CRITICAL: Same calculation error
            avg_salary_dict[sub_department["name"]] = avg_salary_sub_dept  # CRITICAL: Overwrites value in each iteration
    return {"Department with highest average salary":max(avg_salary_dict, key = avg_salary_dict.get), "Average": max(avg_salary_dict.values())}  # PRACTICE: Poor formatting, CRITICAL: Crashes if dict is empty

# List all employees who earn above the company-wide average salary, along with their department path.
def emp_with_higher_than_avg_salary(data: dict):  # PRACTICE: Missing docstring, CRITICAL: Doesn't return department path as required
    total_budget_salary = total_salary_budget(data)
    employees_num = 0
    employees_with_higher_avg_salary = {}
    for employee in data["employees"]:
        employees_num += 1
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            employees_num += 1
        for unit in (sub_department["sub_departments"]):  # PRACTICE: Only handles 2 levels
            for employee in (unit["employees"]):
                employees_num += 1
    avg_company_wide_salary = total_budget_salary/employees_num  # PRACTICE: Missing space around operator

    for employee in (data["employees"]):
        if employee["salary"] > avg_company_wide_salary:
            employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path as required
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            if employee["salary"] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
        for unit in (sub_department["sub_departments"]):
            for employee in (unit["employees"]):
                if employee["salary"] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
    return employees_with_higher_avg_salary


# ------ Grading Report ------
# Grade: 3.5 / 10

# Critical Issues:
# 1. Incorrect average calculation in dept_with_highest_avg_salary(): The algorithm is 
#    fundamentally wrong. It calculates (salary1/count + salary2/count + ...) instead 
#    of (salary1 + salary2 + ...)/count, producing incorrect results.
# 2. Variable overwriting in loops: avg_salary_dict values are overwritten in each 
#    iteration, meaning only the last employee's calculation is kept.
# 3. Missing department path: emp_with_higher_than_avg_salary() doesn't return department 
#    paths as explicitly required in the function description.
# 4. No error handling: Functions will crash with KeyError if expected keys are missing.
# 5. Root department exclusion: dept_with_highest_avg_salary() ignores the root 
#    department's employees entirely.
# 6. Empty dictionary handling: max() function will crash if avg_salary_dict is empty.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. No input validation or type checking.
# 3. Unnecessary parentheses around iterables.
# 4. Poor variable naming (employees vs employee).
# 5. Missing spaces around operators.
# 6. Poor code formatting and readability.
# 7. Code duplication across functions.
# 8. Hard-coded to handle only 2 levels of nesting (acceptable given recursion note).

# Good Practices:
# 1. Type hints are used for function parameters.
# 2. Functions are properly named and descriptive.
# 3. Code structure is logical and follows the dataset structure.
# 4. The first function (total_salary_budget) works correctly for the given dataset.

# Detailed Analysis:
# The code has some fundamental issues that prevent it from working correctly:
#
# 1. CRITICAL FAILURE - Mathematical Error: The second function has a completely wrong 
#    algorithm for calculating averages. For a department with employees earning [90000, 95000], 
#    it calculates (90000/2 + 95000/2) = 92500 instead of (90000 + 95000)/2 = 92500. 
#    While this specific example gives the same result, the logic is wrong and would fail 
#    in other cases or with different iteration patterns.
#
# 2. CRITICAL FAILURE - Loop Logic Error: The avg_salary_dict is being overwritten in 
#    each iteration instead of being calculated once per department. This means only 
#    the last employee's calculation affects the final result.
#
# 3. CRITICAL FAILURE - Missing Required Functionality: The third function completely 
#    fails to meet the requirement of returning "department path" along with employee info.
#
# 4. CRITICAL FAILURE - Incomplete Department Coverage: The second function ignores the 
#    root department employees when calculating averages.
#
# 5. The first function actually works correctly for the given dataset and produces 
#    the right total salary budget.
#
# Recommendations:
# 1. Fix the average calculation: Sum all salaries first, then divide by count.
# 2. Calculate department averages outside the employee loop.
# 3. Include root department in average calculations.
# 4. Add department path tracking in the third function.
# 5. Add proper error handling for missing keys.
# 6. Add comprehensive docstrings and comments.
# 7. Use more descriptive variable names and follow PEP 8 guidelines.
# 8. Add input validation to handle edge cases.
#
# The code partially works (first function is correct) but has significant algorithmic 
# errors in the other functions that produce wrong results or missing required information.