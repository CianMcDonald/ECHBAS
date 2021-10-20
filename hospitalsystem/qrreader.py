from PIL import Image
from pyzbar.pyzbar import decode
import sqlite3
import tkinter as tk
from tkinter import Button, StringVar


def calculate_triage(current_injury_submit):
   # fname = fname_submit
   # sname = sname_submit.get()
   # dob = dob_submit.get()
   # gender = gender_submit.get()
   # medical_history = medical_history_submit.get()
   current_injury = current_injury_submit
   # print(fname)
   # print(sname)
   # print(dob)
   # print(gender)
   # print(medical_history)
   print(current_injury)

def create_form(fname="", sname="", dob="", gender="", medical_history=""):
   master = tk.Tk()
   tk.Label(master, text="Forename").grid(row=0)
   tk.Label(master, text="Surname").grid(row=1)
   tk.Label(master, text="Date of Birth").grid(row=2)
   tk.Label(master, text="Gender").grid(row=3)
   tk.Label(master, text="Medical History").grid(row=4)
   tk.Label(master, text="Current Aliment/Injury").grid(row=5)

   fname_submit = StringVar()
   sname_submit = StringVar()
   dob_submit = StringVar()
   gender_submit = StringVar()
   medical_history_submit = StringVar()
   current_injury_submit = StringVar()
   

   #creat each entry box for form
   e1 = tk.Entry(master, textvariable=fname_submit)
   e2 = tk.Entry(master, textvariable=sname_submit)
   e3 = tk.Entry(master, textvariable=dob_submit)
   e4 = tk.Entry(master, textvariable=gender_submit)
   e5 = tk.Entry(master, textvariable=medical_history_submit)
   e6 = tk.Entry(master, textvariable=current_injury_submit)

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

   submitbut = Button(master, text="Submit", width=10, command= lambda: calculate_triage(current_injury_submit))
   submitbut.grid(row=6, column=1)

   tk.mainloop()

def patient_data():
   data = decode(Image.open("static/qr_photos/qrdata.png"))
   new = data[0].data
   new = new.decode('utf-8')
   letter_list = new.split(",")
   #print(letter_list)

   fname = letter_list[0]
   sname = letter_list[1]
   ppsno = letter_list[2]

   connection = sqlite3.connect("hse_data.db")
   cursor = connection.cursor()
   verify_query = "SELECT ppsno, fname, sname, DOB, gender, medical_history FROM medicalrecords WHERE ppsno='"+ ppsno +"'"
   cursor.execute(verify_query)

   result = cursor.fetchall()
   if len(result) == 0:
      create_form()
   else:
      dob = result[0][3]
      gender = result[0][4]
      medical_history = result[0][5]
      create_form(fname, sname, dob, gender, medical_history)

def main():
   patient_data()
   
main()
