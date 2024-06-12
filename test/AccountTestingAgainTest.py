import unittest
from assignment_in_python.AccountTestingAgain import AccountTestingAgain


class MyTestCase(unittest.TestCase):
    def test_That_Account_Can_Be_Created(self):
        account = AccountTestingAgain("Mary", "Clark")
        account.set_pin("0147")
        self.assertEqual("Mary", account.first_name, "Clark")

    def test_To_Deposit_Money(self):
        account = AccountTestingAgain("Mary", "Clark")
        account.deposit(20_000)
        self.assertEqual(20_000, account.get_balance())

    def test_That_Negative_Amount_Can_Be_Deposited(self):
        account = AccountTestingAgain("Mary", "Clark")
        self.assertRaises(ValueError, lambda: account.deposit(-10_000))

    def test_To_withdraw_Money(self):
        account = AccountTestingAgain("Mary", "Clark")
        account.deposit(7_000)
        self.assertEqual(7_000, account.get_balance())
        account.withdraw(5_000)
        self.assertEqual(2_000, account.get_balance())

    def test_That_withdraw_Amount_Can_Be_Negative(self):
        account = AccountTestingAgain("Mary", "Clark")
        account.deposit(6_000)
        self.assertEqual(6_000, account.get_balance())
        account.withdraw(-7000)
        self.assertRaises(ValueError, lambda: account.deposit(-7000))


if __name__ == '__main__':
    unittest.main()
