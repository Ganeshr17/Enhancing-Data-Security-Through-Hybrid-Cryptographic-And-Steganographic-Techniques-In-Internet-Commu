import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style
import os
import base64
from tkinter import *
import compress_new2 as cd
import AES_Hash as en
import time
from tkinter import filedialog
import tkinter.font as tkFont
import pyperclip
import img_txt as imt
import stegnno_embed as embd
import pickle
import stegano
from stegano import lsb
import Performance_Metrics as pm
from PIL import Image, ImageTk
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")


key = ""
sg = customtkinter.CTk()
width = sg.winfo_screenwidth()
height = sg.winfo_screenheight()
window_width = int(1.02 * width)
window_height = int(1.02 * height)
# Set the window geometry to be centered and with margin
x_offset = (width - window_width) // 2
y_offset = (height - window_height) // 2
sg.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
sg.title("Embedding")
f = ("Times bold", 14)
sg.configure(bg="#242424")
script_dir = os.path.dirname(__file__)
tick = os.path.join(script_dir, "green_tick.png")
tick_image = Image.open(tick)
tick_image = tick_image.resize((20, 20))
tick_image = ImageTk.PhotoImage(tick_image)
style = ttk.Style()
style.configure("Custom.TCheckbutton", relief="solid", background=sg.cget("bg"))

tfn = ("Helvetica", 30, "bold")
title = Label(
    sg,
    text="Image Encryption",
    justify="center",
    font=tfn,
    bg=sg.cget("bg"),
    fg="white",
)
title.place(x=860, y=25)

tick_label_cover = None
tick_label_user = None


# Function to get file path for cover image
def get_file_path1():
    global cvr_file_path, tick_label_cover
    cvr_file_path = filedialog.askopenfilename(
        title="Select A File",
        filetypes=(
            ("jpg", "*.jpg"),
            ("PNG", "*.png"),
            ("mp4", "*.mp4"),
            ("wmv", "*.wmv"),
            ("avi", "*.avi"),
        ),
    )
    if cvr_file_path:
        tick_label_cover = tk.Label(image=tick_image)
        tick_label_cover.image = tick_image
        tick_label_cover.configure(bg="#2b2b2b")
        tick_label_cover.place(x=1005, y=335)
        sbmt.configure(state="normal", fg_color="#1f6aa5", text_color="white")


# Function to get file path for user image
def get_file_path():
    global file_path, tick_label_user
    file_path = filedialog.askopenfilename(
        title="Select A File",
        filetypes=(
            ("jpg", "*.jpg"),
            ("PNG", "*.png"),
            ("mp4", "*.mp4"),
            ("wmv", "*.wmv"),
            ("avi", "*.avi"),
        ),
    )
    if file_path:
        tick_label_user = tk.Label(image=tick_image)
        tick_label_user.image = tick_image
        tick_label_user.configure(bg="#2b2b2b")
        tick_label_user.place(x=609, y=335)
        fbt.configure(state="normal", fg_color="#1f6aa5", text_color="white")


def submit():
    global key_name
    key_name1 = textbox.get()
    key_name = key_name1 + str(radio_var.get())
    print(key_name)
    # lbl.config(text = "Provided Input: "+inp)
    B.configure(state="normal", fg_color="#1f6aa5", text_color="white")


cbt = ("Arial", 16)


def helloCallBack():
    global C1, lbl, comp_image, label1_comp_image, script_dir
    comp_image = cd.Compression_Process(file_path, script_dir)
    # time.sleep(1)
    C1.state(["selected"])
    comp_image = comp_image.resize((200, 200))
    comp_image = ImageTk.PhotoImage(comp_image)
    label1_comp_image = tk.Label(
        image=comp_image,
    )
    label1_comp_image.image = comp_image
    label1_comp_image.place(x=518, y=585)
    lbl.place(x=546, y=540)
    lbl.config(
        text="SUCCESSFUL",
        foreground="green",
        font=cbt,
        bg=sg.cget("bg"),
    )

    B1.configure(state="normal", fg_color="#1f6aa5", text_color="white")


