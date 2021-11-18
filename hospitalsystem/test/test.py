import unittest
import sqlite3
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
        
    def test_entered_empty(self):
        connection = sqlite3.connect("ailments.db")
        cursor = connection.cursor()
        #get all the patients details with their ppno
        ailmentlist_query = "SELECT name FROM ailments;"
        cursor.execute(ailmentlist_query)
        list_ailments = cursor.fetchall() 

        # create a list of the ailments selected from db
        actual = [ailment_value[0] for ailment_value in list_ailments]
        entered = ""
        self.assertEqual(key_entered(entered), actual)

if __name__ == '__main__':
    unittest.main(verbosity=2)