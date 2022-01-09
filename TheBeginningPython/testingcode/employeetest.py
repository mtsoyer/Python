import unittest
from employee import Employee

class testEmp(unittest.TestCase):
    def setUp(self):
        self.me = Employee("John", "James", 2000)
        
    def test__give_raise(self):
        self.assertEqual(self.me.give_raise(), 7000)
    
    def test__custom_raise(self):
        self.assertEqual(self.me.give_raise(1000), 3000)
if __name__ == "__main__":
    unittest.main()