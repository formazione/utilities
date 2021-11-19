def tkinput(text) -> str:
	import tkinter as tk

	root = tk.Tk()
	question = tk.StringVar()
	tk.Label(root, text=text).pack()
	e = tk.Entry(root, textvariable=question)
	e.pack()
	e.focus()
	# question.set("prova")
	e.bind("<Return>", lambda event: root.destroy())
	root.mainloop()
	print(type(question.get()))
	return question.get()



if __name__ == '__main__':
	name = tkinput("What is your name?")
	print(f"{name=}")
	

