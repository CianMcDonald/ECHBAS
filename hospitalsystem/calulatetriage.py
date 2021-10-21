from PIL import Image
from pyzbar.pyzbar import *
import sqlite3
import tkinter as tk
from tkinter import Button, StringVar

#initialise tkinter
master = tk.Tk()
#create labels 
tk.Label(master, text="Forename").grid(row=0)
tk.Label(master, text="Surname").grid(row=1)
tk.Label(master, text="Date of Birth").grid(row=2)
tk.Label(master, text="Gender").grid(row=3)
tk.Label(master, text="Medical History").grid(row=4)
tk.Label(master, text="Current Aliment/Injury").grid(row=5)

def calculate_triage():
   """
   Function thats gets data from form and calculates the patients triage score
   """
   #store input from form and print
   fname = fname_submit.get()
   sname = sname_submit.get()
   dob = dob_submit.get()
   gender = gender_submit.get()
   medical_history = medical_history_submit.get()
   current_injury = current_injury_submit.get()
   print(fname)
   print(sname)
   print(dob)
   print(gender)
   print(medical_history)
   print(current_injury)


def patient_data():
   """
   Function that decodes the QR code and searches for the patients details in the hse's database using their pps number
   """
   #decode qr
   qr_decoded = decode(Image.open("static/qr_photos/qrdata.png"))
   #get the data values
   qr_data = qr_decoded[0].data
   #convert to string
   qr_data = qr_data.decode('utf-8')
   #add firtname, surname, ppsno to a list sepertated by commmas
   letter_list = qr_data.split(",")
   #assign values to list
   fname = letter_list[0]
   sname = letter_list[1]
   ppsno = letter_list[2]
   #connect to hse database
   connection = sqlite3.connect("hse_data.db")
   cursor = connection.cursor()
   #get all the patients details with their ppno
   verify_query = "SELECT ppsno, fname, sname, DOB, gender, medical_history FROM medicalrecords WHERE ppsno='"+ ppsno +"'"
   cursor.execute(verify_query)

   result = cursor.fetchall()
   #if they are not in the database, return empty strings
   if len(result) == 0:
      return "", "", "", "", ""
   #else they are in the database, return their details
   else:
      dob = result[0][3]
      gender = result[0][4]
      medical_history = result[0][5]
      return fname, sname, dob, gender, medical_history


#access the entries from the form
fname_submit = StringVar()
sname_submit = StringVar()
dob_submit = StringVar()
gender_submit = StringVar()
medical_history_submit = StringVar()
current_injury_submit = StringVar()

#create each entry box for form
e1 = tk.Entry(master, textvariable=fname_submit)
e2 = tk.Entry(master, textvariable=sname_submit)
e3 = tk.Entry(master, textvariable=dob_submit)
e4 = tk.Entry(master, textvariable=gender_submit)
e5 = tk.Entry(master, textvariable=medical_history_submit)
e6 = tk.Entry(master, textvariable=current_injury_submit)

#autofill the form using patient details
fname, sname, dob, gender, medical_history = patient_data()

#where to insert each value
e1.insert(0, fname)
e2.insert(0, sname)
e3.insert(0, dob)
e4.insert(0, gender)
e5.insert(0, medical_history)


#where tp place each entry
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)

#click the submit button sends the data to calculate the triage
submitbut = Button(master, text="Submit", width=10, command=calculate_triage)
submitbut.grid(row=6, column=1)

tk.mainloop()
