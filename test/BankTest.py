from unittest import TestCase
from assignment_in_python import Bank


class TestBank(TestCase):
    def test_register(self):
        gtBank = Bank.Bank("G_T_B")
        gtBank.register("1234", "jack", "songu")
        self.assertEqual(len(gtBank.list_Of_Accounts), 1)
