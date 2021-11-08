import tkinter as tk
from tkinter import font
from tkinter import messagebox

from patientform import run_patientform
from bed_priority_queue import PriorityHeap
from assign_bed import AssignBed
from patient import Patient

class HomePage(tk.Tk):
    """
    Frame object holdig all pages
    Controller of pages: fonts 
    """
    def __init__(self):
        # Shared title font
        super().__init__()
        self.geometry('700x600')
        self.titlefont = font.Font(family = 'Rockwell', size=30,
                                    weight="bold")
        self.textfont = font.Font(family = 'Gadugi', size=18)
        self.configure(bg="#F0F0F0", pady=50)
        self.title("Home Page")
        self.display_homepage()
        self.queue = PriorityHeap()
       
        #self._queue_test()

        
    def display_homepage(self):
        title_label = tk.Label(self, text="Bed Allocation System", font=self.titlefont, bg="#F0F0F0", fg="#af1a40", borderwidth=1.5, relief="solid", highlightcolor="#0e6556")
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.15)
        #title_label.pack()

        calculate_triage_button = tk.Button(self, text="Add Patient",  bd='5', command = lambda: self.display_patientform(), bg="#0e6556", fg="white", activebackground="#af1a40", font=self.textfont)
        calculate_triage_button.place(relx=0.25, rely=0.3, relwidth=0.5, relheight=0.13)
        #calculate_triage_button.pack()

        allocate_bed_button = tk.Button(self, text="Assign Bed to Patient", bd='5', bg="#0e6556", fg="white", activebackground="#af1a40", command=lambda: self.display_assignbed(), font=self.textfont)
        allocate_bed_button.place(relx=0.25, rely=0.5, relwidth=0.5, relheight=0.13)

        edit_queue_button = tk.Button(self, text="Edit Queue",  bd='5', bg="#0e6556", fg="white", activebackground="#af1a40",font=self.textfont)
        edit_queue_button.place(relx=0.25, rely=0.7, relwidth=0.5, relheight=0.13)


    def display_patientform(self):
        run_patientform(self)

    def display_assignbed(self):
        msg = messagebox.askquestion("Assign Bed", "Are you sure?")
        if msg == 'yes':
            window = AssignBed(self, self.queue)
            window.grab_set()

    def _queue_test(self):
        cian = Patient("cian", "mcdonald", 2)
        louis = Patient("louis", "sull", 4)
        self.queue.push_queue(cian)
        self.queue.push_queue(louis)


if __name__ == "__main__":
    app = HomePage()
    app.mainloop()