from decimal import Decimal


class CommissionEmployee:
    def __init__(self, first_name, last_name, phone_number, sales, rate):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self.sales = sales
        self.rate = rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def sales(self):
        return self._sales

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, value):
        if value < Decimal('0.00') and value > Decimal('1.0'):
            raise ValueError('rate must be between 0.0 and 1.0')
        self._rate = value



    @sales.setter
    def sales(self, value):
        if value < Decimal('0.00'):
            raise ValueError('Sales value Cannot Be Less Than Zero.')
        self._sales = value

    def earnings(self):
        return self.sales * self.rate

    def __str__(self):
        return f'{self.first_name} {self._last_name}{self._phone_number}{self.earnings():.2f}'


employeeOne = CommissionEmployee("Jack", " " 'Songu', " "  '0813360',   5000,    0.05)
print(employeeOne)
