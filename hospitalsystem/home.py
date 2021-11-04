import tkinter as tk
from tkinter import font
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
        self.title("Home Page")
        self.display_homepage()
        self.queue = PriorityHeap()
        self._queue_test()

        
    def display_homepage(self):
        title_label = tk.Label(self, text="Home", font=self.titlefont)
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)
        #title_label.pack()

        calculate_triage_button = tk.Button(self, text="Calculate Triage", command = lambda: self.display_patientform(), bg="grey")
        calculate_triage_button.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.15)
        #calculate_triage_button.pack()

        allocate_bed_button = tk.Button(self, text="Allocate Bed", bg="grey", command=lambda: self.display_assignbed())
        allocate_bed_button.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.15)

        edit_queue_button = tk.Button(self, text="Edit Queue", bg="grey")
        edit_queue_button.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.15)

    def display_patientform(self):
        run_patientform(self)

    def display_assignbed(self):
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