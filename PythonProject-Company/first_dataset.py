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
def total_salary_budget(data: dict):
    budget = 0
    for employee in data["employees"]:
        budget += employee["salary"]
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            budget += employee["salary"]
        for unit in (sub_department["sub_departments"]):
            for employee in unit["employees"]:
                budget += employee["salary"]
    return budget

# Find the department (at any nesting level) with the highest average employee salary.
def dept_with_highest_avg_salary(data: dict):
    avg_salary_dict = {}

    for sub_department in data["sub_departments"]:
        avg_salary_sub_dept = 0
        for unit in sub_department["sub_departments"]:
            avg_salary_unit = 0
            for employee in (unit["employees"]):
                avg_salary_unit += employee["salary"] / len(unit["employees"])
                avg_salary_dict[unit["name"]] = avg_salary_unit
        for employees in (sub_department["employees"]):
            avg_salary_sub_dept += employees["salary"] / len(sub_department["employees"])
            avg_salary_dict[sub_department["name"]] = avg_salary_sub_dept
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
    avg_company_wide_salary = total_budget_salary/employees_num

    for employee in (data["employees"]):
        if employee["salary"] > avg_company_wide_salary:
            employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
    for sub_department in data["sub_departments"]:
        for employee in (sub_department["employees"]):
            if employee["salary"] > avg_company_wide_salary:
                employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
        for unit in (sub_department["sub_departments"]):
            for employee in (unit["employees"]):
                if employee["salary"] > avg_company_wide_salary:
                    employees_with_higher_avg_salary[employee["name"]] = employee["salary"]
    return employees_with_higher_avg_salary
