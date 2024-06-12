class AccountTestingAgain:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.pin = ""
        self.__balance = 0.0

    def set_first_name(self, first_name: str) -> None:
        self.first_name = first_name

    def set_last_name(self, last_name: str) -> None:
        self.last_name = last_name

    def get_balance(self) -> float:
        return self.__balance

    def set_pin(self, pin: str) -> None:
        self.pin = pin

    def deposit(self, amount):
        if amount <= 0.0:
            raise ValueError("Deposit Amount must be greater than Zero")
        if amount > self.__balance:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient Balance")
        if amount < self.__balance:
            self.__balance -= amount

        pass
