import unittest
import os
from employee import Employee
from caesar_cipher import encrypt, decrypt, calculate_shift_from_id
from file_utils import load_employees, save_employees

class TestCaesarCipher(unittest.TestCase):
    def test_calculate_shift(self):
        self.assertEqual(calculate_shift_from_id("UHE12345"), 15)

    def test_encrypt(self):
        self.assertEqual(encrypt("5280", 15), "0735")

    def test_decrypt(self):
        self.assertEqual(decrypt("0735", 15), "5280")

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.emp = Employee("Jenny", "CEO", "5280", "E001", "UHE12345")

    def test_encrypt_decrypt_salary(self):
        self.emp.encrypt_salary()
        self.assertEqual(self.emp.salary, "0735")
        self.emp.decrypt_salary()
        self.assertEqual(self.emp.salary, "5280")

    def test_str_method(self):
        expected = "👤 Jenny - CEO - Salary: 5280 - ID: E001"
        self.assertEqual(str(self.emp), expected)

    def test_comparison(self):
        emp2 = Employee("Ana", "Engineer", "6000", "E002", "UHE12345")
        self.assertTrue(emp2 < self.emp)
        self.assertFalse(self.emp == emp2)

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        self.test_filename = "test_employees.txt"
        self.test_data = {
            "E001": Employee("Jenny", "CEO", "5280", "E001", "UHE12345"),
            "E002": Employee("Ana", "Engineer", "6000", "E002", "UHE12345")
        }
        save_employees(self.test_filename, self.test_data)

    def test_load_employees(self):
        loaded = load_employees(self.test_filename, "UHE12345")
        self.assertEqual(len(loaded), 2)
        self.assertIn("E001", loaded)
        self.assertEqual(loaded["E001"].name, "Jenny")

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

if __name__ == '__main__':
    unittest.main()
