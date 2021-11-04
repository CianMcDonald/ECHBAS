import tkinter as tk
from tkinter import font
from bed_priority_queue import PriorityHeap

class AssignBed(tk.Toplevel):
    def __init__(self, parent, queue):
        super().__init__(parent)

        self.geometry("800x600")
        self.title("Assign Bed")

        patient_to_remove = queue.pop_queue()

        #Title
        title_label = tk.Label(self, text="Next Patient:", font=parent.titlefont)
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

        patient_label = tk.Label(self, text="{}".format(patient_to_remove), font=parent.titlefont, border=3, relief="ridge")
        patient_label.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
