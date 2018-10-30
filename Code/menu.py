import tkinter as tk


class Menu(tk.Menu):

    def __init__(self, parent, auto_attach=True):
        tk.Menu.__init__(self, parent)
        self.file_browser_text = tk.StringVar()
        if auto_attach:
            parent.configure(menu=self)

    def _addFileMenu(self, recent_files):
        self.file_menu = tk.Menu(self, tearoff=0)
        self.recent_menu = tk.Menu(self.file_menu, tearoff=0)
        self.file_menu.add_cascade(label="Open Recent", menu=self.recent_menu, underline=0)
        self.file_menu.add_command(label="Settings", command=self.__settingsHandler, underline=0)

        # Add separator for quit option
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit", command=self.__quitHandler, underline=0)
        self.add_cascade(label="File", menu=self.file_menu)

        if len(recent_files) > 0:
            self.__addFilesInRecentsMenu(recent_files)
        else:
            self.file_menu.entryconfigure(0, state=tk.DISABLED)

    def __addFilesInRecentsMenu(self, file_path, count=0):
        print("Adding files in recents menu")
        file_path_with_count = "{0}. {1}".format(count, file_path)
        self.recent_menu.add_command(label=file_path_with_count, command=lambda: self.openRecentFileHandler(file_path))
        # for file in recent_files:
        #     if os.path.isfile(file):

    @staticmethod
    def __settingsHandler():
        print("Settings Handler Called")

    # If it does not work properly i.e. if it can't call parent callback function for quiting,
    # delete this option.
    def __quitHandler(self):
        print("Calling destroy from Menu.")
        self.master.destroy()

    def openRecentFileHandler(self, file_path):
        self.file_browser_text.set(file_path)
        print("Callback from Menu")

    def updateRecentsMenu(self, file_path, count):
        print(file_path)
        if len(file_path) > 0:
            self.file_menu.entryconfigure(0, state=tk.NORMAL)
            self.__addFilesInRecentsMenu(file_path, count)
        else:
            self.file_menu.entryconfigure(0, state=tk.DISABLED)
