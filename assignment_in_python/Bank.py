from assignment_in_python.Account import Account


class Bank:

    def __init__(self, bank_name: str):
        self.bank_name = bank_name
        self.list_Of_Accounts = []
        self.account_number = 0O123456700

    def register(self, pin, first_name, last_name):
        myAccount = Account(first_name, last_name)
        myAccount.set_pin(pin)
        myAccount.set_account_number(self.generate_account_number())
        self.list_Of_Accounts.append(myAccount)

    def findByAccountNumber(self, account_number) -> Account:
        for account in self.list_Of_Accounts:
            if account.get_account_number() == account_number:
                return account

    def deposit(self, account_number, amount):
        for account in self.list_Of_Accounts:
            if account.get_account_number() == account_number:
                account.deposit(amount)
                break

    def withdraw(self, account_number, amount):
        for account in self.list_Of_Accounts:
            if account.get_account_number() == account_number:
                account.withdraw(amount)
                break

    def generate_account_number(self):
        self.account_number = self.account_number + 1
        return self.account_number

    def get_balance(self, account_number):
        for account in self.list_Of_Accounts:
            if account.get_account_number() == account_number:
                return account.get_balance()

    def transfer(self, senderAccount, receiverAccount, amount, pin):
        for account in self.list_Of_Accounts:
            if account.get_account_number() == senderAccount:
                if account.get_pin() == pin:
                    account.withdraw(amount)

        for account in self.list_Of_Accounts:
            if account.get_account_number() == receiverAccount:
                account.deposit(amount)
