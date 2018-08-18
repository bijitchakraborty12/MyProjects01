
#from normalFunctions import oddeven as oe

import normalFunctions as oe
import unittest

class TestNormalFunction(unittest.TestCase):
    """docstring for TestNormalFunction"""
    def testOddEven(self):
        payload=[1,2,3,4]
        res=oe.oddeven(payload)  # function odeven in module normalFunctions is now aliased as oe...
        exp=['o','e','o','e']
        self.assertEqual(res,exp)

print('I am inside test code')
print(__name__)

if __name__ == '__main__':
    unittest.main()