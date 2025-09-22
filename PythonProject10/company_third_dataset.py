# Compute the total salary budget for the entire company.
# Find the department (at any nesting level) with the highest average employee salary.
# List all employees who earn above the company-wide average salary, along with their department path.

from typing import Final
BONUS: Final[str] = "bonus"

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
    try:
        for employee in data["employees"]:
            budget += employee["salary"] + employee.get(BONUS, 0)

        for sub_department in data["sub_departments"]:
            for employee in sub_department["employees"]:
                budget += employee["salary"] + employee.get(BONUS, 0)
            for unit in sub_department["sub_departments"]:
                for employee in unit["employees"]:
                    budget += employee["salary"] + employee.get(BONUS, 0)
                for section in unit["sub_departments"]:
                    for employee in section["employees"]:
                        budget += employee["salary"] + employee.get(BONUS, 0)
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    total_budget = {"Total Budget": budget}
    return total_budget

# Find the department (at any nesting level) with the highest average employee salary.
def dept_with_highest_avg_salary(data: dict):
    avg_salary_of_departments = {}
    total_salary_hq = 0
    try:
        for root_department in data["employees"]:
            total_salary_hq += root_department["salary"]
        avg_salary_of_departments[data["name"]] = round(total_salary_hq / len(data["employees"]), 2)

        for sub_department in data["sub_departments"]:
            total_salary_sub_departments = 0
            count_sub_department = 0
            for employee in sub_department["employees"]:
                count_sub_department += 1
                total_salary_sub_departments += employee["salary"]
            avg_salary_of_departments[sub_department["name"]] = round(
                total_salary_sub_departments / count_sub_department, 2)

            for section in sub_department["sub_departments"]:
                total_salary_sections = 0
                count_section = 0
                for employee in section["employees"]:
                    count_section += 1
                    total_salary_sections += employee["salary"]
                avg_salary_of_departments[section["name"]] = round(total_salary_sections / count_section, 2)

                for unit in section["sub_departments"]:
                    total_salary_units = 0
                    count_unit = 0
                    for employee in unit["employees"]:
                        count_unit += 1
                        total_salary_units += employee["salary"]
                    avg_salary_of_departments[unit["name"]] = round(total_salary_units / count_unit, 2)
    except KeyError as missing_key:
        return f"Key: {missing_key} not found."

    department_with_highest_avg_salary = {max(avg_salary_of_departments, key = avg_salary_of_departments.get) : max(avg_salary_of_departments.values())}
    return department_with_highest_avg_salary

# List all employees who earn above the company-wide average salary, along with their department path.
def emp_with_higher_than_avg_salary(data: dict):
    total_budget = 0
    try:
        for v in total_salary_budget(data).values():
            total_budget = v
        employee_count = 0

        for employee in data["employees"]:
            employee_count += 1
        for sub_department in data["sub_departments"]:
            for employee in (sub_department["employees"]):
                employee_count += 1
            for unit in (sub_department["sub_departments"]):
                for employee in (unit["employees"]):
                    employee_count += 1
                for section in (unit["sub_departments"]):
                    for employee in (section["employees"]):
                        employee_count += 1

        avg_company_wide_salary = round(total_budget / employee_count, 2)
        employees_with_higher_than_average_salary = {}

        for employee in data["employees"]:
            if employee["salary"] + employee.get(BONUS, 0) > avg_company_wide_salary:
                if data["name"] not in employees_with_higher_than_average_salary:
                    employees_with_higher_than_average_salary[data["name"]] = [
                        {employee["name"]: employee["salary"] + employee.get(BONUS, 0)}
                    ]
                else:
                    for v in employees_with_higher_than_average_salary.values():
                        v.append({employee["name"]: employee["salary"] + employee.get(BONUS, 0)})

        for sub_department in data["sub_departments"]:
            for employee in sub_department["employees"]:
                if employee["salary"] + employee.get(BONUS, 0) > avg_company_wide_salary:
                    if sub_department["name"] not in employees_with_higher_than_average_salary:
                        employees_with_higher_than_average_salary[sub_department["name"]] = [
                            {employee["name"]: employee["salary"] + employee.get(BONUS, 0)}
                        ]
                    else:
                        for k, v in employees_with_higher_than_average_salary.items():
                            if k == sub_department["name"]:
                                v.append({employee["name"]: employee["salary"] + employee.get(BONUS, 0)})

            for unit in sub_department["sub_departments"]:
                for employee in unit["employees"]:
                    if employee["salary"] + employee.get(BONUS, 0) > avg_company_wide_salary:
                        if unit["name"] not in employees_with_higher_than_average_salary:
                            employees_with_higher_than_average_salary[unit["name"]] = [
                                {employee["name"]: employee["salary"] + employee.get(BONUS, 0)}
                            ]
                        else:
                            for k, v in employees_with_higher_than_average_salary.items():
                                if k == unit["name"]:
                                    v.append({employee["name"]: employee["salary"] + employee.get(BONUS, 0)})

                for section in unit["sub_departments"]:
                    for employee in section["employees"]:
                        if employee["salary"] + employee.get(BONUS, 0) > avg_company_wide_salary:
                            if section["name"] not in employees_with_higher_than_average_salary:
                                employees_with_higher_than_average_salary[section["name"]] = [
                                    {employee["name"]: employee["salary"] + employee.get(BONUS, 0)}
                                ]
                            else:
                                for k, v in employees_with_higher_than_average_salary.items():
                                    if k == section["name"]:
                                        v.append({employee["name"]: employee["salary"] + employee.get(BONUS, 0)})

    except KeyError or ZeroDivisionError as missing_key:
        if KeyError:
            return f"Key: {missing_key} not found."
        else:
            return f"Employee count is 0!!"

    return employees_with_higher_than_average_salary




if __name__ == "__main__":
    print(total_salary_budget(company))
    print(dept_with_highest_avg_salary(company))
    print(emp_with_higher_than_avg_salary(company))