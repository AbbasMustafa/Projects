from tkinter import *
import tkinter.filedialog
import os
from Logic import logic



def callBrowse(flag):
	root.withdraw() #use to hide tkinter window
	currdir = os.getcwd()
	tempdir = tkinter.filedialog.askdirectory(parent=root, initialdir=currdir,
											 title='Please select a directory')
	if flag:
		global source
		source = tempdir
		source_lbl.config(text=f"Source: {source}")
	else:
		global Destination
		Destination = tempdir
		dest_label.config(text=f"Destination: {Destination}")

	root.deiconify() #use to show tkinter window

def callback(selection):
	global fileExt
	fileExt = selection



root = Tk()

variable = StringVar(root)
variable.set("PDF") 

Label(root, text="Select Path Directory").grid(row=0, column=0)
Button(root, text="Browse", width=20,
	activebackground="BLACK", activeforeground="WHITE",
	command=lambda: callBrowse(True)).grid(row=0, column=1)

source_lbl = Label(root, text="Source: ")
source_lbl.grid(row=1,column=0,columnspan=2)

Label(root, text="Select File Ext.").grid(row=2,column=0)
OptionMenu(root, variable, "pdf", "txt", "py",
			 command=callback).grid(row=2, column=1)

Label(root, text="Destination Location").grid(row=3, column=0)
Button(root, text="Browse", width=20,
	activebackground="BLACK", activeforeground="WHITE",
	command=lambda: callBrowse(False)).grid(row=3, column=1)

dest_label = Label(root, text="Destination: ")
dest_label.grid(row=4,column=0,columnspan=2)

Button(root, text="Move"
	,activebackground="BLACK", width=20,
	 activeforeground="WHITE",
	 command=lambda: logic(source, Destination, False, fileExt)).grid(row=5, column=0)
Button(root, text="Copy", width=20,
	activebackground="BLACK",
	 activeforeground="WHITE",
	 command=lambda: logic(source, Destination, True, fileExt)).grid(row=5, column=1)


root.mainloop()