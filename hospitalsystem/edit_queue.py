import tkinter as tk
from tkinter import font
from bed_priority_queue import PriorityHeap

class EditQueue(tk.Toplevel):
    def __init__(self, parent, queue):
        super().__init__(parent)

        self.geometry("800x600")
        self.title("Edit Queue")
        self.queue = queue
        self.list_name = self.create_queue_list(queue._queue)
        self.parent = parent
        self.create_display()

    def create_display(self):   
        #Title
        title_label = tk.Label(self, text="Edit Queue", font=self.parent.titlefont)
        title_label.place(relx=0.15, rely=0.01, relwidth=0.7, relheight=0.2)

        #List
        list_items = tk.StringVar(value=self.list_name)
        listbox = tk.Listbox(self, height = 6, listvariable = list_items, selectmode='multiple')
        listbox.place(relx=0, rely=0.25, relwidth=0.3, relheight=0.75)

        #Confirm button
        confrim_button = tk.Button(self, text="Remove From Queue", bg="grey", command=lambda: self.remove_items_selected(listbox), font=self.parent.textfont)
        confrim_button.place(relx=0.6, rely=0.35, relwidth=0.3, relheight=0.15)

    def remove_items_selected(self, listbox):
        msg = tk.messagebox.askquestion("Remove from queue", "Are you sure?")
        if msg == 'yes':
            indexs_to_remove = listbox.curselection()
            names = [self.list_name[x] for x in indexs_to_remove]
            self.queue.remove_from_queue(names)
            self.destroy()


    def create_queue_list(self, queue):
        names = [str(patient) for patient in queue]
        return names
    
