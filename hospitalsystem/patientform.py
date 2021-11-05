import pyzbar.pyzbar as pyzbar
import numpy as np
import sqlite3
import cv2
from tkinter import Button, StringVar, IntVar, Listbox, messagebox, Toplevel
import tkinter as tk
from patient import Patient

def run_patientform(root):
   #connect to hse database
   connection = sqlite3.connect("ailments.db")
   cursor = connection.cursor()
   #get all the patients details with their ppno
   ailmentlist_query = "SELECT name FROM ailments;"
   cursor.execute(ailmentlist_query)
   list_ailments = cursor.fetchall() 

   # create a list of the ailments selected from db
   ailmentsearch_list = [ailment_value[0] for ailment_value in list_ailments]

   def submit_form():
      """
      Function thats validates triage and prints data entered in from
      """
      if not str(triage_submit.get()).isdigit() or int(triage_submit.get()) > 5:
         messagebox.showerror(title="Triage Score Error", message="The value entered into 'Triage Score' is incorrect!")
      else:
         #store input from form and print
         fname = fname_submit.get()
         sname = sname_submit.get()
         dob = dob_submit.get()
         gender = gender_submit.get()
         medical_history = medical_history_submit.get()
         current_injury = current_injury_submit.get()
         triage = triage_submit.get()
         print(fname)
         print(sname)
         print(dob)
         print(gender)
         print(medical_history)
         print(current_injury)
         print(triage)
         root.queue.push_queue(Patient(fname, sname, triage))
         master.destroy()

   def validate_form(event):
      """
      Function that checks if the form is fully filled out
      """
      # make sure something entered is every box
      if fname_submit.get() and sname_submit.get() and dob_submit.get() and gender_submit.get() and medical_history_submit.get() and current_injury_submit.get() and triage_submit.get():
         # now we can submit
         submitbut.config(state='normal')
      else:
         # otherwise something is blank so we cannot submit
         submitbut.config(state='disabled')

   def calculate_triage():
      """
      Function thats gets data from form and calculates the patients triage score
      """
      # get triage from db
      current_injury = current_injury_submit.get()
      patient_triage_query = "SELECT score FROM ailments WHERE name='"+ current_injury +"'"
      cursor.execute(patient_triage_query)
      triage_db_result = cursor.fetchone()
      # if the triage is a number
      if str(triage_db_result[0]).isdigit():
         # add triage to entry box
         triage_score = int(triage_db_result[0])
         e7.delete(0, 'end')
         e7.insert(0, triage_score)
         validate_form(None)
      else:
         # triage is not a number so display error
         master.messagebox.showerror(title="Triage Score Error", message="The value entered into Triage Score is incorrect!")

   def patient_data():
      """
      Function that boots camera to get qr code, decodes the QR code and searches for the patients details in the hse's database using their pps number
      """
      #Boot camera 1 to scan qr code
      #In Linux remove cv2.CAP_DSHOW
      cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
      data_recieved = None
      # while no data has been recieved
      while data_recieved is None:
         # read in data from the screen
         done, qr_scanner = cap.read()
         # decode data when qr is detected
         qr_decoded = pyzbar.decode(qr_scanner)
         # for the qr that is decoded 
         for qr in qr_decoded:   
            # set data recieved to not none to break loop            
            data_recieved = qr.data
            # close camera
            cv2.destroyAllWindows()
      #qr_decoded = decode(Image.open("static/qrphotos/qrdata.png"))
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
      connection.close()

   def key_entered(event):
      """
      When a key is entered into the sixth entry box (current aliment)
      this functions searches the list for that ailment and shortens the list.
      """
      # get what letters was entered by person
      entered = e6.get()
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
      update_list(new_val_list)

   def fillin(event):
      """
      Function that adds selected value from dropdown to the entry
      """
      # get the list box widget where the selection occurred
      my_listbox = event.widget 
      # get the index of the selection
      my_listbox_index= my_listbox.curselection() 
      if my_listbox_index:
         # get the value fo that selection
         my_listbox_value = my_listbox.get(my_listbox_index[0])
         # delete whatever is in current ailment
         e6.delete(0, 'end')
         # add the newly selected value
         e6.insert(0, my_listbox_value)
         calculate_triage()

   def update_list(new_list):
      """
      Function that updates the current list with the newly selected values
      """
      # delete what is already displayed in the list box
      listbox.delete(0, 'end')
      # for the item in the new list
      for item in new_list:
         # add it to the listbox at the end
         listbox.insert('end', item)

   form_load = messagebox.askquestion(title="Qr Scan", message="Would you like to scan a QR code?")

   #initialise tkinter
   #master = tk.Tk()
   master = Toplevel(root)
   master.grab_set()
   
   #Form details
   master.title("Patient Form")
   master.maxsize(800, 600)
   master.config(bg="Light Grey")


   #create labels 
   tk.Label(master, text="Forename", bg="Light Grey").grid(row=0)
   tk.Label(master, text="Surname", bg="Light Grey").grid(row=1)
   tk.Label(master, text="Date of Birth", bg="Light Grey").grid(row=2)
   tk.Label(master, text="Gender", bg="Light Grey").grid(row=3)
   tk.Label(master, text="Medical History", bg="Light Grey").grid(row=4)
   tk.Label(master, text="Current Aliment", bg="Light Grey").grid(row=5)
   tk.Label(master, text="Triage Score", bg="Light Grey").grid(row=10)

   #access the entries from the form
   fname_submit = StringVar()
   sname_submit = StringVar()
   dob_submit = StringVar()
   gender_submit = StringVar()
   medical_history_submit = StringVar()
   current_injury_submit = StringVar()
   triage_submit = StringVar()

   #create each entry box for form
   e1 = tk.Entry(master, textvariable=fname_submit)
   e2 = tk.Entry(master, textvariable=sname_submit)
   e3 = tk.Entry(master, textvariable=dob_submit)
   e4 = tk.Entry(master, textvariable=gender_submit)
   e5 = tk.Entry(master, textvariable=medical_history_submit)
   e6 = tk.Entry(master, textvariable=current_injury_submit)
   e7 = tk.Entry(master, textvariable=triage_submit)

   if form_load == 'yes':
      #autofill the form using patient details
      fname, sname, dob, gender, medical_history = patient_data()
      #where to insert each value
      e1.insert(0, fname)
      e2.insert(0, sname)
      e3.insert(0, dob)
      e4.insert(0, gender)
      e5.insert(0, medical_history)

   #where t0 place each entry
   e1.grid(row=0, column=1)
   e2.grid(row=1, column=1)
   e3.grid(row=2, column=1)
   e4.grid(row=3, column=1)
   e5.grid(row=4, column=1)
   e6.grid(row=5, column=1)
   e7.grid(row=10, column=1)

   # when a key is entered related ailments will appear in the list box
   e6.bind('<KeyRelease>', key_entered)

   #make sure that there is soemthing entered before we submit
   e1.bind('<KeyRelease>', validate_form)
   e2.bind('<KeyRelease>', validate_form)
   e3.bind('<KeyRelease>', validate_form)
   e4.bind('<KeyRelease>', validate_form)
   e5.bind('<KeyRelease>', validate_form)
   #e6.bind('<KeyRelease>', validate_form)
   e7.bind('<KeyRelease>', validate_form)

   #click the submit button sends the data to calculate the triage
   submitbut = Button(master, text="Submit", width=10, command=submit_form)
   submitbut.grid(row=10, column=100)
   submitbut.config(state='disabled')

   # create the searchable listbox
   listbox = Listbox(master, width=35)
   # display the box in the grid
   listbox.grid(row=6, column=1, columnspan=20)
   # if an item is selected in listbox, function that adds it to current ailment is called
   listbox.bind("<<ListboxSelect>>", fillin)
   # initially update the list with the full list of ailments
   update_list(ailmentsearch_list)

   tk.mainloop()

if __name__ == "__main__":
   main = tk.Tk()
   run_patientform(main)
