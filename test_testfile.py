import unittest
from testfile import CarChoices, Car, Shop, CarNova, PorscheDealer, Oldies, Bidders

def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


class TestCarNova(unittest.TestCase):

    @classmethod
    @print_func_name
    def setUpClass(cls):
        print(end="")

    @classmethod
    @print_func_name
    def tearDownClass(cls):
        print(end="")

    @print_func_name
    def setUp(self):
        self.shop_1 = CarNova

    @print_func_name
    def tearDown(self):
        print()

    @print_func_name
    def test_append_multiple_cars(self):
        len_before = len(self.shop_1.cars)

        num = 100
        self.shop_1.append_multiple_cars(self.shop_1, num)

        len_after = len(self.shop_1.cars)

        self.assertEqual(num, len_after-len_before)
    
    @print_func_name
    def test_get_data(self):
        pass

if __name__ == '__main__':
    unittest.main()
