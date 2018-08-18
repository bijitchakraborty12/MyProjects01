
#from normalFunctions import oddeven as oe

from Assignment02_01b import openFile
from Assignment02_01b import processCommands
import unittest

class TestAssignment02(unittest.TestCase):
    """docstring for TestNormalFunction"""
    def testOpenFile(self):
        payload='C:\\Python Practice\\MyProjects01\\MyProjects01\\20180707\\Commands_List.txt'
        res=openFile(payload)  # function odeven in module normalFunctions is now aliased as oe...        
        exp='insert 0 5\n'     # first line
        self.assertEqual(res[1],exp)    
        
        exp='insert 1 10\n'     # second line
        self.assertEqual(res[2],exp)    

    def testProcessCommands(self):
        payload=['insert 1 10\n']
        res=processCommands(payload)  # function odeven in module normalFunctions is now aliased as oe...        
        exp=[10]     # first line
        self.assertEqual(res,exp)    
        


if __name__ == '__main__':
    unittest.main()