import unittest
from matches import matches

class test(unittest.TestCase):
    def test_case1(self):
        obj1 = matches(["helloworld","foo","bar","stylight_team","seo"])
        objresult= obj1.find('eos')
        self.assertEqual(objresult, ['seo'])
        
    def test_case2(self):
        obj2 = matches(['abc'])
        objresult= obj2.find('abc')
        self.assertEqual(objresult, ['abc'])

    def test_case3(self):
        obj3 = matches(['1'])
        objresult= obj3.find('1')
        self.assertEqual(objresult, ['1'])
    
    def test_case4(self):
        obj4 = matches(["helloworld","oof","foo","bar","stylight_team"])
        objresult4= obj4.find('foo')
        self.assertTrue(objresult4 ==['oof', "foo"] or objresult4 ==['foo', "oof"])

    def test_case5(self):
        obj5 = matches(1)
        objresult= obj5.find(1)
        self.assertEqual(objresult, 'User should enter valid input list of string details')
    
    def test_case6(self):
        obj6 = matches('1')
        objresult= obj6.find(1)
        self.assertEqual(objresult, 'User should enter valid find string details')

if __name__=='__main__':
    unittest.main()