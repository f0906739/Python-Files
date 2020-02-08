import unittest
from Beaver import Time, Beaver


class TestTime(unittest.TestCase):
    def setUp(self):
        self.time = Time(1, 73, 63)

    def tearDown(self):
        print("tearDown\n")

    @classmethod
    def setUpClass(cls):
        print('Setup class\n')

    @classmethod
    def tearDownClass(cls):
        print('Teardown class\n')

    def test_calculate_time(self):
        self.time.calculate_time()

        self.assertEqual(self.time.minutes, 3)
        self.assertEqual(self.time.hours, 2)
        self.assertEqual(self.time.days, 4)


if __name__ == '__main__':
    unittest.main()
