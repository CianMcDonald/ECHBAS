import unittest
from key_entered_test import key_entered


class KeyTest(unittest.TestCase):

    def test_entered_correct_string(self):
        actual = ["airway compromise"]
        entered = "airway compromise"
        self.assertEqual(key_entered(entered), actual)
        
    def test_entered_invalid_string(self):
        actual = []
        entered = "12345"
        self.assertEqual(key_entered(entered), actual)
        
    def test_entered_special_char(self):
        actual = []
        entered = "@"
        self.assertEqual(key_entered(entered), actual)


if __name__ == '__main__':
    unittest.main(verbosity=2)