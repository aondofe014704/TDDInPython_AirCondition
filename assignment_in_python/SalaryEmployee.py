from commissionemployee import CommissionEmployee
from decimal import Decimal


class SalaryEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, rate, phone_number, sales, base_salary, ):
        super().__init__(first_name, last_name, phone_number, sales=sales, rate=rate)
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self.base_salary

    @base_salary.setter
    def base_salary(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError('Amount must be greater than 0')
        self.base_salary = amount

    def earnings(self):
        return self.base_salary + super().earnings()

    def __str__(self):
        return f"""
        {super().__str__()}
        Earning:{self.earnings()}
        Phone:{self.phone_number}        
        """


salaryCommission = SalaryEmployee('James', "Brown", 0.25, '080765', 25000, 15000)
anotherSalary = SalaryCommission('Kenny', 0.76, "0908765", 45000, "080765", 45000)
