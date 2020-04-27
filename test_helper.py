import unittest
from helper import increment_msppdate

class TestHelper(unittest.TestCase):
    def test_increment_msppdatedef(self):
        self.assertEqual(increment_msppdate('29-02-2020')["str"],"01-03-2020")

if __name__ == '__main__':
    unittest.main()