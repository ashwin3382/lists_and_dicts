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
    "employees": [
        {"name": "CEO", "salary": 250000, "bonus": 50000, "type": "permanent", "tenure_years": 15},
        {"name": "CTO", "salary": 200000, "type": "permanent", "tenure_years": 10}
    ],
    "sub_departments": [
        {
            "name": "Engineering",
            "employees": [
                {"name": "Lead", "salary": 150000, "bonus": 20000, "type": "permanent", "tenure_years": 8},
                {"name": "Dev1", "salary": 110000, "type": "contract", "tenure_years": 1, "remote": True},
                {"name": "Dev2", "salary": 115000, "bonus": 10000, "type": "permanent", "tenure_years": 5, "remote": False},
                {"name": "Intern", "salary": 30000, "type": "intern", "tenure_years": 0}
            ],
            "sub_departments": [
                {
                    "name": "QA",
                    "employees": [
                        {"name": "Test1", "salary": 90000, "type": "permanent", "tenure_years": 4, "remote": True},
                        {"name": "Test2", "salary": 95000, "bonus": 5000, "type": "contract", "tenure_years": 2, "remote": False}
                    ],
                    "sub_departments": [
                        {
                            "name": "Automation",
                            "employees": [
                                {"name": "Auto1", "salary": 99000, "type": "permanent", "tenure_years": 3, "remote": False},
                                {"name": "Auto2", "salary": 97000, "type": "contract", "tenure_years": 1, "remote": True}
                            ],
                            "sub_departments": []
                        }
                    ]
                },
                {
                    "name": "DevOps",
                    "employees": [
                        {"name": "Ops1", "salary": 105000, "bonus": 5000, "type": "contract", "tenure_years": 2, "remote": True},
                        {"name": "Ops2", "salary": 108000, "type": "permanent", "tenure_years": 3, "remote": False}
                    ],
                    "sub_departments": []
                }
            ]
        },
        {
            "name": "HR",
            "employees": [
                {"name": "HR1", "salary": 60000, "type": "permanent", "tenure_years": 7},
                {"name": "HR2", "salary": 65000, "type": "permanent", "tenure_years": 2},
                {"name": "Recruiter", "salary": 48000, "type": "contract", "tenure_years": 1}
            ],
            "sub_departments": [
                {
                    "name": "Training",
                    "employees": [
                        {"name": "Trainer1", "salary": 50000, "type": "permanent", "tenure_years": 4, "remote": False},
                        {"name": "Trainer2", "salary": 52000, "bonus": 1000, "type": "permanent", "tenure_years": 2, "remote": True}
                    ],
                    "sub_departments": [
                        {
                            "name": "Onboarding",
                            "employees": [
                                {"name": "Onboarder1", "salary": 48000, "type": "contract", "tenure_years": 1, "remote": False}
                            ],
                            "sub_departments": []
                        }
                    ]
                }
            ]
        },
        {
            "name": "Marketing",
            "employees": [
                {"name": "Mark1", "salary": 70000, "type": "permanent", "tenure_years": 5, "remote": True},
                {"name": "Mark2", "salary": 72000, "type": "contract", "tenure_years": 3, "remote": False},
                {"name": "Mark3", "salary": 69000, "type": "part-time", "tenure_years": 2}
            ],
            "sub_departments": []
        },
        {
            "name": "Legal",
            "employees": [
                {"name": "Lawyer1", "salary": 120000, "type": "permanent", "tenure_years": 9},
                {"name": "Lawyer2", "salary": 130000, "type": "contract", "tenure_years": 4}
            ],
            "sub_departments": []
        }
    ]
}

# Compute the total salary budget for the entire company.
def total_salary_budget(data: dict):  # PRACTICE: Missing docstring and input validation
    budget = 0
    bonus = "bonus"  # PRACTICE: Hardcoded string, should use constant
    for employee in data["employees"]:  # CRITICAL: KeyError if "employees" key doesn't exist
        budget += employee["salary"]  # CRITICAL: KeyError if "salary" key doesn't exist
        if bonus in employee is not None:  # CRITICAL: Wrong syntax - 'is not None' checks if result of 'in' operation is not None, which is always True/False
            budget += employee[bonus]

    for sub_department in data["sub_departments"]:  # CRITICAL: KeyError if "sub_departments" key doesn't exist
        for employee in sub_department["employees"]:
            budget += employee["salary"]
            if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                budget += employee[bonus]
        for unit in sub_department["sub_departments"]:
            for employee in unit["employees"]:
                budget += employee["salary"]
                if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                    budget += employee[bonus]
            for section in unit["sub_departments"]:  # PRACTICE: Good improvement - handles 3 levels now
                for employee in section["employees"]:
                    budget += employee["salary"]
                    if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                        budget += employee[bonus]
    return budget

