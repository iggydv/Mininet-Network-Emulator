import unittest
import tempfile
import Parser
import sys, os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'hosts.txt')

class TestParser(unittest.TestCase):
   
   def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()
       print(self.testdata)
       
   def Test_Parse(self):
      
      
if __name__ == '__main__':
    unittest.main()
