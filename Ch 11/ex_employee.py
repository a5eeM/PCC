class Employee():
    """
    An employee class.
    """

    def __init__(self, first, last, annual_salary):
        """
        Initialize attributes.
        """
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_given=5000):
        """
        Raise for an employee.
        """
        self.annual_salary += raise_given
        return self.annual_salary
