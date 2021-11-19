from tkinter import Button, StringVar, IntVar, Listbox, messagebox, Toplevel
import tkinter as tk
import sqlite3


connection = sqlite3.connect("ailments.db")
cursor = connection.cursor()
#get all the patients details with their ppno
ailmentlist_query = "SELECT name FROM ailments;"
cursor.execute(ailmentlist_query)
list_ailments = cursor.fetchall() 

   # create a list of the ailments selected from db
ailmentsearch_list = [ailment_value[0] for ailment_value in list_ailments]

def key_entered(entered):
      """
      When a key is entered into the sixth entry box (current aliment)
      this functions searches the list for that ailment and shortens the list.
      """
      # get what letters was entered by person
      #entered = e6.get()
      entered = entered
      # if box is blank and backspace is pressed
      if entered == '' and entered == '<BackSpace>':
         #display entire list
         totallist = ailmentsearch_list
      # else a key has been entered
      else:
         # create a list with new values
         new_val_list = []
         # look for a value in our complete list that matches what was entered in the box
         for val in ailmentsearch_list:
            # if value entered equals value in the list
            if entered.lower() in val.lower():
               #add it to our new list
               new_val_list.append(val)
      # display only values that match the entered value				
      return new_val_list