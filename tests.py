import unittest

from main import get_plain_list


class TestPlainIntegerList(unittest.TestCase):

    def test_plain_list_1(self):
        nested_list1 = [1, [2, [3, [4, 5]]]]
        plain_list1 = [1, 2, 3, 4, 5]
        self.assertEqual(get_plain_list(nested_list1, []), plain_list1)

    def test_plain_list_2(self):
        nested_list2 = [1, [2, [3, 4, [5, 6], 7]], 8, [9, 10]]
        plain_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(get_plain_list(nested_list2, []), plain_list2)

    def test_plain_list_3(self):
        nested_list3 = [1, [2, "a", ["b", 3, 4]]]
        wrong_plain_list3 = [1, 2, "a", "b", 3, 4]
        self.assertNotEqual(get_plain_list(nested_list3, []), wrong_plain_list3)


if __name__ == '__main__':
    unittest.main()