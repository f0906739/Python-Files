import unittest
from testfile import CarNova


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

    @classmethod
    @print_func_name
    def setUp(self):
        self.shop_1 = CarNova

    @classmethod
    @print_func_name
    def tearDown(self):
        print()

    @print_func_name
    def test_append_multiple_cars(self):
        len_before = len(self.shop_1.cars)

        num = 100
        self.shop_1.append_multiple_cars(self.shop_1, num)

        len_after = len(self.shop_1.cars)

        self.assertEqual(num, len_after - len_before)

        self.shop_1.append_multiple_cars(self.shop_1, 100)
        for car in self.shop_1.cars.values():
            print(car.color)
            self.assertTrue(car.color != "blue")

            print(car.make)
            self.assertTrue(car.make != "honda")

            print(car.car_type)
            self.assertTrue(car.car_type != "truck")

    # @print_func_name
    # def test_get_data(self):
    #     cars = []
    #     for car in self.shop_1.append_multiple_cars(self.shop_1,100):
    #         cars.append(car)
    #     for car in cars:
    #         self.assert


if __name__ == '__main__':
    unittest.main()
