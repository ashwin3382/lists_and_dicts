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
        {"name": "CEO", "salary": 250000, "bonus": 50000, "type": "permanent"},
        {"name": "CTO", "salary": 200000, "type": "permanent"}
    ],
    "sub_departments": [
        {
            "name": "Engineering",
            "employees": [
                {"name": "Lead", "salary": 150000, "bonus": 20000, "type": "permanent"},
                {"name": "Dev1", "salary": 110000, "type": "contract"},
                {"name": "Dev2", "salary": 115000, "bonus": 10000, "type": "permanent"},
                {"name": "Intern", "salary": 30000, "type": "intern"}
            ],
            "sub_departments": [
                {
                    "name": "QA",
                    "employees": [
                        {"name": "Test1", "salary": 90000, "type": "permanent"},
                        {"name": "Test2", "salary": 95000, "bonus": 5000, "type": "contract"}
                    ],
                    "sub_departments": [
                        {
                            "name": "Automation",
                            "employees": [
                                {"name": "Auto1", "salary": 99000, "type": "permanent"}
                            ],
                            "sub_departments": []
                        }
                    ]
                },
                {
                    "name": "DevOps",
                    "employees": [
                        {"name": "Ops1", "salary": 105000, "bonus": 5000, "type": "contract"},
                        {"name": "Ops2", "salary": 108000, "type": "permanent"}
                    ],
                    "sub_departments": []
                }
            ]
        },
        {
            "name": "HR",
            "employees": [
                {"name": "HR1", "salary": 60000, "type": "permanent"},
                {"name": "HR2", "salary": 65000, "type": "permanent"},
                {"name": "Recruiter", "salary": 48000, "type": "contract"}
            ],
            "sub_departments": [
                {
                    "name": "Training",
                    "employees": [
                        {"name": "Trainer1", "salary": 50000, "type": "permanent"},
                        {"name": "Trainer2", "salary": 52000, "bonus": 1000, "type": "permanent"}
                    ],
                    "sub_departments": []
                }
            ]
        },
        {
            "name": "Marketing",
            "employees": [
                {"name": "Mark1", "salary": 70000, "type": "permanent"},
                {"name": "Mark2", "salary": 72000, "type": "contract"}
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
            budget += employee["bonus"]

    for sub_department in data["sub_departments"]:  # CRITICAL: KeyError if "sub_departments" key doesn't exist
        for employee in sub_department["employees"]:
            budget += employee["salary"]
            if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                budget += employee["bonus"]
        for unit in sub_department["sub_departments"]:
            for employee in unit["employees"]:
                budget += employee["salary"]
                if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                    budget += employee["bonus"]
            for section in unit["sub_departments"]:  # PRACTICE: Good improvement - handles 3 levels now
                for employee in section["employees"]:
                    budget += employee["salary"]
                    if bonus in employee is not None:  # CRITICAL: Same logical error repeated
                        budget += employee["bonus"]
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
print(emp_with_higher_than_avg_salary(company))  # PRACTICE: Should be in main block


# ------ Grading Report ------
# Grade: 1.5 / 10

# Critical Issues:
# 1. SYNTAX ERROR: "if bonus in employee is not None" is fundamentally wrong syntax. 
#    The 'in' operator returns True/False, and 'True is not None' is always True, 
#    'False is not None' is always True. This means the condition is ALWAYS True, 
#    causing KeyError when trying to access employee["bonus"] for employees without bonus.
# 2. MATHEMATICAL ERROR: Average calculation is still completely wrong in second function.
#    Still uses (salary1/count + salary2/count) instead of (salary1 + salary2)/count.
# 3. INCOMPLETE LOGIC: In second function, avg_salary_section is calculated but never 
#    added to avg_salary_dict, making that entire code block useless.
# 4. OVERWRITING VALUES: avg_salary_dict values are still overwritten in each iteration.
# 5. MISSING REQUIRED OUTPUT: Third function still doesn't return department paths.
# 6. ROOT DEPARTMENT IGNORED: Second function still ignores root department employees.

# Practice Issues:
# 1. Missing docstrings for all functions.
# 2. Code duplication and poor structure.
# 3. Debug print statement left in production code.
# 4. Hardcoded strings instead of constants.
# 5. No error handling for missing keys.
# 6. Poor variable naming and formatting.

# Good Practices:
# 1. Extended nesting to handle 3 levels instead of 2.
# 2. Added bonus consideration to calculations.
# 3. Used round() function for better number formatting.
# 4. Type hints are present.

# Detailed Analysis:
# This code has a CRITICAL syntax error that makes it completely non-functional:
#
# 1. CRITICAL FAILURE - Syntax Logic Error: The condition "if bonus in employee is not None" 
#    is syntactically valid Python but logically wrong. The 'in' operator returns a boolean, 
#    and any boolean 'is not None' is always True. This means:
#    - For employees WITH bonus: condition is True, code tries employee["bonus"] ✓
#    - For employees WITHOUT bonus: condition is STILL True, code tries employee["bonus"] ✗ CRASH
#    
#    This will cause KeyError crashes for any employee without a bonus field.
#
# 2. CRITICAL FAILURE - The average calculation in the second function is still 
#    mathematically incorrect and uses the same flawed algorithm as before.
#
# 3. CRITICAL FAILURE - The second function has incomplete logic where avg_salary_section 
#    is calculated but never stored in the results dictionary.
#
# 4. CRITICAL FAILURE - The third function completely ignores the requirement to return 
#    department paths along with employee information.
#
# 5. The code will crash when executed due to the syntax error, making it completely 
#    non-functional despite the attempt to handle bonuses and deeper nesting.
#
# Recommendations:
# 1. Fix the bonus checking syntax to: "if bonus in employee:"
# 2. Fix the average calculation algorithm completely.
# 3. Store calculated averages properly without overwriting.
# 4. Add department path tracking to the third function.
# 5. Include root department in average calculations.
# 6. Add proper error handling and input validation.
# 7. Remove debug print statements and add proper logging if needed.
# 8. Add comprehensive testing to catch these basic errors.
#
# This code fails to meet basic functionality requirements and contains critical 
# syntax errors that prevent execution. It requires a complete rewrite of the 
# logic and syntax correction.