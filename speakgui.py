"""Use gtts with Python.

Create mp3 from text with python, tkinter and gtts
2018
@ Giovanni Gatto
"""

# A PROGRAM FROM GIOVANNI GATTO AKA EDUCATIONAL CHANNEL ON YOUTUBE
# AKA PYTHONPROGRAMMI ON TWITTER
# published on http://pythonprogramming.altervista.org

from gtts import gTTS
import os
import tkinter as tk

root = tk.Tk()
root.geometry("400x400+500+100")

# THE ACTION LINKED TO THE EVENT LISTENER
def create_mp3(lang="en"):

    print(lan.get())
    if lan.get() != None:
        lang = str(lan.get())
    s = gTTS(text.get(0.0, tk.END), lang=lang)
    s.save(f"{str(mp3.get())}.mp3")
    filename = mp3.get() + ".mp3"
    os.system("start " + filename)

# THE FIRST LABEL TELLS YOU WHAT TO DO TO MAKE IT WORK
title = tk.Label(root, text="PRESS ENTER TO HEAR THE TEXT")
title.pack()
title['bg'] = 'yellow'
# WHERE YOU WRITE THE TEXT

# THE LANGUAGE
    # THE LABEL
l2 = tk.Label(root, text="Choose language (default is english=en)")
l2.pack()
    # THE ENTRY WIDGET
lan = tk.StringVar()
language = tk.Entry(root, textvariable=lan)
language.pack()
lan.set("en")

# THE NAME OF THE FILE
mp3 = tk.StringVar()
mp3title = tk.Entry(root, textvariable=mp3, width=50)
mp3title.pack()
mp3.set("myfile")

# THE EVENT LISTENER
root.bind("<Return>", lambda x: create_mp3())

t = tk.StringVar()
text = tk.Text(root, bg="gold")
text.pack()

root.mainloop()