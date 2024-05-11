@echo off

REM Set the path to the image file
set "IMAGE_PATH=D:\project\Design Project II\try image\decompressed.jpg"

REM Wait for 10 seconds silently
timeout /t 15 /nobreak >nul

REM Check if the system is shutting down
shutdown /s /t 4 /d p:4:1 /c "Deleting image files before shutdown..." /f /a >nul

REM Delete the image files immediately if shutdown command is detected
if errorlevel 1 (
    del "%IMAGE_PATH%" >nul 2>&1
)
