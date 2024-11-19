@echo off
REM Download Python 3.11 installer
echo Downloading Python 3.11 installer...
curl -o python-3.11.exe https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe

REM Install Python 3.11 silently
echo Installing Python 3.11...
start /wait python-3.11.exe /quiet InstallAllUsers=1 PrependPath=1

REM Verify Python installation
python --version
if %errorlevel% neq 0 (
    echo Python installation failed.
    exit /b 1
)

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install requests package
echo Installing requests package...
pip install requests

REM Install tkinter package
echo Installing tkinter package...
pip install tk

echo Installation completed.
pause