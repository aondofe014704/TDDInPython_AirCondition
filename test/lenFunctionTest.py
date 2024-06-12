import unittest


class FunctionClass(unittest.TestCase):

    def test_to_return_length_of_Argument(self):
        functionClass = FunctionClass()
        functionClass.to_return()
        self.assertEqual(5, self.to_return())

    def to_return(self):
        return len("Hello")