# Find the department (at any nesting level) with the highest average employee salary.
def dept_with_highest_avg_salary(data: dict):  # PRACTICE: Missing docstring
    avg_salary_dict = {}
    bonus = "bonus"
    for sub_department in data["sub_departments"]:  # CRITICAL: Still doesn't include root department
        avg_salary_sub_dept = 0
        for unit in sub_department["sub_departments"]:
            avg_salary_unit = 0
            for employee in (unit["employees"]):  # CRITICAL: Still wrong calculation - divides each salary by total
                if bonus in employee is not None:  # CRITICAL: Wrong syntax repeated
                    avg_salary_unit += (employee["salary"]+employee[bonus])/ len(unit["employees"])  # CRITICAL: Wrong formula
                else:
                    avg_salary_unit += employee["salary"]/len(unit["employees"])  # CRITICAL: Wrong formula
                avg_salary_dict[unit["name"]] = avg_salary_unit  # CRITICAL: Overwrites in each iteration
        for employees in (sub_department["employees"]):  # CRITICAL: Wrong variable name and calculation
            if bonus in employees is not None:  # CRITICAL: Wrong syntax
                avg_salary_sub_dept += (employees["salary"]+employees[bonus]) / len(sub_department["employees"])  # CRITICAL: Wrong formula
            else:
                avg_salary_sub_dept += employees["salary"]/len(sub_department["employees"])  # CRITICAL: Wrong formula
            avg_salary_dict[sub_department["name"]] = avg_salary_sub_dept  # CRITICAL: Overwrites in each iteration
        for unit in sub_department["sub_departments"]:  # CRITICAL: Code duplication and incomplete logic
            avg_salary_section = 0
            for section in (unit["sub_departments"]):
                for employee in (section["employees"]):
                    if bonus in employee is not None:  # CRITICAL: Wrong syntax
                        avg_salary_section += (employee["salary"]+employee[bonus])/len(section["employees"])  # CRITICAL: Wrong formula
                    else:
                        avg_salary_section += employee["salary"]/len(section["employees"])  # CRITICAL: Wrong formula
                                                                                                              # CRITICAL: avg_salary_section never added to dictionary

    return {"Department with highest average salary":max(avg_salary_dict, key = avg_salary_dict.get), "Average": max(avg_salary_dict.values())}  # CRITICAL: Crashes if dict is empty

# List all employees who earn above the company-wide average salary, along with their department path.
def emp_with_higher_than_avg_salary(data: dict):  # CRITICAL: Still doesn't return department path as required
    total_budget_salary = total_salary_budget(data)
    employees_num = 0
    employees_with_higher_avg_salary = {}
    for employee in data["employees"]:
        employees_num += 1
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            employees_num += 1
        for unit in (sub_department["sub_departments"]):
            for employee in (unit["employees"]):
                employees_num += 1
            for section in (unit["sub_departments"]):  # PRACTICE: Good - handles 3 levels
                for employee in (section["employees"]):
                    employees_num += 1
    avg_company_wide_salary = round(total_budget_salary/employees_num, 2)  # PRACTICE: Good use of round()
    print(avg_company_wide_salary)  # PRACTICE: Debug print should be removed in production
    bonus = "bonus"
    for employee in (data["employees"]):
        if bonus in employee is not None:  # CRITICAL: Wrong syntax - should be 'if bonus in employee:'
            if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]  # CRITICAL: Missing department path
        elif employee["salary"] > avg_company_wide_salary:
            employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            if bonus in employee is not None:  # CRITICAL: Wrong syntax repeated
                if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]  # CRITICAL: Missing department path
            elif employee["salary"] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
        for unit in (sub_department["sub_departments"]):
            for employee in (unit["employees"]):
                if bonus in employee is not None:  # CRITICAL: Wrong syntax repeated
                    if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                        employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]  # CRITICAL: Missing department path
                elif employee["salary"] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
            for section in (unit["sub_departments"]):
                for employee in (section["employees"]):
                    if bonus in employee is not None:  # CRITICAL: Wrong syntax repeated
                        if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                            employees_with_higher_avg_salary[employee["name"]] = employee["salary"] + employee[bonus]  # CRITICAL: Missing department path
                    elif employee["salary"] > avg_company_wide_salary:
                        employees_with_higher_avg_salary[employee["name"]] = employee["salary"]  # CRITICAL: Missing department path
    return employees_with_higher_avg_salary


