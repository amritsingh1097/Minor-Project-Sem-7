import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd
import menu
import sd_window as sd
import dv_window as dv
# import da_window as da

FONT_CAMBRIA_10 = ("Cambria", "10")
FONT_CAMBRIA_11 = ("Cambria", "11")


class RootWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.protocol("WM_DELETE_WINDOW", self.quitCallback)
        self.title('ROOT')
        self.iconbitmap("icon.ico")
        self.geometry('+150+100')
        self.resizable(False, False)

        # Container to contain main page
        self.container = tk.Frame(self, bg='#000000')
        self.container.pack(side='top', fill='both', expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.__recent_files = []

        self.__sd_win_id = 0
        self.__dv_win_id = 0
        self.__da_win_id = 0

        # Variables to store data to view in 'At Glance' section.
        self.relation_name = "None"
        self.row_count = 0
        self.column_count = 0
        self.binary_column_count = 0
        self.nominal_column_count = 0
        self.numeric_column_count = 0

        self.__addMenuBar()
        self.__addAtGlanceSection()
        self.__addFileBrowserSection()
        self.__addOperationsSection()

        # Below line are just for testing. Remove these when testing is complete.
        self.menu_bar.file_browser_text.set("E:/Minor Project/Datasets/iris/Iris.csv")
        self.__visualizeData()
        # self.__showData()

    def __addMenuBar(self):
        self.menu_bar = menu.Menu(self)
        self.menu_bar._addFileMenu(self.__recent_files)

    def __addAtGlanceSection(self):
        self.at_glance_container = tk.Frame(self.container, padx='2m', pady='2m')
        self.at_glance_container.pack(side=tk.TOP, fill=tk.X)
        self.at_glance_container.grid_columnconfigure(0, weight=1)

        self.at_glance_label = tk.Label(self.at_glance_container,
                                        justify=tk.LEFT,
                                        font=FONT_CAMBRIA_11,
                                        text="At Glance:")
        self.at_glance_label.grid(row=0, column=0, sticky=tk.W, padx='2m')

        self.__addDescriptionSection()

    def __addDescriptionSection(self):
        self.glance_container = tk.Frame(self.at_glance_container,
                                         bg="#dddddd",
                                         padx='3m',
                                         pady='2m',
                                         relief=tk.FLAT)
        self.glance_container.grid(row=1, column=0, sticky=tk.EW, padx='2m')
        self.glance_container.grid_columnconfigure(0, weight=1)
        self.glance_container.grid_columnconfigure(1, weight=1)

        row_keys = ["Relation:",
                    "Row count:",
                    "Column count:",
                    "Binary columns:",
                    "Nominal columns:",
                    "Numeric columns:"]
        for row in range(0, len(row_keys)):
            tk.Label(self.glance_container,
                     bg=self.glance_container['bg'],
                     justify=tk.LEFT,
                     font=FONT_CAMBRIA_10,
                     text=row_keys[row]).grid(row=row, column=0, sticky=tk.W)

        self.glance_labels = []
        for row in range(0, len(row_keys)):
            label = tk.Label(self.glance_container,
                             bg=self.glance_container['bg'],
                             justify=tk.LEFT,
                             font=FONT_CAMBRIA_10)
            label.grid(row=row, column=1, sticky=tk.W)
            self.glance_labels.append(label)

        self.__updateAtGlance()

        # self.label_frame = tk.LabelFrame(self.at_glance_container)

    def __updateAtGlance(self):
        row_values = [self.relation_name,
                      self.row_count,
                      self.column_count,
                      self.binary_column_count,
                      self.nominal_column_count,
                      self.numeric_column_count]

        for row in range(0, len(self.glance_labels)):
            print(row_values[row])
            self.glance_labels[row].configure(text=row_values[row])

    def __addFileBrowserSection(self):
        self.browser_container = tk.Frame(self.container, padx='2m', pady='2m')
        self.browser_container.pack(side=tk.TOP, fill=tk.X)
        self.browser_container.grid_columnconfigure(0, weight=3)
        self.browser_container.grid_columnconfigure(1, weight=1)

        self.choose_label = tk.Label(self.browser_container,
                                     justify=tk.LEFT,
                                     font=FONT_CAMBRIA_11,
                                     text='Choose file...')
        self.choose_label.grid(row=0, column=0, sticky=tk.W, padx='2m')

        self.__addFileBrowser()
        self.__addBrowseButton()

    def __addFileBrowser(self):
        # self.file_browser_text = tk.StringVar()
        validate_function = (self.browser_container.register(self.__validateFilePath), '%P', '%W')
        self.file_browser_entry_field = tk.Entry(self.browser_container,
                                                 width=40,
                                                 bd=0,
                                                 insertontime=600,
                                                 insertofftime=600,
                                                 font=FONT_CAMBRIA_11,
                                                 textvariable=self.menu_bar.file_browser_text,
                                                 highlightbackground='#000000',
                                                 highlightcolor='#5555FF',
                                                 highlightthickness='0.7p',
                                                 validate='all',
                                                 validatecommand=validate_function,
                                                 relief=tk.GROOVE)

        # self.file_browser_entry_field.focus_set()
        # self.file_browser_text.set('E:/Programs/Python/Sem 7/BI Lab/Datasets/iris-species/Iris.csv')
        # self.file_browser_entry_field.pack(side=tk.LEFT, padx=20)
        self.file_browser_entry_field.grid(row=1, column=0, sticky=tk.N+tk.S, columnspan=1, padx='2m', pady='0m')
        # self.file_browser_entry_field.grid_columnconfigure(0, weight=3)

    def __addBrowseButton(self):
        browse_button = tk.Button(self.browser_container,
                                  # width=30,
                                  height=1,
                                  font=FONT_CAMBRIA_11,
                                  activebackground='#7EB6FF',
                                  text="Browse",
                                  command=lambda: self.__selectFile(),
                                  padx='3m',
                                  pady='0m',
                                  relief=tk.GROOVE)
        # browse_button.pack(side=tk.RIGHT, padx=20)
        browse_button.grid(row=1, column=1, sticky=tk.N+tk.S, columnspan=1, padx='2m', pady='0m')
        # browse_button.grid_columnconfigure(1, weight=1)

    def __selectFile(self):
        file_types = [('Files - *.csv; *.arff; *.json', '*.csv;*.arff;*.json'),
                      ('CSV File - *.csv', '*.csv'),
                      ('ARFF File - *.arff', '*.arff'),
                      ('JSON File - *.json', '*.json')]

        selected_file_name = filedialog.askopenfilename(filetypes=file_types)
        print('Selected File', selected_file_name)

        if selected_file_name != "":
            self.menu_bar.file_browser_text.set(selected_file_name)

    def __validateFilePath(self, changed_file_path, widget_name):
        # print("Validating path\n{0}".format(widget_name))

        # Enable/Disable the buttons based on the existence of the file.
        if os.path.isfile(changed_file_path):
            self.sd_button.configure(state=tk.NORMAL)
            self.dv_button.configure(state=tk.NORMAL)
            self.da_button.configure(state=tk.NORMAL)
            if len(self.__recent_files) < 10 and changed_file_path not in self.__recent_files:
                # print("If condition")
                self.__recent_files.append(changed_file_path)
                self.menu_bar.updateRecentsMenu(changed_file_path, len(self.__recent_files))
        else:
            self.sd_button.configure(state=tk.DISABLED)
            self.dv_button.configure(state=tk.DISABLED)
            self.da_button.configure(state=tk.DISABLED)
        # print("d: {0}\ni: {1}\nP: {2}\ns: {3}\nS: {4}\nv: {5}\nV: {6}\nW: {7}\n".format(d, i, P, s, S, v, V, W))

        # Get the extension of the file and call the corresponding file processing function.
        self.extension = os.path.splitext(changed_file_path)[1]
        print(self.extension)

        if self.extension == '.csv':
            self.__processFileCSV(changed_file_path)
        if self.extension == '.arff':
            self.__processFileARFF(changed_file_path)
        if self.extension == '.json':
            self.__processFileJSON(changed_file_path)
        return True

    def __addOperationsSection(self):
        self.operations_container = tk.Frame(self.container, padx='2m', pady='2m')
        self.operations_container.pack(side=tk.TOP, fill=tk.X)
        self.operations_container.grid_columnconfigure(0, weight=1)
        self.operations_container.grid_columnconfigure(1, weight=1)
        self.operations_container.grid_columnconfigure(2, weight=1)

        self.__addOperationsButtons()

    def __addOperationsButtons(self):
        self.sd_button = tk.Button(self.operations_container,
                                   width=10,
                                   # height=1,
                                   text="Show Data",
                                   font=FONT_CAMBRIA_11,
                                   activebackground='#7EB6FF',
                                   command=lambda: self.__showData(),
                                   padx='3m',
                                   pady='1m',
                                   state=tk.DISABLED,
                                   relief=tk.GROOVE)
        self.sd_button.grid(row=0, column=0, pady='3m 5m')

        self.dv_button = tk.Button(self.operations_container,
                                   width=10,
                                   height=1,
                                   text="Visualize",
                                   font=FONT_CAMBRIA_11,
                                   activebackground='#7EB6FF',
                                   command=lambda: self.__visualizeData(),
                                   padx='3m',
                                   pady='1m',
                                   state=tk.DISABLED,
                                   relief=tk.GROOVE)
        self.dv_button.grid(row=0, column=1, pady='3m 5m')

        self.da_button = tk.Button(self.operations_container,
                                   width=10,
                                   height=1,
                                   text="Analyse",
                                   font=FONT_CAMBRIA_11,
                                   activebackground='#7EB6FF',
                                   command=lambda: self.__analyseData(),
                                   padx='3m',
                                   pady='1m',
                                   state=tk.DISABLED,
                                   relief=tk.GROOVE)
        self.da_button.grid(row=0, column=2, pady='3m 5m')

    def __showData(self):
        print('Showing Data')
        self.sd_window = sd.Window(self, self.__sd_win_id, self.file_browser_entry_field.get(), self.extension)
        self.sd_window.focus_set()
        self.__sd_win_id += 1

    def __visualizeData(self):
        print('Visualizing Data')
        self.dv_window = dv.Window(self, self.__dv_win_id, self.file_browser_entry_field.get(), self.extension)
        self.dv_window.focus_set()
        self.__dv_win_id += 1

    def __analyseData(self):
        pass

    def __processFileCSV(self, file):
        print('Processing CSV File - ', file, self.extension)
        with open(file, 'r') as csv_file:
            reader = pd.read_csv(csv_file)
            print(reader.columns[0])
        csv_file.close()

        # Update 'At Glance' variables and call update function.
        file_name = file.split('/')[-1]
        self.relation_name = file_name.split('.')[0]
        self.row_count = len(reader)
        self.column_count = len(reader.columns)
        self.__updateAtGlance()

    def __processFileARFF(self, file):
        print('Processing ARFF File - ', file, self.extension)

    def __processFileJSON(self, file):
        print('Processing JSON File - ', file, self.extension)

    def quitCallback(self):
        print("Quiting...")
        self.destroy()
