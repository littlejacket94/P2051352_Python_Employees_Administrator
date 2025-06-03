from employee import Employee

def load_employees(filename, student_id):
    employees = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, position, salary, emp_id = line.split(',')
            emp = Employee(name, position, salary, emp_id, student_id)
            employees[emp_id] = emp
    return employees

def save_employees(filename, employees):
    with open(filename, 'w') as file:
        for emp in employees.values():
            file.write(f"{emp.name},{emp.position},{emp.salary},{emp.employee_id}\n")
