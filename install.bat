@echo off
echo Installing required packages...
echo.

pip install requests
if %errorlevel% neq 0 (
    echo Failed to install requests
    pause
    exit /b 1
)

pip install Pillow
if %errorlevel% neq 0 (
    echo Failed to install Pillow
    pause
    exit /b 1
)

pip install pyperclip
if %errorlevel% neq 0 (
    echo Failed to install pyperclip
    pause
    exit /b 1
)

pip install pywin32
if %errorlevel% neq 0 (
    echo Failed to install pywin32
    pause
    exit /b 1
)

pip install pycryptodome
if %errorlevel% neq 0 (
    echo Failed to install pycryptodome
    pause
    exit /b 1
)

pip install websocket-client
if %errorlevel% neq 0 (
    echo Failed to install websocket-client
    pause
    exit /b 1
)

pip install windows
if %errorlevel% neq 0 (
    echo Failed to install windows
    pause
    exit /b 1
)

pip install psutil
if %errorlevel% neq 0 (
    echo Failed to install psutil
    pause
    exit /b 1
)

echo.
echo All packages installed successfully. Ready to run builder.py
pause

