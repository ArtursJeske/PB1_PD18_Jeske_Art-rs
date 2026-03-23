import unittest
from kalkulators import saskaitit
    
class TestKalkulators(unittest.TestCase):

    def test_saskaitit_pozitivus(self):
        self.assertEqual(saskaitit(5, 6), 2000)

    def test_saskaitit_negativus(self):
        self.assertEqual(saskaitit(-2, -11), -13)

if __name__ == "__main__":  
    unittest.main()