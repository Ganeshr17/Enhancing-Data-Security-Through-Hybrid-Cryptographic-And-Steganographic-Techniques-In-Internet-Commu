from PIL import Image
import numpy as np
import os
import base64
import customtkinter
from CTkMessagebox import CTkMessagebox


def name():
    return new_name


# Function to convert binary to decimal
def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal


# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return "0" * (8 - len(binary)) + binary


def attach_password_to_image_name(image_path, password):
    # Encode the password using Base64
    # Encode the password using Base64
    encoded_password = base64.b64encode(password.encode()).decode()

    # Get the filename from the image path without the extension
    image_name, extension = os.path.splitext(os.path.basename(image_path))

    # Concatenate the encoded password with the image name using a hyphen as delimiter
    image_name_with_password = f"{image_name}_{encoded_password}{extension}"
    return image_name_with_password


# Modify the hide_data_in_image() function in embd.py to accept an output folder
def hide_data_in_image(sg,file_path, image_path, output_folder, password):
    # Load image
    global new_name
    image = Image.open(image_path)
    pixels = np.array(image)

    # Read binary data from file
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Convert binary data to binary string
    binary_string = "".join(format(byte, "08b") for byte in binary_data)

    # Check if image has enough capacity to hide binary data
    if len(binary_string) > pixels.size:
        messagebox=CTkMessagebox(
            title="warning",
            message="Image does not have enough capacity to hide all binary data. select the high quality cover image",
            icon="warning",
            justify="center",
        )
        x_offset = (sg.winfo_width() - messagebox.winfo_width()) // 2
        y_offset = (sg.winfo_height() - messagebox.winfo_height()) // 2
        messagebox.geometry(f"+{sg.winfo_x() + x_offset}+{sg.winfo_y() + y_offset}")
        messagebox.wait_window()
        raise ValueError("Image does not have enough capacity to hide all binary data.")

    binary_index = 0
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(pixels.shape[2]):
                if binary_index < len(binary_string):
                    pixel = pixels[i][j][k]
                    pixel_binary = format(pixel, "08b")
                    pixel_binary = pixel_binary[:-1] + binary_string[binary_index]
                    pixels[i][j][k] = int(pixel_binary, 2)
                    binary_index += 1

    # Save the modified image to output folder
    filename = os.path.basename(file_path)
    output_path = os.path.join(output_folder, filename.replace(".txt", "_steg.png"))
    output_path = output_path.replace("\\", "/")
    output_path = output_path.replace(".jpg", ".png")
    new_name = attach_password_to_image_name(output_path, password)
    final_path = os.path.join(output_folder, new_name)

    try:
        modified_image = Image.fromarray(pixels)
        modified_image.save(final_path)
        print("Successful")
    except Exception as e:
        print("Error:", e)
        return None
    print(final_path)
    return final_path
