# grabscreen.py

import pyscreenshot as ImageGrab
import os
from PIL import Image
from io import BytesIO
import win32clipboard
import pygame
import win32api
import win32con
import win32gui
import tkinter as tk


def destroy():
    root.destroy()

root = tk.Tk()
b = tk.Button(root, text="Click to Capture screen",
    fg='red',
    bg='yellow',
    font="Arial 36",
    command=root.destroy)
b.pack()
root.mainloop()

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

pygame.init()
info = pygame.display.Info()
w = info.current_w
h = info.current_h
screen = pygame.display.set_mode((w, h), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
done = False
fuchsia = (255, 0, 128)  # Transparency color

# Create layered window
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# Set window transparency color
# win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 50, win32con.LWA_ALPHA)

click1 = 0
x1 = 0
y1 = 0
x2 = 0
y2 = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            # time.sleep(.1)
            if click1 == 0:
                x1, y1 = pygame.mouse.get_pos()
                click1 = 1
            elif click1 == 1:
                x2, y2 = pygame.mouse.get_pos()
                dx = x1 + (x2 - x1)
                dy = y1 + (y2 - y1)
                win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_ALPHA)
                grab(x1, y1, dx, dy)
                click1 = 0
                # Sh
                # done = True
                win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 50, win32con.LWA_ALPHA)
                x1 = 0
                y1 = 0
                x2 = 0
                y2 = 0
    screen.fill((255, 255, 255))  # Transparent background
    # show_text()
    if click1 == 0:
        mx, my = pygame.mouse.get_pos()
        dx = 5
        dy = 5
    elif click1 == 1:
        mx2, my2 = pygame.mouse.get_pos()
        x2 = mx2 - x1
        y2 = my2 - y1

    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(mx, my, x2, y2))
    pygame.display.update()

pygame.quit()
