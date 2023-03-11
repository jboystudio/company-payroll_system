class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class PayrollCalculator:
    def calculate_payroll(self):
        pass
        
class SalaryEmployee(Employee, PayrollCalculator):
    def __init__(self, id, name, salary):
        super().__init__(id, name)
        self.salary = salary
        
    def calculate_payroll(self):
        return self.salary
        
class HourlyEmployee(Employee, PayrollCalculator):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate
        
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, salary, commission_rate, sales):
        super().__init__(id, name, salary)
        self.commission_rate = commission_rate
        self.sales = sales
        
    def calculate_payroll(self):
        fixed_salary = super().calculate_payroll()
        commission = self.sales * self.commission_rate
        return fixed_salary + commission

# Now i will prompt the user to enter employee details
employee_type = input("Enter employee type (salary/hourly/commission): ")
id = int(input("Enter employee ID: "))
name = input("Enter employee name: ")

if employee_type == "salary":
    salary = float(input("Enter salary: "))
    employee = SalaryEmployee(id, name, salary)
elif employee_type == "hourly":
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    employee = HourlyEmployee(id, name, hours_worked, hourly_rate)
elif employee_type == "commission":
    salary = float(input("Enter salary: "))
    commission_rate = float(input("Enter commission rate: "))
    sales = float(input("Enter sales amount: "))
    employee = CommissionEmployee(id, name, salary, commission_rate, sales)
else:
    print("Invalid employee type.")
    exit()

# calculate payroll for the employee and print the result
payroll = employee.calculate_payroll()
print("Amount to be paid to", employee.name, ":", payroll)