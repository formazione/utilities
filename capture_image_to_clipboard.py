# grabscreen.py

import pyscreenshot as ImageGrab
import os
from pynput.mouse import Listener
import sys
import tkinter as tk
from PIL import Image

from io import BytesIO
import win32clipboard


''' Derives from my script grab (use this to show text in a pic and
transform in audio)


'''

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def grab(x, y, w, h):
    im = ImageGrab.grab(bbox=(x, y, w, h))
    im.save('im.png')
    image = Image.open("im.png")
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)


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
            click1 = 0
            # sys.exit()

def start():
    global listener

    # root.destroy()
    print("Click once on top left and once on bottom right")
    # with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
    with Listener(on_click=on_click) as listener:
        listener.join()
        # listener.stop()
        # sys.exit()

root = tk.Tk()
root.geometry("400x200")
'''
when you click on this button goes to start
in start there i a listener and when you click it sends you to on_click
in on_click it makes you click twice and then goes to grab
in grab it uses pyscreenshot functions to grab the image and save it
we do not use ocr here, to do it use the grab.py file
'''
but = tk.Button(root, text="GRAB GET IMAGE", command=start, width=20,height=10, bg="gold")
but.pack()

root.mainloop()
listener.stop()
sys.exit()
