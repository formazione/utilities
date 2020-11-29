# grabscreen.py
import win32clipboard
import pyscreenshot as ImageGrab
import os
from pynput.mouse import Listener
import sys
import tkinter as tk
from gtts import gTTS
import time

'''
        Grab a text from an image
        grabbed clickin on the left top corner
        and right down corner of the part of the screen
        with the text.
        It returns it in the console
        Then... it transform it into audio.

'''

import pytesseract


def grab(x, y, w, h):
    im = ImageGrab.grab(bbox=(x, y, w, h))
    save(im)
    ocr()


def save(im):
    im.save('im.png')
    os.startfile('im.png')

trycount = 0
def ocr():
    global trycount


    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    text = pytesseract.image_to_string(r'im.png')
    print(text)
    try:
        create_mp3(text)
    except:
        trycount += 1
        if trycount < 3:
            ocr()
        else:
            print("Some problems with connection maybe")
            trycount2 = 0

def create_mp3(text, lang="en"):
    s = gTTS(text, lang=lang)
    print("Wait a second...")
    time.sleep(3)
    s.save(f"text.mp3")
    os.system("text.mp3")

trycount2 = 0
def clip():
    global trycount2


    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    try:
        create_mp3(data)
    except:
        trycount2 += 1
        if trycount2 < 3:
            ocr()
    else:
        print("Some problems with connection maybe")
        trycount2 = 0


click1 = 0
x1 = 0
y1 = 0
def on_click(x, y, button, pressed):
    global click1, x1, y1, listener
    
    if pressed:
        if click1 == 0:
            x1 = x
            y1 = y
            click1 = 1
        else:
            grab(x1, y1, x, y)
            listener.stop()
            sys.exit()
def start():
    global listener

    root.destroy()
    print("Click once on top left and once on bottom right")
    # with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    with Listener(on_click=on_click) as listener:
        listener.join()
        # listener.stop()
        # sys.exit()

root = tk.Tk()
root.title("GRAUTESC 2 - Text to Audio APP")
root.geometry("200x200")
but = tk.Button(root, text="GRAB GET IMAGE", command=start, width=20,height=5, bg="gold")
but.pack()
butclip = tk.Button(root, text="Get audio from clipboard", command=clip, width=20,height=5, bg="gold")
butclip.pack()

root.mainloop()