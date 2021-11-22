from tkinter import Button, StringVar, IntVar, Listbox, messagebox, Toplevel
import tkinter as tk
import sqlite3

# connection = sqlite3.connect("ailments.db")
# cursor = connection.cursor()
# #get all the patients details with their ppno
# ailmentlist_query = "SELECT name FROM ailments;"
# cursor.execute(ailmentlist_query)
# list_ailments = cursor.fetchall() 

def calculate_triage(entered):
      """
      Function thats gets data from form and calculates the patients triage score
      """
      # get triage from db
      triage_score = entered
      # if the triage is a number
      if str(triage_score).isdigit():
          if int(triage_score) <= 5:
         # add triage to entry box
            return "True"
      else:
         # triage is not a number so display error
         return "False"