import tkinter as tk
from tkinter import font
from bed_priority_queue import PriorityHeap

class AssignBed(tk.Toplevel):
    def __init__(self, parent, queue):
        super().__init__(parent)

        self.geometry("800x600")
        self.title("Assign Bed")
        self.configure(bg="#6fa491", pady=50)

        patient_to_remove = queue.pop_queue()

        try:
            if patient_to_remove == "Error: Empty queue":
                #Title
                title_label = tk.Label(self, text="ERROR:", font=parent.titlefont, bg="#6fa491")
                title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

                #Confirmation
                title_label = tk.Label(self, text="The queue is empty no bed has been allocated", font=parent.textfont, bg="#0e6556", fg="white")
                title_label.place(relx=0.0, rely=0.4, relwidth=1, relheight=0.1)

                #Patient to remove
                patient_label = tk.Label(self, text="{}".format(patient_to_remove), font=parent.titlefont, border=3, relief="ridge", bg="#6fa491", fg="white")
                patient_label.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
                
        except AttributeError:
            #Title
            title_label = tk.Label(self, text="Next Patient:", font=parent.titlefont, bg="#6fa491")
            title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)

            #Confirmation
            title_label = tk.Label(self, text="{} has been allocated a bed and has been removed from queue".format(patient_to_remove), font=parent.textfont, bg="#0e6556", fg="white")
            title_label.place(relx=0.0, rely=0.4, relwidth=1, relheight=0.1)

            #Patient to remove
            patient_label = tk.Label(self, text="{}".format(patient_to_remove), font=parent.titlefont, border=3, relief="ridge", bg="#6fa491", fg="white")
            patient_label.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)
        

