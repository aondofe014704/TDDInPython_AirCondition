class CommissionEmployeeTwo:
    def __init__(self, first_name, last_name, phone_number, email, rate, sales):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email
        self.rate = rate
        self.sales = sales

    @property
    def fname(self):
        return self._first_name

    @property
    def lname(self):
        return self._last_name
