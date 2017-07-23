import unittest
from models.trial import my_func
class MyTest(unittest.TestCase):
    def test_my_func(self):
        self.assertEqual(5,my_func())