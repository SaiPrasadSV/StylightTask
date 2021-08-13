import unittest  #Unitest framework to test the different scenarios 
from matches import matches  

class test(unittest.TestCase):
    def test_case1(self):  #TestCase1 : Random string 
        obj1 = matches(["helloworld","foo","bar","stylight_team","seo"])
        objresult= obj1.find('eos')
        self.assertEqual(objresult, ['seo'])
        
    def test_case2(self):  #TestCase2 : Single value 
        obj2 = matches(['abc'])
        objresult= obj2.find('abc')
        self.assertEqual(objresult, ['abc'])

    def test_case3(self): #TestCase3 : Numeric value string
        obj3 = matches(['1'])
        objresult= obj3.find('1')
        self.assertEqual(objresult, ['1'])
    
    def test_case4(self): #TestCase4 : Multiple string find in the given list of strings
        obj4 = matches(["helloworld","oof","foo","bar","stylight_team"])
        objresult4= obj4.find('foo')
        self.assertTrue(objresult4 ==['oof', "foo"] or objresult4 ==['foo', "oof"])

    def test_case5(self): #TestCase5 : User enter Input value for list of string as Integer or invalid datatype 
        obj5 = matches(1)
        objresult= obj5.find(1)
        self.assertEqual(objresult, 'User should enter valid input list of string details')
    
    def test_case6(self):
        obj6 = matches('1') #TestCase6 : User enter Input value for find string as Integer or invalid datatype 
        objresult= obj6.find(1)
        self.assertEqual(objresult, 'User should enter valid find string details')

if __name__=='__main__':
    unittest.main()