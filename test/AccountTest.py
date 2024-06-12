import unittest
from assignment_in_python.Account import Account


class MyTestCase(unittest.TestCase):
    def test_That_Account_Can_Be_Created(self):
        account = Account("james", "brown")
        account.set_pin("1234")
        self.assertEqual("james", account.get_first_name(), "The first name is james")
        self.assertEqual("brown", account.get_last_name(), "The last name is brown")
        self.assertEqual("1234", account.get_pin())

    def test_To_Deposit_Money(self):
        account = Account("james", "Perry")
        account.set_pin("0147")
        account.deposit(5_000)
        self.assertEqual(5_000, account.get_balance())

    def test_That_Deposit_Amount_Cannot_Be_A_Negative_Amount(self):
        account = Account("james", "Wizz")
        account.set_pin("1234")
        self.assertRaises(ValueError, lambda: account.deposit(-4_000))

    def test_To_withdraw_Money(self):
        account = Account("Pauline", "LinePaul")
        account.set_pin("0147")
        account.deposit(14_000)
        self.assertEqual(14_000, account.get_balance())
        account.withdraw(7_000)
        self.assertEqual(7_000, account.get_balance())

    def test_That_withdraw_Amount_Cannot_withdraw_Above_Balance(self):
        account = Account("Pedri", "Gonzalez")
        account.set_pin("014704")
        account.deposit(9_000)
        self.assertEqual(9_000, account.get_balance())
        self.assertRaises(ValueError, lambda: account.withdraw(17_000))


if __name__ == '__main__':
    unittest.main()
