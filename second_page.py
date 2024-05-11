import tkinter as tk
from tkinter import ttk
import os
from tkinter import *
from tkinter import messagebox
import Decompression_DWT as dcd
import AES_Hash_Decryption as dt
import stegno_decoded as decod
from tkinter import filedialog
import tkinter.font as tkFont
import time
import txtimage as txim
import stegano
import base64
import subprocess
from stegano import lsb
import pickle
from PIL import Image, ImageTk
import customtkinter
from CTkMessagebox import CTkMessagebox

sg = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
width = sg.winfo_screenwidth()
height = sg.winfo_screenheight()
window_width = int(1.02 * width)
window_height = int(1.02 * height)
# Set the window geometry to be centered and with margin
x_offset = (width - window_width) // 2
y_offset = (height - window_height) // 2
sg.geometry(f"{window_width}x{window_height}+{x_offset}+{y_offset}")
sg.configure(bg="#242424")
sg.title("Detecting")
script_dir = os.path.dirname(__file__)
tick=os.path.join(script_dir,"green_tick.png")
tick_image = Image.open(tick)
tick_image = tick_image.resize((20, 20))
tick_image = ImageTk.PhotoImage(tick_image)
style = ttk.Style()
style.configure("Custom.TCheckbutton", relief="solid", background=sg.cget("bg"))

tfn = ("Helvetica", 30, "bold")
title = Label(
    sg,
    text="Image Decryption",
    justify="center",
    font=tfn,
    bg=sg.cget("bg"),
    fg="white",
)
title.place(x=860, y=25)


def get_file_path():
    global file_path, tick_label_cover
    file_path = filedialog.askopenfilename(
        title="Select A File",
        filetypes=(
            ("jpg", "*.jpg"),
            ("PNG", "*.png"),
            ("mov files", "*.png"),
            ("mp4", "*.mp4"),
            ("wmv", "*.wmv"),
            ("avi", "*.avi"),
        ),
    )
    if file_path:
        tick_label_cover = tk.Label(image=tick_image)
        tick_label_cover.image = tick_image
        tick_label_cover.configure(bg="#2b2b2b")
        tick_label_cover.place(x=764, y=335)
        cpy.configure(state="normal", fg_color="#1f6aa5", text_color="white")


cbt = ("Arial", 16)
f = ("Times bold", 14)


def helloCallBack():
    global C1, lbl, decrypted_img, label1
    loading_animation = tk.Label(
        sg, text="Loading...", font=("Arial", 15), bg=sg.cget("bg"), fg="green"
    )
    loading_animation.place(x=585, y=585)
    sg.update_idletasks()

    decod.extract_data_from_image(file_path, script_dir)
    C1.state(["selected"])
    txim.txt_to_image()
    decrypted_img_path = os.path.join(script_dir, "image", "detect_aes.jpg")
    decrypted_img = Image.open(decrypted_img_path)
    decrypted_img = decrypted_img.resize((200, 200))
    decrypted_img = ImageTk.PhotoImage(decrypted_img)
    label1 = tk.Label(image=decrypted_img)
    label1.image = decrypted_img
    label1.place(x=519, y=593)
    lbl.place(x=546, y=555)
    lbl.config(
        text="SUCCESSFUL",
        foreground="green",
        font=cbt,
        bg=sg.cget("bg"),
    )
    B1.configure(state="normal", fg_color="#1f6aa5", text_color="white")
    loading_animation.place_forget()


def helloCallBack1():
    global C2, lb2, key, aesimg, label2, decryp_image_path, save_folder_path

    # Ask the user to select the folder to save the decrypted image
    save_folder_path = filedialog.askdirectory(
        title="Select Folder to Save Decrypted Image"
    )

    # Check if the user selected a folder
    if not save_folder_path:
        print("No folder selected. Exiting.")
        return

    # Decrypt the image and save it in the selected folder
    dt.decrypt(decoded_password, save_folder_path, script_dir)

    # Update UI elements
    C2.state(["selected"])
    decryp_image_path = os.path.join(save_folder_path, "nonsteg11_33_59decry.png")
    aesimg = Image.open(decryp_image_path)
    aesimg = aesimg.resize((200, 200))
    aesimg = ImageTk.PhotoImage(aesimg)
    label2 = tk.Label(image=aesimg)
    label2.image = aesimg
    label2.place(x=947, y=593)
    lb2.place(x=977, y=555)
    lb2.config(
        text="SUCCESSFUL",
        foreground="green",
        font=cbt,
        bg=sg.cget("bg"),
    )
    B2.configure(state="normal", fg_color="#1f6aa5", text_color="white")


