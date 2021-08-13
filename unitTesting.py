import unittest
import matches

class test(unittest.TestCase):
    def test_match(self):
        obj = matches(['abc'])
        find_str = input('Enter find string in list of stings:')
        objresult= obj.find('abc')

        self.assertEqual(objresult, ['abc'])