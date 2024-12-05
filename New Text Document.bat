@echo off
REM Get the directory where the script is located
set "CURRENT_DIR=%~dp0"

REM Add the current directory to PATH
echo Adding %CURRENT_DIR% to PATH...
setx PATH "%CURRENT_DIR%;%PATH%" /M

REM Add the current directory to PYTHONPATH
echo Adding %CURRENT_DIR% to PYTHONPATH...
setx PYTHONPATH "%CURRENT_DIR%;%PYTHONPATH%" /M

echo Done! You may need to restart your terminal for changes to take effect.
pause