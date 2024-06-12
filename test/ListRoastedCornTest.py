import unittest
from assignment_in_python.RoastedCornReal import RoastedCornReal


class MyTestCase(unittest.TestCase):
    def test_to_generate_list_a_list_of_ten_numbers(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        self.assertEqual(10, len(roastedCornReal.generateList))

    def test_to_count_the_number_of_items_in_the_List(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        self.assertEqual(10, roastedCornReal.countElements())

    def test_to_sum_up_All_the_elements_on_Even_Position(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        self.assertEqual(180, roastedCornReal.sumOfEvenPosition())

    def test_to_sum_up_All_the_elements_on_Odd_Position(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        self.assertEqual(175, roastedCornReal.sumOfOddPosition())

    def test_multiply_Elements_on_Third_Position(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        roastedCornReal.multiply3rdPositionElements()
        self.assertEqual(1559920, roastedCornReal.multiply3rdPositionElements())

    def test_to_calculate_the_average_of_all_the_elements_in_the_list(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        roastedCornReal.calculateAverage()
        self.assertEqual(3.55, roastedCornReal.calculateAverage())

    def test_to_get_the_largest_elements_in_the_list(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        roastedCornReal.largestElement()
        self.assertEqual(40, roastedCornReal.largestElement())

    def test_to_get_the_smallest_elements_in_the_list(self):
        roastedCornReal = RoastedCornReal()
        roastedCornReal.createList()
        roastedCornReal.smallestElement()
        self.assertEqual(31, roastedCornReal.smallestElement())

    def test_to_return_the_first_and_last_characters_of_A_given_Strings(self):
        roastedCornReal = RoastedCornReal()
        self.assertEqual(["mum", "dad", "omo"],
                         roastedCornReal.createStringList(["name", "mum", "dad", "church", "omo"]))

    def test_to_construct_a_sequential_list_of_integers(self):
        roastedCornReal = RoastedCornReal()
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                         roastedCornReal.sequentialList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))




if __name__ == '__main__':
    unittest.main()
