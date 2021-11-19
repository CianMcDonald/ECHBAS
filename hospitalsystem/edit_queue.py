import tkinter as tk
from tkinter import font
from bed_priority_queue import PriorityHeap

class EditQueue(tk.Toplevel):
    def __init__(self, parent, queue):
        super().__init__(parent)

        self.geometry("1000x800")
        self.title("Edit Queue")
        self.configure(bg="#F0F0F0", pady=50)
        
        self.queue = queue
        self.list_name = self.create_queue_list()
        self.parent = parent
        self.create_display()

    def create_display(self):   
        #Title
        title_label = tk.Label(self, text="Edit Queue", font=self.parent.titlefont, bg="#6fa491", fg="white")
        title_label.place(relx=0.15, rely=0.01, relwidth=0.7, relheight=0.2)

        #List
        list_items = tk.StringVar(value=self.list_name)
        listbox = tk.Listbox(self, height = 6, listvariable = list_items, selectmode='multiple')
        listbox.place(relx=0, rely=0.25, relwidth=0.3, relheight=0.75)

        #Confirm button
        confrim_button = tk.Button(self, text="Remove From Queue", command=lambda: self.remove_items_selected(listbox), bd='5', bg="#0e6556", fg="white", activebackground="#af1a40", font=self.parent.textfont)
        confrim_button.place(relx=0.6, rely=0.35, relwidth=0.3, relheight=0.15)

    def remove_items_selected(self, listbox):
        indexs_to_remove = listbox.curselection()
        if len(indexs_to_remove) == 0:
            tk.messagebox.showerror("Error", "No patient selected")
        else:
            msg = tk.messagebox.askquestion("Remove from queue", "Are you sure?")
            if msg == 'yes':
                names = [self.list_name[x] for x in indexs_to_remove]
                self.queue.remove_from_queue(names)
                self.destroy()


    def create_queue_list(self):
        names = self.queue.ordered_list()
        string_names = [str(patient) for patient in names]
        return string_names
    
