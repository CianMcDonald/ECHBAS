import unittest
import sqlite3
from key_entered_test import key_entered
from calculate_triage_test import calculate_triage

import sys
from contextlib import contextmanager
from io import StringIO 

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
class Test(unittest.TestCase):
    def test_keyentered_correct_string(self):
        actual = ["airway compromise"]
        entered = "airway compromise"
        self.assertEqual(key_entered(entered), actual)
        
    def test_keyentered_invalid_string(self):
        actual = []
        entered = "12345"
        self.assertEqual(key_entered(entered), actual)
        
    def test_keyentered_special_char(self):
        actual = []
        entered = "@"
        self.assertEqual(key_entered(entered), actual)
        
    def test_keyentered_empty(self):
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
        
    def test_triage_digit(self):
        entered = "1"
        with captured_output() as (out, err): calculate_triage(entered)
        output = out.getvalue().strip()
        assert (output == "True")
        pass
    
    def test_triage_notdigit(self):
        entered = "fdsd"
        with captured_output() as (out, err): calculate_triage(entered)
        output = out.getvalue().strip()
        assert (output == "False")
        pass
    
    def test_triage_lessthandigit(self):
        entered = "5"
        with captured_output() as (out, err): calculate_triage(entered)
        output = out.getvalue()
        assert (output == "True")
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)