import tkinter as tk
import os

def searchfiles(extension='.txt', folder='H:\\'):
    "insert all files in the listbox"
    container = []
    for r, d, f in os.walk(folder):
        for file in f:
            if file.endswith(extension):
                container.append(os.path.join(r, file))
   
    for file in container:
    	lb.insert(0, file)

def open_file():
    os.startfile(lb.get(lb.curselection()[0]))

def clear():
	lb.delete(0, tk.END)

root = tk.Tk()
root.geometry("400x400")
# ENTRY FOR THE FOLDER TO START THE SEARCH FROM
lab_en = tk.Label(root, text="Start folder")
lab_en.pack()
en = tk.Entry(root)
en.insert(0, "H:\\")
en.pack()

# BUTTON TO START SEARCH
bt = tk.Button(root, text="Search", command=lambda:searchfiles('.png', en.get()))
bt.pack()

bt2 = tk.Button(root, text="Clear", command=clear)
bt2.pack()

lb = tk.Listbox(root)
lb.pack(fill="both", expand=1)
lb.bind("<Double-Button>", lambda x: open_file())
root.mainloop()