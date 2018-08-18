
#from normalFunctions import oddeven as oe

import normalFunctions_generators as oe
import unittest

class TestGeneratorFunction(unittest.TestCase):
    """docstring for TestNormalFunction"""
    def testOddEven(self):
        res=[] 
        payload=[1,2,3,4]
        resGenarator=oe.oddeven(payload)  # function odeven in module normalFunctions is now aliased as oe...
        exp=['o','e','o','e']
        for k in resGenarator:
            res.append(k)
        
        # alterativly:
        # self.assertEqual(list(resGenarator),exp)
        # either of the above ways can be used, as once a 
        # particular yield is iterated through, the memory 
        # is cleared of that...


        self.assertEqual(res,exp)    


if __name__ == '__main__':
    unittest.main()