def create_delete_image_batch():
    # Set the path to the batch file
    image = decomp_image_path
    image1 = decryp_image_path
    directory_name, file_name = os.path.split(file_path)
    full_file_path = os.path.join(directory_name, file_name)
    print(full_file_path)
    image2 = full_file_path
    batch_file_path = os.path.join(save_folder_path, "delete_image.bat")

    batch_content = f"""@echo off

    REM Set the path to the image file
    set "IMAGE_PATH={image}"

    REM Set the path to the image file
    set "IMAGE_PATH1={image1}"

    REM Set the path to the image file
    set "IMAGE_PATH2={image2}"

    REM Wait for  seconds silently
    timeout /t {waiting_time} /nobreak >nul

    REM Delete the image file silently
    del "%IMAGE_PATH%" >nul 2>&1

    REM Delete the image file silently
    del "%IMAGE_PATH1%" >nul 2>&1

    REM Delete the image file silently
    del "%IMAGE_PATH2%" >nul 2>&1

    REM Remove the hidden attribute from the batch file
    attrib -h "{batch_file_path}" >nul 2>&1

    REM Delete the batch file itself
    del "{batch_file_path}" >nul 2>&1
    """

    with open(batch_file_path, "w") as batch_file:
        batch_file.write(batch_content)

    subprocess.Popen(["attrib", "+h", batch_file_path], shell=True)

    # Execute the batch file silently
    subprocess.Popen([batch_file_path], shell=True)

            # attrib -h "{batch_file_path}" >nul 2>&1
            # del "{batch_file_path}" >nul 2>&1

def helloCallBack2():
    global decomp_image_path, waiting_time, label3
    otpath1 = save_folder_path
    dcd.Decompression_Process(decryp_image_path, otpath1)
    # time.sleep(1)
    C3.state(["selected"])
    decomp_image_path = os.path.join(save_folder_path, "decompressed.jpg")
    decomp = Image.open(decomp_image_path)
    decomp = decomp.resize((200, 200))
    decomp = ImageTk.PhotoImage(decomp)
    label3 = tk.Label(image=decomp)
    label3.image = decomp
    label3.place(x=1375, y=593)
    lb3.place(x=1400, y=555)
    lb3.config(
        text="SUCCESSFUL",
        foreground="green",
        font=cbt,
        bg=sg.cget("bg"),
    )

    waiting_time = int(last_digit) * 60 if last_digit.isdigit() else 0

    if waiting_time > 0:
        print("bat file created")
        messagebox = CTkMessagebox(
            title="warning",
            message=f"The Image Will Delete in {last_digit} Minute",
            icon="warning",
            justify="center",
        )
        x_offset = (sg.winfo_width() - messagebox.winfo_width()) // 2
        y_offset = (sg.winfo_height() - messagebox.winfo_height()) // 2
        messagebox.geometry(f"+{sg.winfo_x() + x_offset}+{sg.winfo_y() + y_offset}")
        messagebox.wait_window()
        create_delete_image_batch()
    else:
        print("it only print the image")
        messagebox = CTkMessagebox(
            title="Attention",
            message="Please Rename the Decrypted Image For Safety Purpose",
            icon="info",
            justify="center",
        )
        x_offset = (sg.winfo_width() - messagebox.winfo_width()) // 2
        y_offset = (sg.winfo_height() - messagebox.winfo_height()) // 2
        messagebox.geometry(f"+{sg.winfo_x() + x_offset}+{sg.winfo_y() + y_offset}")
        messagebox.wait_window()
        pass


fst = tkFont.Font(family="Helvetica", size=16)


def get_key():
    global key, file_path
    key = textbox.get()
    password_try = decode_and_extract_password(file_path)

    title = "Error"
    message = ""
    icon = "cancel"

    if password_try is not None:
        if password_try == key:
            B.configure(state="normal", fg_color="#1f6aa5", text_color="white")
            return
        else:
            message = "Wrong Password!"
            icon = "cancel"
    else:
        message = "No Password Found!"
        icon = "warning"

    messagebox = CTkMessagebox(
        title=title,
        message=message,
        icon=icon,
        justify="center",
    )
    # Calculate the center coordinates relative to the main window
    x_offset = (sg.winfo_width() - messagebox.winfo_width()) // 2
    y_offset = (sg.winfo_height() - messagebox.winfo_height()) // 2
    messagebox.geometry(f"+{sg.winfo_x() + x_offset}+{sg.winfo_y() + y_offset}")
    messagebox.wait_window()