def helloCallBack1():
    global key, textbox, key_name, label1_encrypted_image
    global C2, lb2, image_Encypted

    otpath = os.path.join(script_dir, "image", "compressed.jpg")
    # print(key_name)
    key = en.encrypt(otpath, key_name, script_dir)
    print(key)
    # textbox.insert(0, key)
    print(key_name)
    C2.state(["selected"])
    imt.txtconvert()

    # Construct the full path to the image file relative to the script directory
    image_path = os.path.join(script_dir, "image", "aes_gui_trail.png")

    image_Encypted = Image.open(image_path)
    image_Encypted = image_Encypted.resize((200, 200))
    image_Encypted = ImageTk.PhotoImage(image_Encypted)
    label1_encrypted_image = tk.Label(
        image=image_Encypted,
    )
    label1_encrypted_image.image = image_Encypted
    label1_encrypted_image.place(x=915, y=585)
    lb2.place(x=943, y=540)
    lb2.config(
        text="SUCCESSFUL",
        foreground="green",
        font=cbt,
        bg=sg.cget("bg"),
    )
    B2.configure(state="normal", fg_color="#1f6aa5", text_color="white")


def helloCallBack2():
    global C3, lb3, img2, cvr_file_path, ssim_txt, psnr_txt, output_folder, label1_stego_image, loading_animation, key_name, steg_folder_path

    # Prompt user to select a folder to save the stego image
    steg_folder_path = filedialog.askdirectory(
        title="Select Folder to Save Stego Image"
    )
    if not steg_folder_path:
        print("No folder selected. Exiting.")
        return

    # Show loading animation
    loading_animation = tk.Label(
        sg, text="Loading...", font=("Arial", 15), bg=sg.cget("bg"), fg="green"
    )
    loading_animation.place(x=1415, y=620)
    sg.update_idletasks()

    # Path to the file to embed in the image
    path = os.path.join(script_dir, "image", "gui_trail.txt")

    # Embed data in the image and save the stego image in the selected folder
    try:
        embd.hide_data_in_image(sg, path, cvr_file_path, steg_folder_path, key_name)

        # Update GUI elements
        C3.state(["selected"])

        # Display the stego image
        steg_image_path = os.path.join(steg_folder_path, embd.name())
        img2 = Image.open(steg_image_path)
        img2 = img2.resize((200, 200))
        img2 = ImageTk.PhotoImage(img2)
        label1_stego_image = tk.Label(image=img2)
        label1_stego_image.image = img2
        label1_stego_image.place(x=1354, y=585)
        lb3.place(x=1380, y=540)
        lb3.config(
            text="SUCCESSFUL",
            foreground="green",
            font=cbt,
            bg=sg.cget("bg"),
        )

        # Calculate SSIM and PSNR indices
        ssim = pm.ssim_indx(cvr_file_path, steg_image_path)
        ssim_txt.insert(0, ssim)
        psnr = pm.psnr_indx(cvr_file_path, steg_image_path)
        psnr_txt.insert(0, psnr)
        loading_animation.place_forget()

    except ValueError as ve:
        # Handle the case where embedding failed due to insufficient capacity
        print("Embedding failed:", ve)
        loading_animation.place_forget()
        loading_animation = tk.Label(
            sg, text="Failed!", font=("Arial", 15), bg=sg.cget("bg"), fg="red"
        )
        loading_animation.place(x=1420, y=620)


def back():
    sg.destroy()
    import GUI


fst = tkFont.Font(family="Helvetica", size=16)


def copy():
    global textbox
    txt = textbox.get()
    pyperclip.copy(txt)


options_frame = customtkinter.CTkFrame(sg, width=200, height=200)
options_frame.place(x=45, y=150)


checkbox_var = tk.BooleanVar(value=False)


# Function to handle check box state change
def checkbox_state_changed():
    if checkbox_var.get():
        # If the check box is selected, enable the radio buttons
        radiobutton_1.configure(state="normal")
        radiobutton_2.configure(state="normal")
        radiobutton_3.configure(state="normal")
        radiobutton_4.configure(state="normal")
        radiobutton_5.configure(state="normal")
    else:
        # If the check box is deselected, disable the radio buttons
        radiobutton_1.configure(state="disabled")
        radiobutton_2.configure(state="disabled")
        radiobutton_3.configure(state="disabled")
        radiobutton_4.configure(state="disabled")
        radiobutton_5.configure(state="disabled")
        # Set the default value of radio_var to 0 if checkbox is unchecked
        radio_var.set(0)