# ------ Grading Report ------
# Grade: 1.0 / 10

# Critical Issues:
# 1. SYNTAX ERROR: "if bonus in employee is not None" is fundamentally wrong syntax. 
#    The 'in' operator returns True/False, and 'True/False is not None' is always True. 
#    This means the condition is ALWAYS True, causing KeyError when trying to access 
#    employee["bonus"] for employees without bonus. This will CRASH the program.
# 2. MATHEMATICAL ERROR: Average calculation is completely wrong in second function.
#    Uses (salary1/count + salary2/count) instead of (salary1 + salary2)/count.
# 3. INCOMPLETE LOGIC: In second function, avg_salary_section is calculated but never 
#    added to avg_salary_dict, making that entire code block useless.
# 4. OVERWRITING VALUES: avg_salary_dict values are overwritten in each iteration.
# 5. MISSING REQUIRED OUTPUT: Third function doesn't return department paths as required.
# 6. ROOT DEPARTMENT IGNORED: Second function ignores root department employees.
# 7. PROGRAM CRASH: The syntax error will cause the program to crash with KeyError.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. Code duplication and poor structure.
# 3. Debug print statement left in production code.
# 4. Hardcoded strings instead of constants.
# 5. No error handling for missing keys.
# 6. Poor variable naming and formatting.
# 7. Unnecessary parentheses around iterables.

# Good Practices:
# 1. Extended nesting to handle 3 levels instead of 2.
# 2. Attempted to add bonus consideration to calculations.
# 3. Used round() function for better number formatting.
# 4. Type hints are present.
# 5. Functions are named descriptively.

# Detailed Analysis:
# This code has a CRITICAL syntax error that makes it completely non-functional:
#
# 1. CRITICAL FAILURE - Syntax Logic Error: The condition "if bonus in employee is not None" 
#    is the main issue. Here's what happens:
#    - 'bonus in employee' returns True if "bonus" key exists, False if it doesn't
#    - 'True is not None' evaluates to True (since True is not None)
#    - 'False is not None' evaluates to True (since False is not None)
#    - So the condition is ALWAYS True, regardless of whether bonus exists
#    
#    For employees WITHOUT bonus field:
#    - Condition evaluates to True
#    - Code tries to access employee["bonus"] 
#    - This causes KeyError and crashes the program
#
# 2. CRITICAL FAILURE - Program Will Not Run: Due to the syntax error above, the program 
#    will crash when processing any employee without a bonus field (like "CTO", "Dev1", etc.).
#
# 3. CRITICAL FAILURE - Wrong Average Calculation: Even if the syntax were fixed, the 
#    average calculation algorithm is fundamentally broken. It divides each individual 
#    salary by the total count instead of summing first then dividing.
#
# 4. CRITICAL FAILURE - Missing Required Functionality: The third function completely 
#    ignores the requirement to return department paths.
#
# 5. CRITICAL FAILURE - Incomplete Logic: The second function calculates avg_salary_section 
#    but never stores it, making that entire section of code meaningless.
#
# Test Case Failure Examples:
# - When processing "CTO" (no bonus): Will crash with KeyError
# - When processing "Dev1" (no bonus): Will crash with KeyError  
# - Average calculations will be wrong even if syntax is fixed
# - Department paths are completely missing from output
#
# Recommendations:
# 1. URGENT: Fix syntax to "if bonus in employee:" (remove "is not None")
# 2. Completely rewrite average calculation algorithm
# 3. Fix the overwriting issue in loops
# 4. Add department path tracking to third function
# 5. Include root department in calculations
# 6. Add comprehensive error handling
# 7. Add proper testing to catch these basic errors
# 8. Remove debug prints and add proper documentation
#
# This code represents a complete failure - it will not run due to syntax errors and 
# has fundamental algorithmic flaws. It requires a complete rewrite to be functional.