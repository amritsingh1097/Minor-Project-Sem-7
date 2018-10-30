import tkinter as tk
from tkinter import ttk

FONT_CAMBRIA_10 = ("Cambria", "10")
FONT_CAMBRIA_11 = ("Cambria", "11")


class Window(tk.Toplevel):

    def __init__(self, parent, win_id, file, extension):
        tk.Toplevel.__init__(self, parent)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.window_id = win_id
        self.title('Data Visualization')
        self.iconbitmap("icon.ico")
        self.geometry('1500x900+200+50')
        self.minsize(600, 400)
        # self.resizable(False, False)

        # Container to contain main page
        self.container = tk.Frame(self, bg='#000000')
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.__addDataCleaningSection()

    def __addDataCleaningSection(self):
        self.filter_list_container = tk.Frame(self.container,
                                              bd=0,
                                              padx='2m',
                                              pady='2m',
                                              # bg="#cccccc",
                                              relief=tk.FLAT)
        self.filter_list_container.pack(side=tk.TOP, fill=tk.X)
        # self.filter_list_container.grid_columnconfigure(0, weight=1)
        self.filter_list_container.grid_columnconfigure(1, weight=1)
        # self.filter_list_container.grid_columnconfigure(2, weight=1)
        # self.filter_list_container.grid_columnconfigure(3, weight=1)

        label = tk.Label(self.filter_list_container,
                         justify=tk.LEFT,
                         font=FONT_CAMBRIA_11,
                         text="Choose Filter:")
        label.grid(row=0, column=0, sticky=tk.W, padx='2m 0m')

        self.__addFiltersList()
        self.__addFilterOptionsButton()
        self.__addApplyButton()

    def __addFiltersList(self):
        self.list_values = ["Select Filter", "1", "2", "3", "4", "5"]
        # self.list_var = tk.StringVar()
        self.filter_list = ttk.Combobox(self.filter_list_container,
                                        # width=200,
                                        height=10,
                                        state='readonly',
                                        # textvariable=self.list_var,
                                        values=self.list_values)
        self.filter_list.grid(row=0, column=1, sticky=tk.EW, padx='2m')
        self.filter_list.bind("<<ComboboxSelected>>", self.__onOptionSelected)
        self.filter_list.current(0)

    def __onOptionSelected(self, event):
        print("Selected Option:", self.filter_list.current())
        if self.filter_list.current() == 0:
            self.apply_button.configure(state=tk.DISABLED)
        else:
            self.apply_button.configure(state=tk.NORMAL)

    def __addFilterOptionsButton(self):
        self.apply_button = tk.Button(self.filter_list_container,
                                      height=1,
                                      font=FONT_CAMBRIA_10,
                                      activebackground='#7EB6FF',
                                      text="Filter Options",
                                      command=lambda: self.__applyFilter(),
                                      padx='3m',
                                      pady='0m',
                                      # state=tk.DISABLED,
                                      relief=tk.GROOVE)
        self.apply_button.grid(row=0, column=2, padx='2m')

    def __addApplyButton(self):
        self.apply_button = tk.Button(self.filter_list_container,
                                      height=1,
                                      font=FONT_CAMBRIA_10,
                                      activebackground='#7EB6FF',
                                      text="Apply",
                                      command=lambda: self.__applyFilter(),
                                      padx='3m',
                                      pady='0m',
                                      # state=tk.DISABLED,
                                      relief=tk.GROOVE)
        self.apply_button.grid(row=0, column=3, padx='2m')

    def __applyFilter(self):
        print("Applying Filter")
