


import unittest


class Test(unittest.TestCase):
    def setUp(self):
        self.a=5
        self.string='string'
        self.list=[1,2,3,4,5]




    def test_equalization_parameters(self):
        s='anderson masese'
        self.assertEqual('anderson',longest(s))

    
    def test_setup(self):
        self.assertEqual(self.a,6,'value is not equal to six')

    def test_is_string(self):
        self.assertIsInstance(self.string,str)

    #using the true and false assertion
    def test_not_not_true_progression(self):
        self.assertTrue(4*4==16)
    def test_list_comprehension(self):


        self.assertIn(1,self.list)
    def test_greater(self):
        t=4
        self.assertGreater(5,t)

   