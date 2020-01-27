import unittest


class TestTime(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        print('Setup class')

    @classmethod
    def tearDownClass(cls):
        print('Teardown class')
