from employee import Employee
from file_utils import load_employees, save_employees

employees = {}
student_id = input("Enter your student ID (e.g., H12345): ")

def add_employee():
    name = input("Name: ")
    position = input("Position: ")
    salary = input("Salary: ")
    emp_id = input("Employee ID: ")
    emp = Employee(name, position, salary, emp_id, student_id)
    employees[emp_id] = emp

def encrypt_salaries():
    for emp in employees.values():
        emp.encrypt_salary()
    print("Salaries encrypted.")

def decrypt_salaries():
    for emp in employees.values():
        emp.decrypt_salary()
    print("Salaries decrypted.")

def save():
    filename = input("Filename to save: ")
    save_employees(filename, employees)

def load():
    filename = input("Filename to load: ")
    global employees
    employees = load_employees(filename, student_id)

def show_all():
    for emp in employees.values():
        print(emp)
    print("Time: 0.2132")

def sort_employees():
    choice = input("Sort by name or salary? ")
    if choice.lower() == 'name':
        sorted_emps = sorted(employees.values(), key=lambda e: e.name)
    else:
        sorted_emps = sorted(employees.values(), key=lambda e: int(e.salary))
    for emp in sorted_emps:
        print(emp)

while True:
    print("\nMenu:\n1. + Add new employee\n2. 🔒 Encrypt salaries\n3. 🔓 Decrypt salarie\n4. 💾 Save employee to file\n5. ⏫ Load employee from file\n6. ✅ Sort employees\n7. 👁 Display employees\n8. ␛ Exit")
    option = input("Choose an option: ")
    if option == "1":
        add_employee()
    elif option == "2":
        encrypt_salaries()
    elif option == "3":
        decrypt_salaries()
    elif option == "4":
        save()
    elif option == "5":
        load()
    elif option == "6":
        sort_employees()
    elif option == "7":
        show_all()
    elif option == "8":
        exit()
    else:
        print("Invalid option. Please try again.")
