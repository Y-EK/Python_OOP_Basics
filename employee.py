import datetime
from datetime import date

class Employee:

    # class attributes
    num_of_emps = 0
    raise_amount = 1.04
    
    # Dunder Methods
    # contructor
    def __init__(self, fname, lname, pay):
        # instance variables
        self.fname = fname 
        self.lname = lname
        self.pay = pay
        
        Employee.num_of_emps += 1

    # Object Representation: __str__, __repr__
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.fname, self.lname, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    # returns the sum of pays of two employees
    # by using: print(emp_1 + emp_2)
    def __add__(self, other):
        return self.pay + other.pay
        
    # returns the length of the fullname of an employee 
    # ex: print(len(emp_1))
    def __len__(self):
        return len(self.fullname())      

    # Object Methods
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    # getter methods
    @property
    def email(self):
        return '{}.{}@mycompany.com'.format(self.fname, self.lname)

    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    # setter methods

    @fullname.setter
    def fullname(self, name):
        fn, ln = name.split(' ')
        self.fname = fn
        self.lname = ln  
        
    # DELETER
    # ex: del emp_1.fullname
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.fname = None
        self.lname = None 

    # Class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, pay = emp_str.split('-')
        return cls(fname, lname, pay)

    # Static methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True