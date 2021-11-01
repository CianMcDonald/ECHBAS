import tkinter as tk

HEIGHT = 1920
WIDTH = 1600

root = tk.Tk()

calculate_triage_button = tk.Button(root, text="Calculate Triage")
calculate_triage_button.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.2)

root.mainloop()