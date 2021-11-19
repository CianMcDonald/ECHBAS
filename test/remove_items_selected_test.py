import tkinter as tk
from tkinter import messagebox

def create_queue_list(queue):
    names = queue.ordered_list()
    string_names = [str(patient) for patient in names]
    return string_names

def print_queue(queue):
    for item in queue._queue:
        print(item)

def remove_items_selected(listbox, queue, msg):
    indexs_to_remove = listbox
    if len(indexs_to_remove) == 0 or queue.length_of_queue() == 0:
        #tk.messagebox.showerror("Error", "No patient selected")
        pass
    else:
        #msg = tk.messagebox.askquestion("Remove from queue", "Are you sure?")
        list_name = create_queue_list(queue)
        if msg == 'yes':
            names = [list_name[x] for x in indexs_to_remove]
            queue.remove_from_queue(names)
    return queue
           



# to_remove = [1,3,2]
# remove_items_selected(to_remove)