checkbox_1 = customtkinter.CTkCheckBox(
    options_frame,
    text="Auto Destructable",
    variable=checkbox_var,
    command=checkbox_state_changed,
)
checkbox_1.grid(row=0, column=0, padx=10, pady=10)


def radiobutton_event():
    print("Radiobutton toggled, current value:", radio_var.get())


radio_var = tk.IntVar(value=0)

radiobutton_1 = customtkinter.CTkRadioButton(
    options_frame,
    text="1 M",
    command=radiobutton_event,
    variable=radio_var,
    state="disabled",
    value=1,
)
radiobutton_1.grid(row=1, column=0, pady=10)

radiobutton_2 = customtkinter.CTkRadioButton(
    options_frame,
    text="2 M",
    command=radiobutton_event,
    variable=radio_var,
    state="disabled",
    value=2,
)
radiobutton_2.grid(row=2, column=0, pady=10)
radiobutton_3 = customtkinter.CTkRadioButton(
    options_frame,
    text="3 M",
    command=radiobutton_event,
    variable=radio_var,
    state="disabled",
    value=3,
)
radiobutton_3.grid(row=3, column=0, pady=10)
radiobutton_4 = customtkinter.CTkRadioButton(
    options_frame,
    text="5 M",
    command=radiobutton_event,
    variable=radio_var,
    state="disabled",
    value=5,
)
radiobutton_4.grid(row=4, column=0, pady=10)
radiobutton_5 = customtkinter.CTkRadioButton(
    options_frame,
    text="9 M",
    command=radiobutton_event,
    variable=radio_var,
    state="disabled",
    value=9,
)
radiobutton_5.grid(row=5, column=0, pady=10)


lbl = Label(sg)
lb2 = tk.Label(sg, text="")
lb3 = tk.Label(sg, text="")
compress = tk.Label(
    sg,
    text="Compress Image(DWT) ",
    font=fst,
    borderwidth=0,
    relief="solid",
    # bg="grey",
    bg=sg.cget("bg"),
    fg="white",
)
compress.place(x=524, y=430)
C1 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C1.place(x=490, y=432)
B = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B.place(x=429, y=390)

