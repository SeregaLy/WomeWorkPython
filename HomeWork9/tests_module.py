import unittest
from scripts_module import *


class Test_Functions(unittest.TestCase):

    def test_salary(self):
        self.assertEqual(salary(160, 700, 10000), 122000)

    def test_salary2(self):
        self.assertNotEqual(salary(160, 700, 1000), 122000)

    def test_salary3(self):
        self.failureException(salary(160, 'Dollar', 1000),
                              'один из аргументов имеет не числовой формат')

    def test_sum(self):
        self.assertEqual(sum_two_max(200, 300, 100), 500)

    def test_sum2(self):
        self.assertNotEqual(sum_two_max(100, 400, 200), 500)

    def test_title(self):
        self.assertEqual(title_func('google'), 'Google')

    def testmyfunccount1(self):
        self.assertIn(4, gen_num(2, 7))

    def testmyfunccount2(self):
        self.assertNotIn(8, gen_num(2, 7))


if __name__ == '__main__':
    unittest.main()
