import tkinter as tk
from tkinter import font
from tkinter import messagebox
from edit_queue import EditQueue

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
        self.geometry('1000x1000')
        self.titlefont = font.Font(family = 'Verdana', size=30,
                                    weight="bold")
        self.textfont = font.Font(family = 'Verdana', size=15)
        self.title("Home Page")
        self.display_homepage()
        self.queue = PriorityHeap()
        self._queue_test()
        # print(self.queue.length_of_queue())
        # print(type(self))

        
    def display_homepage(self):
        # queue_length = tk.Label(self, text="Queue length: %d" % self.queue.length_of_queue())
        # queue_length.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

        title_label = tk.Label(self, text="System Home", font=self.titlefont)
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)
        #title_label.pack()

        calculate_triage_button = tk.Button(self, text="Add Patient", command = lambda: self.display_patientform(), bg="grey", font=self.textfont)
        calculate_triage_button.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.15)
        #calculate_triage_button.pack()

        allocate_bed_button = tk.Button(self, text="Assign Bed to Patient", bg="grey", command=lambda: self.display_assignbed(), font=self.textfont)
        allocate_bed_button.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.15)

        edit_queue_button = tk.Button(self, text="Edit Queue", bg="grey", command=lambda: self.display_editqueue(), font=self.textfont)
        edit_queue_button.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.15)

    def display_patientform(self):
        run_patientform(self)

    def display_assignbed(self):
        msg = messagebox.askquestion("Assign Bed", "Are you sure?")
        if msg == 'yes':
            window = AssignBed(self, self.queue)
            window.grab_set()
    
    def display_editqueue(self):
        window = EditQueue(self, self.queue)
        window.grab_set()

    def _queue_test(self):
        cian = Patient("cian", "mcdonald", 2)
        katie = Patient("katie", "c", 4)
        abbie = Patient("abbie", "d", 1)
        ben = Patient("ben", "p", 3)
        self.queue.push_queue(cian)
        self.queue.push_queue(katie)
        self.queue.push_queue(abbie)
        self.queue.push_queue(ben)



if __name__ == "__main__":
    app = HomePage()
    app.mainloop()