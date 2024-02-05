import unittest

# The class that contains the test methods
class MyTestCase(unittest.TestCase):
    
    def test_addition(self):
        result = 2 + 2
        self.assertEqual(result, 4)
    
    def test_uppercase(self):
        string = "HELLO"
        self.assertTrue(string.isupper())

# Running the tests
if __name__ == '__main__':
    unittest.main()
