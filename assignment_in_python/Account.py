class Account:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__balance = 0.0
        self.pin = ""
        self.account_number = 0

    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def get_balance(self) -> float:
        return self.__balance

    def set_pin(self, pin: str) -> None:
        self.pin = pin

    def get_pin(self) -> str:
        return self.pin

    def get_first_name(self) -> str:
        return self.first_name

    def get_last_name(self) -> str:
        return self.last_name

    def deposit(self, amount):
        if amount < 0.0:
            raise ValueError("Amount cannot be less than Zero")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        if amount <= self.__balance:
            self.__balance -= amount

    def set_account_number(self, account_number: int) -> None:
        self.account_number = account_number

    def get_account_number(self) -> int:
        return self.account_number





