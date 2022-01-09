import unittest
from name_function import get_formatted_name

class NamesTest(unittest.TestCase):
    """
    This test's name_function
    """
    def testName(self):
        formatted_name = get_formatted_name("john", "james")
        self.assertEqual(formatted_name, "John James")
    def testNameMiddle(self):
        formatted_name = get_formatted_name("john","johna","jamerson")
        self.assertEqual(formatted_name, "John Johna Jamerson")
        
if __name__ == "__main__":
    unittest.main()
    