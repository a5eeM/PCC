import unittest
from ex_employee import Employee

class TestEmployee(unittest.TestCase):
    """
    Test for the class Employee.
    """

    def setUp(self):
        """
        Create an employee to be used in all test methods.
        """
        self.employee = Employee("Edward", "Stone", 120000)
    
    def test_give_default_raise(self):
        """
        Test that default raise is given properly.
        """
        raise_given = self.employee.give_raise()
        self.assertEqual(raise_given, self.employee.annual_salary)
    
    def test_give_custom_raise(self):
        """
        Test that a custom raise is given properly.
        """
        amount = 20000
        raise_given = self.employee.give_raise(amount)
        self.assertEqual(raise_given, self.employee.annual_salary)

unittest.main()
