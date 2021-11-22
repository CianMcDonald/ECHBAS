import unittest
import sys
from contextlib import contextmanager
from io import StringIO 
import sqlite3

from key_entered_test import key_entered
from calculate_triage_test import calculate_triage
from remove_items_selected_test import remove_items_selected
from bed_priority_queue import PriorityHeap
from patient import Patient

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
        
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

class RemoveItemsTest(unittest.TestCase):

    def test_entered_empty_queue(self):
        queue = PriorityHeap()
        listbox = [1,2]
        starting_queue_length = queue.length_of_queue()
        queue_end = remove_items_selected(listbox, queue, "yes")
        self.assertEqual(starting_queue_length, queue_end.length_of_queue())

    def test_entered_empty_selection(self):
        queue = PriorityHeap()
        cian = Patient("cian", "mcdonald", 2)
        katie = Patient("katie", "c", 4)
        queue.push_queue(cian)
        queue.push_queue(katie)
        listbox = []
        starting_queue_length = queue.length_of_queue()
        queue_end = remove_items_selected(listbox, queue, "yes")
        self.assertEqual(starting_queue_length, queue_end.length_of_queue())
    
    
    def test_entered_valid(self):
        cian = Patient("cian", "mcdonald", 2)
        katie = Patient("katie", "c", 4)
        abbie = Patient("abbie", "d", 1)
        ben = Patient("ben", "p", 3)
        queue = PriorityHeap()
        queue.push_queue(cian)
        queue.push_queue(katie)
        queue.push_queue(abbie)
        queue.push_queue(ben)
        listbox = [1,2]
        starting_queue_length = queue.length_of_queue()
        queue_end = remove_items_selected(listbox, queue, "yes")
        self.assertEqual(starting_queue_length, queue_end.length_of_queue()+len(listbox))
       
    def test_entered_valid_select_no(self):
        cian = Patient("cian", "mcdonald", 2)
        katie = Patient("katie", "c", 4)
        abbie = Patient("abbie", "d", 1)
        ben = Patient("ben", "p", 3)
        queue = PriorityHeap()
        queue.push_queue(cian)
        queue.push_queue(katie)
        queue.push_queue(abbie)
        queue.push_queue(ben)
        listbox = [1,2]
        starting_queue_length = queue.length_of_queue()
        queue_end = remove_items_selected(listbox, queue, "no")
        self.assertEqual(starting_queue_length, queue_end.length_of_queue())

class CalculateTriageTest(unittest.TestCase):
         
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

