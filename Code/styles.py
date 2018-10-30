from tkinter import ttk


class Window(ttk.Style):

    def __init__(self, *args, **kwargs):
        ttk.Style.__init__(self, *args, **kwargs)

    def getButtonStyles(self):
        pass

    def getEntryStyles(self):
        pass

    def getLabelStyles(self):
        pass
