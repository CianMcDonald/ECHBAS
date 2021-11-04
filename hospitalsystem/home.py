import tkinter as tk
from tkinter import font
from patientform import run_patientform
class MainFrame(tk.Tk):
    """
    Frame object holdig all pages
    Controller of pages: fonts 
    """
    def __init__(self):
        tk.Tk.__init__(self)

        # Shared title font
        self.titlefont = font.Font(family = 'Verdana', size=30,
                                    weight="bold")
        # Controlling Frame
        container = tk.Frame()
        container.grid(row=0, column=0, sticky='nsew')

        #Dict "page_name" -> Frame
        self.listing = {}

        for page in (HomePage,TriagePage): #,TriagePage
            # Get classes name
            page_name = page.__name__
            # Create each Page
            frame = page(parent = container, controller = self)
            # Place them in Controller stacked on top of each other
            frame.grid(row=0, column=0, sticky='nsew')
            # Adds to dict "page_name" -> page frame
            self.listing[page_name] = frame

        # moves HomePage to top
        self.frame_up("HomePage")

    def frame_up(self, page_name):
        # Takes page name displays that page
        page = self.listing[page_name]
        page.tkraise()

    def patientform(self):
        run_patientform()


class HomePage(tk.Frame):
    # Home Page 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1000, height=1000)
        self.container = controller

        title_label = tk.Label(self, text="Home", font=controller.titlefont)
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)
        #title_label.pack()

        calculate_triage_button = tk.Button(self, text="Calculate Triage", command = lambda: controller.patientform(), bg="grey")
        calculate_triage_button.place(relx=0.15, rely=0.3, relwidth=0.7, relheight=0.15)
        #calculate_triage_button.pack()

        allocate_bed_button = tk.Button(self, text="Allocate Bed", bg="grey")
        allocate_bed_button.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.15)

        edit_queue_button = tk.Button(self, text="Edit Queue", bg="grey")
        edit_queue_button.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.15)


class TriagePage(tk.Frame):
    # Triage Score Page
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, width=1000, height=1000)
        self.container = controller

        title_label = tk.Label(self, text="Calculate Triage", font=controller.titlefont)
        title_label.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.2)
        #title_label.pack()

        calculate_triage_button = tk.Button(self, text="Return Home", command = lambda: controller.frame_up("HomePage"))
        calculate_triage_button.place(relx=0.15, rely=0.5, relwidth=0.7, relheight=0.2)
        #calculate_triage_button.pack()

if __name__ == "__main__":
    app = MainFrame()
    app.geometry("1000x1000")
    app.mainloop()