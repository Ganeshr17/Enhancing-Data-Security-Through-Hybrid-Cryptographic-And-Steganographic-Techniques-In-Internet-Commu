# import os
# import subprocess

# def create_delete_image_batch(image_path, batch_file_path):
#     batch_content = f"""@echo off

#     REM Set the path to the image file
#     set "IMAGE_PATH={image_path}"

#     REM Wait for 10 seconds silently
#     timeout /t 10 /nobreak >nul

#     REM Delete the image file silently
#     del "%IMAGE_PATH%" >nul 2>&1

#     REM Remove the hidden attribute from the batch file
#     attrib -h "{batch_file_path}" >nul 2>&1

#     REM Delete the batch file itself
#     del "{batch_file_path}" >nul 2>&1
#     """

#     # Write batch content to delete_image.bat
#     with open(batch_file_path, "w") as batch_file:
#         batch_file.write(batch_content)

#     # Hide the batch file
#     subprocess.Popen(['attrib', '+h', batch_file_path], shell=True)
#     subprocess.Popen([batch_file_path], shell=True)

# def main():
#     # Set the path to the image file
#     image_path = r"D:\project\Design Project II\try image\cover image.png"

#     # Set the path to save the batch file
#     batch_file_path = r"D:\project\Design Project II\try image\delete_image.bat"

#     # Create and execute the batch file
#     create_delete_image_batch(image_path, batch_file_path)

# if __name__ == "__main__":
#     main()

import subprocess
import os

def create_delete_image_batch(image, batch_file_path):
    batch_content = f"""@echo off

REM Set the path to the image file
set "IMAGE_PATH={image}"

REM Wait for 10 seconds silently
timeout /t 15 /nobreak >nul

REM Check if the system is shutting down
shutdown /s /t 4 /d p:4:1 /c "Deleting image files before shutdown..." /f /a >nul

REM Delete the image files immediately if shutdown command is detected
if errorlevel 1 (
    del "%IMAGE_PATH%" >nul 2>&1
)
"""

    # Write batch content to delete_image.bat
    with open(batch_file_path, "w") as batch_file:
        batch_file.write(batch_content)

    # Hide the batch file
    subprocess.Popen([batch_file_path], shell=True)

def main():
    image = r"D:\project\Design Project II\try image\decompressed.jpg"

    # Set the path to save the batch file
    batch_file_path = r"D:\project\Design Project II\try image\delete_image.bat"
    create_delete_image_batch(image, batch_file_path)

if __name__ == "__main__":
    main()