@echo off
setlocal
cd /d "%~dp0"
title Livewave - TV and Mobile Server
echo Livewave local network server
 echo.
echo Keep this window open while watching on your TV or phone.
echo In the TV or phone browser open: http://PC-IP-ADDRESS:8765
 echo.
where py.exe >nul 2>nul
if not errorlevel 1 (
  py.exe -3 -m http.server 8765 --bind 0.0.0.0 --directory "%~dp0"
  goto finished
)
where python.exe >nul 2>nul
if not errorlevel 1 (
  python.exe -m http.server 8765 --bind 0.0.0.0 --directory "%~dp0"
  goto finished
)
echo Python 3 was not found. Install Python 3 and try again.
echo Download: https://www.python.org/downloads/windows/
:finished
echo.
pause
endlocal
