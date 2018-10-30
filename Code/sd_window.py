# TODO 1: Add the column names (in bold) separately to avoid editing due to #3.
# TODO 2: Implement __getValue(row, col) function to show the data.
# TODO 3: Add a checkbox to enable user to edit the data in the window itself.
# TODO 4: Add Save button to save the modified data to a new file.
# TODO 5: Add Reset button to reset the data to its original values from the original file.
# TODO 6: Implement a function to infer the data type (nominal/numeric) of the columns.
# TODO 7: Implement validation function after inferring the data type of the columns.
# TODO 8: Add a Scrollbar to the data container.

import tkinter as tk
from tkinter import ttk
import pandas as pd

FONT_CAMBRIA_10 = ("Cambria", "10")
FONT_CAMBRIA_11 = ("Cambria", "11")


class Window(tk.Toplevel):

    def __init__(self, parent, win_id, file, extension):
        tk.Toplevel.__init__(self, parent)
        self.protocol("WM_DELETE_WINDOW", self.destroy)
        self.window_id = win_id
        self.title('Show Data')
        self.iconbitmap("icon.ico")
        self.geometry('800x500+200+150')
        self.minsize(400, 200)
        # self.maxsize(self.winfo_screenwidth()-100, self.winfo_screenheight())
        # self.resizable(False, False)

        # Container to contain main page
        self.container = tk.Frame(self)
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.__opened_file = file
        self.__opened_file_extension = extension
        print(extension)

        # self.__addButtons()
        # self.__addCheckBox()
        self.__addDataFields()

    def __addCheckBox(self):
        self.checkbox_container = tk.Frame(self.container,
                                           bd=0,
                                           bg="#cccccc",
                                           relief=tk.FLAT)
        self.checkbox_container.pack(side=tk.TOP, padx='1m', pady='1m')
        self.checkbox_container.grid_columnconfigure(0, weight=1)

        self.checkbox_status = tk.IntVar()
        self.checkbox_status.set(0)
        self.checkbox = ttk.Checkbutton(self.checkbox_container,
                                        text="Enable Editing",
                                        command=self.__checkboxCallback,
                                        offvalue=0,
                                        onvalue=1,
                                        variable=self.checkbox_status)
        self.checkbox.grid(row=0, column=0, sticky=tk.W)

    def __checkboxCallback(self):
        print("Checkbox Callback.")
        for field in self.__entry_fields:
            if self.checkbox_status.get():
                field.configure(state=tk.NORMAL)
            else:
                field.configure(state=tk.DISABLED)

    def __addDataFields(self):
        self.data_container = tk.Frame(self.container,
                                       name="data_frame",
                                       bd=0,
                                       # highlightbackground='#000000',
                                       # highlightcolor='#000000',
                                       # highlightthickness='0.5p',
                                       relief=tk.FLAT)
        self.data_container.pack(side=tk.TOP, padx='1m', pady='1m')

        self.header = []
        if self.__opened_file_extension == ".csv":
            with open(self.__opened_file, 'r') as csv_file:
                self.reader = pd.read_csv(csv_file)
                self.header = self.reader.columns
            csv_file.close()

        self.rows = len(self.reader)
        self.columns = len(self.header)
        print(self.rows)
        print(self.columns)

        self.__addColumnNames()
        self.__feedData()

    def __addColumnNames(self):
        self.header_container = tk.Frame(self.data_container,
                                         bd=0,
                                         highlightbackground='#000000',
                                         highlightcolor='#000000',
                                         highlightthickness='0.5p',
                                         relief=tk.FLAT)
        self.header_container.pack(side=tk.TOP)

        columns = len(self.header)
        for col in range(0, columns):
            print(self.header[col], col)
            header_field = tk.Entry(self.header_container,
                                    name="head({0})".format(col),
                                    width=15,
                                    bd=0,
                                    bg='#ffffff',
                                    disabledbackground="#dddddd",
                                    disabledforeground="#000000",
                                    insertontime=600,
                                    insertofftime=600,
                                    font=FONT_CAMBRIA_11,
                                    highlightbackground='#aaaaaa',
                                    highlightcolor='#0000FF',
                                    highlightthickness='0.5p',
                                    relief=tk.FLAT)
            header_field.insert(0, self.header[col])
            header_field.grid(row=0, column=col)
            header_field.configure(state=tk.DISABLED)

    def __feedData(self):
        self.values_container = tk.Frame(self.data_container,
                                         bd=0,
                                         highlightbackground='#000000',
                                         highlightcolor='#000000',
                                         highlightthickness='0.5p',
                                         relief=tk.FLAT)
        self.values_container.pack(side=tk.TOP)

        validate_function = (self.values_container.register(self.__validateValue), '%P', '%W')

        self.__entry_fields = []

        if self.rows > 200:
            self.rows = 200

        print("Rows:", self.rows)
        print("Columns:", self.columns)
        for row in range(0, self.rows):
            for col in range(0, self.columns):
                val = self.__getValue(row, col)
                entry_field = tk.Entry(self.values_container,
                                       name="cell({0},{1})".format(row, col),
                                       width=15,
                                       bd=0,
                                       bg='#ffffff',
                                       insertontime=600,
                                       insertofftime=600,
                                       font=FONT_CAMBRIA_11,
                                       highlightbackground='#aaaaaa',
                                       highlightcolor='#0000FF',
                                       highlightthickness='0.5p',
                                       relief=tk.FLAT)
                entry_field.insert(0, val)
                entry_field.configure(validate='all', validatecommand=validate_function,)
                entry_field.grid(row=row, column=col)
                self.__entry_fields.append(entry_field)

    def __getValue(self, row, col):
        return self.reader[self.header[col]][row]

    def __validateValue(self, changed_value, widget_name):
        # print("Validating IP\n{0}".format(widget_name))
        return False

    def __addButtons(self):
        self.button_container = tk.Frame(self.container,
                                         bg="#dddddd",
                                         relief=tk.FLAT)
        self.button_container.pack(side=tk.BOTTOM, fill=tk.X)
        self.button_container.grid_columnconfigure(0, weight=1)

        self.reset_button = tk.Button(self.button_container,
                                      width=15,
                                      # height=1,
                                      text="Reset to default",
                                      font=FONT_CAMBRIA_10,
                                      activebackground='#7EB6FF',
                                      command=lambda: self.__resetData(),
                                      # padx='2m',
                                      # pady='1m',
                                      state=tk.NORMAL,
                                      relief=tk.GROOVE)
        self.reset_button.grid(row=0, column=9, sticky=tk.E, pady='2m 2m')

        self.save_button = tk.Button(self.button_container,
                                     width=10,
                                     # height=1,
                                     text="Save",
                                     font=FONT_CAMBRIA_10,
                                     activebackground='#7EB6FF',
                                     command=lambda: self.__saveData(),
                                     # padx='2m',
                                     # pady='1m',
                                     state=tk.NORMAL,
                                     relief=tk.GROOVE)
        self.save_button.grid(row=0, column=10, sticky=tk.E, padx="4m 5m", pady='2m 2m')

    def __resetData(self):
        pass

    def __saveData(self):
        pass
