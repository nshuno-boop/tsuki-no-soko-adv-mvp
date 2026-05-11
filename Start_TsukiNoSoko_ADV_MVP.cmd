@echo off
setlocal

set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"
set "RENPY_EXE="

if defined RENPY_EXE_PATH (
    if exist "%RENPY_EXE_PATH%" set "RENPY_EXE=%RENPY_EXE_PATH%"
)

if not defined RENPY_EXE (
    for %%D in (
        "%PROJECT_DIR%\..\..\tools\renpy-8.5.2-sdk"
        "C:\RenPy"
        "C:\renpy"
        "%USERPROFILE%\Downloads"
        "%USERPROFILE%\Documents"
        "%USERPROFILE%\Desktop"
    ) do (
        if not defined RENPY_EXE (
            for /f "delims=" %%F in ('dir /b /s "%%~D\renpy.exe" 2^>nul') do (
                if not defined RENPY_EXE set "RENPY_EXE=%%F"
            )
        )
    )
)

if defined RENPY_EXE (
    echo Starting Ren'Py project...
    echo Project: %PROJECT_DIR%
    echo RenPy: %RENPY_EXE%
    start "" "%RENPY_EXE%" "%PROJECT_DIR%"
    exit /b 0
)

echo Ren'Py executable was not found.
echo.
echo Open the Ren'Py Launcher, then add this project folder:
echo %PROJECT_DIR%
echo.
echo If Ren'Py is installed in a custom folder, set RENPY_EXE_PATH to renpy.exe.
echo Example:
echo setx RENPY_EXE_PATH "C:\renpy-8.3.7-sdk\renpy.exe"
echo.
start "" "%PROJECT_DIR%"
pause
