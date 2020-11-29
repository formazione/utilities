import win32clipboard
from gtts import gTTS
import time
import tkinter as tk
import os


def create_mp3(text, lang="en"):
    s = gTTS(text, lang=lang)
    print("Wait a second...")
    time.sleep(5)
    s.save(f"text.mp3")
    os.system("text.mp3")

trycount = 0
def clip():
	global trycount


	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	try:
		create_mp3(data)
	except:
		trycount += 1
		if trycount < 3:
		    ocr()
	else:
	    print("Some problems with connection maybe")

root = tk.Tk()
root.title("Select the text, press crtl + c then press the button")
root.geometry("400x200")
but = tk.Button(root, text="Get audio from clipboard", command=clip, width=20,height=10, bg="gold")
but.pack()


root.mainloop()