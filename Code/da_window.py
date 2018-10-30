import tkinter as tk


class Window(tk.Toplevel):

    def __init__(self, parent, win_id):
        tk.Toplevel.__init__(self, parent)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.window_id = win_id
        self.title('Data Analysis')
        self.iconbitmap("icon.ico")
        self.geometry('700x500+150+100')
        # self.resizable(False, False)

        # Container to contain main page
        self.container = tk.Frame(self, bg='#000000')
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
