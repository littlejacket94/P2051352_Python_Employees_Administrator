from caesar_cipher import calculate_shift_from_id, encrypt, decrypt

class Employee:
    def __init__(self, name, position, salary, employee_id, student_id):
        self.name = name
        self.position = position
        self.salary = str(salary)
        self.employee_id = employee_id
        self.student_id = student_id
        self.shift = calculate_shift_from_id(student_id)

    def __str__(self):
        return f"👤 {self.name} - {self.position} - Salary: {self.salary} - ID: {self.employee_id}"

    def __lt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.employee_id == other.employee_id

    def encrypt_salary(self):
        self.salary = encrypt(self.salary, self.shift)

    def decrypt_salary(self):
        self.salary = decrypt(self.salary, self.shift)
