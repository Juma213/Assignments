# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 16:45:11 2024

@author: George Juma
"""

# Base class for all employees
class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Base Salary: Ksh.{self.base_salary}"

    def calculate_salary(self):
        return self.base_salary


# Full-time employee class
class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits

    def __str__(self):
        return f"Full-Time {super().__str__()}, Benefits: Ksh.{self.benefits}"

    def calculate_salary(self):
        return self.base_salary + self.benefits


# Part-time employee class
class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        # Base salary is calculated by multiplying hourly rate by hours worked
        super().__init__(name, employee_id, hourly_rate * hours_worked)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return f"Part-Time {super().__str__()}, Hourly Rate: Ksh.{self.hourly_rate}, Hours Worked: {self.hours_worked}"

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Company class to manage employees
class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print("No employees in the company.")
        else:
            print("\nEmployee Details:")
            for employee in self.employees:
                print(employee)

    def calculate_total_salary(self):
        total_salary = sum(employee.calculate_salary() for employee in self.employees)
        return total_salary


# Example Usage
if __name__ == "__main__":
    # Creating a company
    company = Company()

    # Adding employees to the company
    emp1 = FullTimeEmployee("Stephen", "E001", 50000, 10000)
    emp2 = PartTimeEmployee("Gina", "E002", 20, 100)
    company.add_employee(emp1)
    company.add_employee(emp2)

    # Displaying employees
    company.display_employees()

    # Calculating total salary expense
    total_salary = company.calculate_total_salary()
    print(f"\nTotal Salary Expense: Ksh.{total_salary}")
