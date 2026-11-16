@echo off
setlocal
cd /d "%~dp0"
title Livewave - Live TV
where py.exe >nul 2>nul
if not errorlevel 1 (
  py.exe -3 "%~dp0launch.py"
  goto finished
)
where python.exe >nul 2>nul
if not errorlevel 1 (
  python.exe "%~dp0launch.py"
  goto finished
)
echo Python 3 was not found. Install Python 3 and try again.
echo Download: https://www.python.org/downloads/windows/
:finished
echo.
pause
endlocal