encrypt = tk.Label(
    sg,
    text="Encryption(AES) ",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
encrypt.place(x=948, y=430)
C2 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C2.place(x=909, y=432)
B1 = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack1,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B1.place(x=744, y=390)

embed = tk.Label(
    sg,
    text="Steganography(LSB) ",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
embed.place(x=1370, y=430)
C3 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C3.place(x=1335, y=432)
B2 = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack2,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B2.place(x=1095, y=390)

sg.style = ttk.Style()
sg.style.configure(
    "Custom.TFrame",
    background="#2b2b2b",
    borderwidth=6,
    relief="solid",
    highlightbackground="#2b2b2b",
    highlightthickness=3,
)


border_frame = customtkinter.CTkFrame(sg, width=200, height=150)
border_frame.place(x=400, y=150)

frame = ttk.Frame(border_frame, style="Inner.TFrame")
frame.place(x=3, y=3)


user_name = Label(
    frame,
    font=fst,
    text="Secret Image",
    borderwidth=0,
    bg=sg.cget("bg"),
    fg="white",
)
user_name.grid(row=0, column=0, padx=58, pady=35)

fbt = customtkinter.CTkButton(
    master=sg, text="Open File", command=get_file_path, width=95
)
fbt.place(x=453, y=230)

sg.style = ttk.Style()
sg.style.configure("Border.TFrame", background="#2b2b2b")
sg.style.configure("Inner.TFrame", background="#2b2b2b")


border_frame1 = customtkinter.CTkFrame(sg, width=200, height=150)
border_frame1.place(x=718, y=150)

frame = ttk.Frame(border_frame1, style="Inner.TFrame")
frame.place(x=3, y=3)

# Label for "Cover-Image" inside the frame
cover_name = Label(
    frame,
    font=fst,
    text="Cover Image",
    borderwidth=0,
    bg=sg.cget("bg"),
    fg="white",
)
cover_name.grid(row=0, column=0, padx=58, pady=35)

# Button for "Open File" inside the frame
fbt = customtkinter.CTkButton(
    master=sg,
    text="Open File",
    command=get_file_path1,
    state="disabled",
    width=95,
    text_color="red",
    fg_color="#d3d3d3",
    cursor="cross",
)
fbt.place(x=771, y=230)


sg.style = ttk.Style()
sg.style.configure("Border.TFrame", background="#2b2b2b")
sg.style.configure("Inner.TFrame", background="#2b2b2b")


# Create a frame to act as a border
border_frame3 = customtkinter.CTkFrame(sg, width=200, height=150)
border_frame3.place(x=1065, y=150)

# Create the main frame inside the border frame
frame = ttk.Frame(border_frame3, style="Inner.TFrame")
frame.place(x=3, y=3)

# Label for "Password" inside the frame
ktxt = Label(
    frame,
    text="Password",
    font=fst,
    borderwidth=0,
    bg=sg.cget("bg"),
    fg="white",
)
ktxt.grid(row=0, column=0, padx=70, pady=35)


textbox = customtkinter.CTkEntry(sg, placeholder_text="")
textbox.place(x=1095, y=215)


sbmt = customtkinter.CTkButton(
    master=sg,
    text="Submit",
    command=submit,
    state="disabled",
    width=100,
    text_color="red",
    fg_color="#d3d3d3",
)
sbmt.place(x=1115, y=255)


sg.style = ttk.Style()
sg.style.configure("Border.TFrame", background="#2b2b2b")
sg.style.configure("Inner.TFrame", background="#2b2b2b")


metrics = tk.Label(
    sg,
    text="Performance Metrics",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
metrics.place(x=930, y=850)

psnr = tk.Label(
    sg,
    text="PSNR",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
psnr.place(x=520, y=932)
psnr_txt = customtkinter.CTkEntry(sg, placeholder_text="", width=200)
psnr_txt.place(x=467, y=743)

ssim = tk.Label(
    sg,
    text="SSIM",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
ssim.place(x=1249, y=932)
ssim_txt = customtkinter.CTkEntry(sg, placeholder_text="", width=200)
ssim_txt.place(x=1051, y=743)

file_path = ""
cvr_file_path = ""
key = ""


label1_encrypted_image = None
label1_stego_image = None
label1_comp_image = None
loading_animation = None


def reset():
    global file_path, cvr_file_path, key, label1_comp_image, label1_encrypted_image, label1_stego_image, lb3, loading_animation

    # Reset global variables
    file_path = ""
    cvr_file_path = ""
    key = ""

    if tick_label_cover:
        tick_label_cover.place_forget()
    if tick_label_user:
        tick_label_user.place_forget()

    if label1_comp_image:
        label1_comp_image.place_forget()
        lbl.place_forget()

    if label1_encrypted_image:
        label1_encrypted_image.place_forget()
        lb2.place_forget()

    if label1_stego_image:
        label1_stego_image.place_forget()
        lb3.place_forget()

    if loading_animation:
        loading_animation.place_forget()

    B.configure(state="disabled", text_color="red", fg_color="#d3d3d3")
    B1.configure(state="disabled", text_color="red", fg_color="#d3d3d3")
    B2.configure(state="disabled", text_color="red", fg_color="#d3d3d3")

    textbox.delete(0, tk.END)

    C1.state(["!selected"])
    C2.state(["!selected"])
    C3.state(["!selected"])

    fbt.configure(state="disabled", text_color="red", fg_color="#d3d3d3")
    sbmt.configure(state="disabled", text_color="red", fg_color="#d3d3d3")

    psnr_txt.delete(0, tk.END)
    ssim_txt.delete(0, tk.END)


button_frame = customtkinter.CTkFrame(sg, width=200, height=500)
button_frame.place(x=40, y=700)
frame = ttk.Frame(button_frame, style="Inner.TFrame")
frame.place(x=3, y=3)

reset_btn = customtkinter.CTkButton(master=button_frame, text="RESET", command=reset)
reset_btn.grid(row=0, column=0, padx=5, pady=10)

bck = customtkinter.CTkButton(master=button_frame, text="BACK", command=back)
bck.grid(row=1, column=0, padx=5, pady=10)


sg.configure()
sg.mainloop()
