@echo off

set /p rawFolderLoc="Enter the fully qualified location on disk where the uncropped memes will be stored, use double backslashes like '\\' for folder separators': "
rem rem
set /p croppedFolderLoc="Enter the fully qualified location on disk where you would like the cropped memes will be stored, use double backslashes like '\\' for folder separators': "
rem rem
set /p pythonLoc="Enter the fully qualified location on disk where your python 3 .exe file is located, use SINGLE backslashes like '\' for folder separators': "
rem rem
rem echo %~dp0
echo driveLocation = ^"%rawFolderLoc%^"> config.py
echo croppedLocation = ^"%croppedFolderLoc%^">> config.py
echo templateLocation = ^"%~dp0^">> config.py

echo ^"%pythonLoc%^"^ ^"%~dp0^cropTheGoddamnMemes.py^"> cropmemes.bat
echo Alright, we're in business.
pause
