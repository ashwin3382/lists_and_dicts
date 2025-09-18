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
def total_salary_budget(data: dict):
    budget = 0
    bonus = "bonus"
    for employee in data["employees"]:
        budget += employee["salary"]
        if bonus in employee is not None:
            budget += employee[bonus]

    for sub_department in data["sub_departments"]:
        for employee in sub_department["employees"]:
            budget += employee["salary"]
            if bonus in employee is not None:
                budget += employee[bonus]
        for unit in sub_department["sub_departments"]:
            for employee in unit["employees"]:
                budget += employee["salary"]
                if bonus in employee is not None:
                    budget += employee[bonus]
            for section in unit["sub_departments"]:
                for employee in section["employees"]:
                    budget += employee["salary"]
                    if bonus in employee is not None:
                        budget += employee[bonus]
    return budget

# Find the department (at any nesting level) with the highest average employee salary.
def dept_with_highest_avg_salary(data: dict):
    avg_salary_dict = {}
    bonus = "bonus"
    for sub_department in data["sub_departments"]:
        avg_salary_sub_dept = 0
        for unit in sub_department["sub_departments"]:
            avg_salary_unit = 0
            for employee in (unit["employees"]):
                if bonus in employee is not None:
                    avg_salary_unit += (employee["salary"]+employee[bonus])/ len(unit["employees"])
                else:
                    avg_salary_unit += employee["salary"]/len(unit["employees"])
                avg_salary_dict[unit["name"]] = avg_salary_unit
        for employees in (sub_department["employees"]):
            if bonus in employees is not None:
                avg_salary_sub_dept += (employees["salary"]+employees[bonus]) / len(sub_department["employees"])
            else:
                avg_salary_sub_dept += employees["salary"]/len(sub_department["employees"])
            avg_salary_dict[sub_department["name"]] = avg_salary_sub_dept
        for unit in sub_department["sub_departments"]:
            avg_salary_section = 0
            for section in (unit["sub_departments"]):
                for employee in (section["employees"]):
                    if bonus in employee is not None:
                        avg_salary_section += (employee["salary"]+employee[bonus])/len(section["employees"])
                    else:
                        avg_salary_section += employee["salary"]/len(section["employees"])


    return {"Department with highest average salary":max(avg_salary_dict, key = avg_salary_dict.get), "Average": max(avg_salary_dict.values())}

# List all employees who earn above the company-wide average salary, along with their department path.
def emp_with_higher_than_avg_salary(data: dict):
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
            for section in (unit["sub_departments"]):
                for employee in (section["employees"]):
                    employees_num += 1
    avg_company_wide_salary = round(total_budget_salary/employees_num, 2)
    print(avg_company_wide_salary)
    bonus = "bonus"
    for employee in (data["employees"]):
        if bonus in employee is not None:
            if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]
        elif employee["salary"] > avg_company_wide_salary:
            employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            if bonus in employee is not None:
                if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]
            elif employee["salary"] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
        for unit in (sub_department["sub_departments"]):
            for employee in (unit["employees"]):
                if bonus in employee is not None:
                    if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                        employees_with_higher_avg_salary[employee["name"]] = employee["salary"]+employee[bonus]
                elif employee["salary"] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
            for section in (unit["sub_departments"]):
                for employee in (section["employees"]):
                    if bonus in employee is not None:
                        if employee["salary"]+employee[bonus] > avg_company_wide_salary:
                            employees_with_higher_avg_salary[employee["name"]] = employee["salary"] + employee[bonus]
                    elif employee["salary"] > avg_company_wide_salary:
                        employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
    return employees_with_higher_avg_salary

