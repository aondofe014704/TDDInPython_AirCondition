from unittest import TestCase
from assignment_in_python import Bank


class TestBank(TestCase):
    def test_register(self):
        gtBank = Bank.Bank("Guaranty Trust Bank")
        gtBank.register("1234", "jack", "songu")
        self.assertEqual(len(gtBank.list_Of_Accounts), 1)

    def test_To_Find_Account_From_The_List_Of_Accounts(self):
        gtBank = Bank.Bank("Guaranty Trust Bank")
        gtBank.register("1234", "jack", "songu")
        self.assertEqual(len(gtBank.list_Of_Accounts), 1)
        value = gtBank.findByAccountNumber(0O123456701)
        self.assertEqual(value.get_first_name(), "jack")
        gtBank.register("1234", "jack1", "songu1")
        self.assertEqual(len(gtBank.list_Of_Accounts), 2)
        value1 = gtBank.findByAccountNumber(0O123456702)
        self.assertEqual(value1.get_first_name(), "jack1")

    def test_To_Transfer_From_One_Account_To_Another(self):
        gtBank = Bank.Bank("Guaranty Trust Bank")
        gtBank.register("1234", "Danny", "Young")
        self.assertEqual(len(gtBank.list_Of_Accounts), 1)
        gtBank.register("0147", "Johnny", "Cage")
        self.assertEqual(len(gtBank.list_Of_Accounts), 2)

        gtBank.deposit(0O123456701,6_000)
        self.assertEqual(6_000, gtBank.get_balance(0O123456701))
        gtBank.transfer(0O123456701, 0O123456702, 6_000, "1234")
        self.assertEqual(0, gtBank.get_balance(0O123456701))

