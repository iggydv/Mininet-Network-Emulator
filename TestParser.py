import unittest
import tempfile
import Parser
import sys, os

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'hosts.txt')

# Testing is a critical part of any coding project. Think of every single way in which
# someone can create malformed config, and create an example of that. Place each in a test dir
# eg, test/test_invalid_hosts/host_bandwidth_negative/hosts.txt
#                                                    /switches.txt
#     test/test_invalid_hosts/host_bandwidth_missing/hosts.txt
#                                                   /switches.txt
#
# You can then create a test per directory
# eg,
#  def test_bandwidth:
#      parser = new Parser()
#      parser.parse('test/test_invalid_hosts/host_bandwidth_negative/')
#      make sure ValueError was raised
#      make sure parser.getHosts returns None
#      make sure parser.getSwitches returns None
#      etc.
#
#      parser.parse('test/test_invalid_hosts/host_bandwidth_missing')
#      make sure ValueError was raised
#      make sure parser.getHosts returns None
#      make sure parser.getSwitches returns None
#      etc.
#
# And this is why your parsers directory should be configurable

class TestParser(unittest.TestCase):
   
   def setUp(self):
       self.testdata = open(TESTDATA_FILENAME).read()
       print(self.testdata)
       
   def Test_Parse(self):
      
      
if __name__ == '__main__':
    unittest.main()
