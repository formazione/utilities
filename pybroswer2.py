import tkinter as tk
import os

def searchfiles(extension='.txt', folder='H:\\'):
    "insert all files in the listbox"
    global listbox
    
    container = []
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                container.append(os.path.join(r, file))
   
    for file in container:
    	lbx.insert(0, file)

def open_file():
    os.startfile(lbx.get(lbx.curselection()[0]))

def clear():
	lbx.delete(0, tk.END)


def label(text):
	lab_en = tk.Label(frame1, text=text)
	lab_en.pack(side="top")
	return lab_en

def entry(text="H:\\"):
	"Visualize an entry"
	en = tk.Entry(frame1)
	en.insert(0, text)
	en["bg"] = "gold"
	en.pack(fill="x")
	en.bind("<Return>", lambda x:searchfiles('.png', en.get()))
	en.focus()
	return en


def button(text, command):
	# BUTTON TO START SEARCH
	bt = tk.Button(frame1, text=text, command=command)
	bt.pack(side="left")
	return bt


def listbox():
	lbx = tk.Listbox(frame2)
	lbx.pack(fill="both", expand=1)
	lbx.bind("<Double-Button>", lambda x: open_file())
	return lbx


def main():
	global lbx

	root.title("My search engine")
	root.geometry("400x400")
	root['bg'] = "orange"
	# ENTRY FOR THE FOLDER TO START THE SEARCH FROM
	# Label, entry, button 1 and 2, listbox
	lab = label("The root folder:")
	en = entry()
	bt1 = button("Search", lambda:searchfiles('.png', en.get()))
	bt2 = button("Clear", clear)
	frame1.pack(fill="x")
	lbx = listbox()
	frame2.pack(fill="both", expand=1)
	root.mainloop()


root = tk.Tk()
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
main()