def decode_and_extract_password(image_path):
    global last_digit, decoded_password
    image_name = os.path.basename(image_path)
    parts = image_name.split("_")
    if len(parts) < 2:
        return None
    encoded_password_with_extension = parts[-1]
    encoded_password = encoded_password_with_extension.split(".")[0]
    decoded_password = base64.b64decode(encoded_password.encode()).decode()
    # Remove the last character from decoded_password
    last_digit = decoded_password[-1] if decoded_password else None
    decoded_password1 = decoded_password[:-1] if decoded_password else None
    print(last_digit)
    return decoded_password1


lbl = Label(sg)
lb2 = tk.Label(sg, text="")
lb3 = tk.Label(sg, text="")


compress = tk.Label(
    sg,
    text="Stegnography Decoding ",
    font=fst,
    borderwidth=0,
    relief="solid",
    # bg="grey",
    bg=sg.cget("bg"),
    fg="white",
)
compress.place(x=520, y=440)
C1 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C1.place(x=491, y=444)
B = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B.place(x=430, y=390)

encrypt = tk.Label(
    sg,
    text="Decryption(AES) ",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
encrypt.place(x=965, y=440)
C2 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C2.place(x=934, y=444)
B1 = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack1,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B1.place(x=766, y=390)

embed = tk.Label(
    sg,
    text="Decompression(DWT) ",
    font=fst,
    borderwidth=0,
    relief="solid",
    bg=sg.cget("bg"),
    fg="white",
)
embed.place(x=1370, y=440)
C3 = ttk.Checkbutton(sg, style="Custom.TCheckbutton")
C3.place(x=1342, y=444)
B2 = customtkinter.CTkButton(
    master=sg,
    text="Click",
    command=helloCallBack2,
    state="disabled",
    text_color="red",
    fg_color="#d3d3d3",
)
B2.place(x=1111, y=390)


border_frame = customtkinter.CTkFrame(sg, width=200, height=150)
border_frame.place(x=520, y=150)

frame = ttk.Frame(border_frame, style="Inner.TFrame")
frame.place(x=3, y=3)


user_name = Label(
    frame,
    font=fst,
    text="Image Path",
    borderwidth=0,
    bg="#2b2b2b",
    fg="white",
)
user_name.grid(row=0, column=0, padx=66, pady=35)

fbt = customtkinter.CTkButton(
    master=sg, text="Open File", command=get_file_path, width=95
)
fbt.place(x=573, y=230)

sg.style = ttk.Style()
sg.style.configure("Border.TFrame", background="#2b2b2b")
sg.style.configure("Inner.TFrame", background="#2b2b2b")


border_frame3 = customtkinter.CTkFrame(sg, width=190, height=150)
border_frame3.place(x=955, y=150)

# Create the main frame inside the border frame
frame = ttk.Frame(border_frame3, style="Inner.TFrame")
frame.place(x=3, y=3)

# Label for "Password" inside the frame
klbl = Label(
    frame,
    text="Password",
    font=fst,
    borderwidth=0,
    bg="#2b2b2b",
    fg="white",
)
klbl.grid(row=0, column=0, padx=64, pady=35)


textbox = customtkinter.CTkEntry(sg, placeholder_text="")
textbox.place(x=981, y=215)


cpy = customtkinter.CTkButton(
    master=sg,
    text="Submit",
    command=get_key,
    state="disabled",
    width=100,
    text_color="red",
    fg_color="#d3d3d3",
)
cpy.place(x=1003, y=255)


sg.style = ttk.Style()
sg.style.configure("Border.TFrame", background="#2b2b2b")
sg.style.configure("Inner.TFrame", background="#2b2b2b")


label1 = None
label2 = None
label3 = None
tick_label_cover = None
loading_animation = None


def reset():
    global file_path, key, label1, label2, label3, lbl, lb2, lb3, loading_animation

    # Reset global variables
    file_path = ""
    key = ""

    if tick_label_cover:
        tick_label_cover.place_forget()

    if label1:
        label1.place_forget()
        lbl.place_forget()

    if label2:
        label2.place_forget()
        lb2.place_forget()

    if label3:
        label3.place_forget()
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

    cpy.configure(state="disabled", text_color="red", fg_color="#d3d3d3")


def back():
    sg.destroy()
    import GUI

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
