# import tkinter as tk
# from tkinter import filedialog
# import os
#
# application_window = tk.Tk()
#
# # Build a list of tuples for each file type the file dialog should display
# my_filetypes = [('all files', '.*'), ('text files', '.txt')]
#
# # Ask the user to select a folder.
# answer = filedialog.askdirectory(parent=application_window,
#                                  initialdir=os.getcwd(),
#                                  title="Please select a folder:")
#
# # Ask the user to select a single file name.
# answer = filedialog.askopenfilename(parent=application_window,
#                                     initialdir=os.getcwd(),
#                                     title="Please select a file:",
#                                     filetypes=my_filetypes)
#
# # Ask the user to select a one or more file names.
# answer = filedialog.askopenfilenames(parent=application_window,
#                                      initialdir=os.getcwd(),
#                                      title="Please select one or more files:",
#                                      filetypes=my_filetypes)
#
# # Ask the user to select a single file name for saving.
# answer = filedialog.asksaveasfilename(parent=application_window,
#                                       initialdir=os.getcwd(),
#                                       title="Please select a file name for saving:",
#                                       filetypes=my_filetypes)
#

# Apoorva's Code
import tkinter as t
from tkinter import *
root = t.Tk()

root.title("MY TITLE")
# root.geometry("700x700")
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.configure(background='light blue')

display = t.Label(root, text="Data Visualization And Analysis Tool For Water Surface Vehicle",font=('helvetica',10, 'bold'))
display.grid(row=0)

button=t.Button(root,text="select file",font=('helvetica',10, 'bold'))
button.config( height = 2, width = 8)

# button.pack(side=t.TOP,row=10,column=20,padx=200,pady=200)
button.grid(row=10,column=10,padx=200,pady=200, sticky=t.W)

button1=t.Button(root,text="visualize",font=('helvetica',10, 'bold'))
button1.config(height = 2, width = 8)
button1.grid(row=21,column=7,padx=30)
button2=t.Button(root,text="analyse",font=('helvetica',10, 'bold'))
button2.config(height = 2, width = 8)
button2.grid(row=21,column=13)
root.mainloop()