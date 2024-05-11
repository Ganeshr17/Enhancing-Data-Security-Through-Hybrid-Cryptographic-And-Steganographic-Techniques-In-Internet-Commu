from tkinter import *
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk
import os
import customtkinter
import sys
import importlib

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")

sg = customtkinter.CTk()
width = sg.winfo_screenwidth()
height = sg.winfo_screenheight()
window_width = int(1.02 * width)
window_height = int(1.02 * height)
# Set the window geometry to be centered and with margin
x_offset = (width - window_width) // 2
y_offset = (height - window_height) // 2
sg.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
sg.title("Stegnography")
script_dir = os.path.dirname(__file__)
f1 = tkFont.Font(family="Helvetica", size=30, weight="bold")
sg.configure(bg="#242424")

image_path = os.path.join(script_dir, "encryption.png")
image = Image.open(image_path)

image = image.resize((60, 60))
# Convert the image to a format compatible with Tkinter
tk_image = ImageTk.PhotoImage(image)

image_path1 = os.path.join(script_dir, "decryption.png")
image1 = Image.open(image_path1)

image1 = image1.resize((60, 60))
# Convert the image to a format compatible with Tkinter
tk_image1 = ImageTk.PhotoImage(image1)


def nextPage():
    sg.destroy()
    import first_page


def prevPage():
    sg.destroy()
    import second_page


Label(
    sg,
    text="Stegno",
    font=f1,
    justify=CENTER,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="#fdbb2d",
).place(x=900, y=80)
f = tkFont.Font(family="Helvetica", size=24, weight="bold")

# f2 = tkFont.Font(family="Comic Sans MS", size=20, weight="bold", slant="italic")
# f3 = tkFont.Font(family="Arial", size=20)

bt1 = Button(
    sg,
    text="Image Encryption",
    font=f,
    borderwidth=1,  # Set border width to 0 to remove the default border
    highlightthickness=5,
    relief="solid",
    bg=sg.cget("bg"),
    activebackground=sg.cget("bg"),
    fg="white",
    command=nextPage,
    width=450,
    height=350,
    background="#2b2b2b",
    compound="top",
    image=tk_image,
    pady=20,
    cursor="hand2",
)
bt1.pack(expand=True, side=LEFT)

bt2 = Button(
    sg,
    text="Image Decryption",
    font=f,
    borderwidth=1,  # Set border width to 0 to remove the default border
    highlightthickness=5,
    relief="solid",
    bg=sg.cget("bg"),
    activebackground=sg.cget("bg"),
    fg="white",
    command=prevPage,
    width=450,
    height=350,
    background="#2b2b2b",
    compound="top",
    image=tk_image1,
    pady=20,
    cursor="hand2",
)
bt2.pack(expand=TRUE, side=LEFT)

sg.configure()
sg.mainloop()
