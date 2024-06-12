import unittest
from assignment_in_python.ClassQueue import ClassQueue


class MyTestCase(unittest.TestCase):
    def test_That_Items_CanBe_Added_To_Queue(self):
        queue = ClassQueue()
        queue.add("Jack")
        queue.add("John")
        self.assertEqual(len(queue.queue), 2)

    def test_to_Add_numbers_To_Queue(self):
        queue = ClassQueue()
        queue.add(1)
        queue.add(2)
        self.assertEqual(len(queue.queue), 2)

    def test_to_Remove_Items_From_Queue(self):
        queue = ClassQueue()
        queue.add("Perry")
        queue.add("Dizzy")
        self.assertEqual(len(queue.queue), 2)
        queue.remove()
        self.assertEqual(len(queue.queue), 1)


if __name__ == '__main__':
    unittest.main()
