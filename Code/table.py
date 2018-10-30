import tkinter as tk

FONT_CAMBRIA_10 = ("Cambria", "10")
FONT_CAMBRIA_11 = ("Cambria", "11")


class Table(tk.Frame):

    def __init__(self, parent, rows, columns, header=[]):
        tk.Frame.__init__(self, parent,
                          bd=0,
                          relief=tk.FLAT)
        self.pack(side='top', fill='both', expand=True)
        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        self.__fields = []
        print(header)

        if len(header) != 0:
            self.__addHeader(header)

        self.__addDataFields(rows, columns)

    def __addHeader(self, header):
        self.header_container = tk.Frame(self,
                                         bd=0,
                                         highlightbackground='#000000',
                                         highlightcolor='#000000',
                                         highlightthickness='0.5p',
                                         relief=tk.FLAT)
        self.header_container.pack(side=tk.TOP, padx='1m', pady='1m')
        col = 0
        for head in header:
            print(head, col)
            header_field = tk.Entry(self.header_container,
                                    name="head({0})".format(col),
                                    width=10,
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
            header_field.insert(0, head)
            header_field.grid(row=0, column=col)
            header_field.configure(state=tk.DISABLED)
            col += 1

    def __addDataFields(self, rows, columns):
        self.data_container = tk.Frame(self,
                                       bd=0,
                                       highlightbackground='#000000',
                                       highlightcolor='#000000',
                                       highlightthickness='0.5p',
                                       relief=tk.FLAT)
        self.data_container.pack(side=tk.TOP)#, padx='1m', pady='1m')
        validate_function = (self.register(self.__validateFilePath), '%P', '%W')

        for row in range(0, rows):
            for col in range(0, columns):
                entry_field = tk.Entry(self.data_container,
                                       name="cell({0},{1})".format(row, col),
                                       width=10,
                                       bd=0,
                                       bg='#ffffff',
                                       disabledbackground="#eeeeee",
                                       disabledforeground="#555555",
                                       insertontime=600,
                                       insertofftime=600,
                                       font=FONT_CAMBRIA_11,
                                       highlightbackground='#aaaaaa',
                                       highlightcolor='#0000FF',
                                       highlightthickness='0.5p',
                                       validate='all',
                                       validatecommand=validate_function,
                                       relief=tk.FLAT)
                entry_field.grid(row=row, column=col)
                self.__fields.append(entry_field)

    def __validateFilePath(self, changed_value, widget_name):
        print("Validating IP\n{0}".format(widget_name))
        return True
