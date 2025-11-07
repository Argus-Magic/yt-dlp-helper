::[Bat To Exe Converter]
::
::YAwzoRdxOk+EWAjk
::fBw5plQjdCyDJGyX8VAjFBdRQwqLAES0A5EO4f7+086IoVgQUewrd5zn6rGcM+8d60nbRYQi3H9ZjNgwLxRcdxysUT8mpmRHtXCWC+GOtgqsfUGF6gYVA2BmhGrDiTgHedx9jtYB1h+480H7mrcv13HzW5ZfRTC5mOJhO8Zg
::YAwzuBVtJxjWCl3EqQJgSA==
::ZR4luwNxJguZRRnk
::Yhs/ulQjdF+5
::cxAkpRVqdFKZSDk=
::cBs/ulQjdF+5
::ZR41oxFsdFKZSDk=
::eBoioBt6dFKZSDk=
::cRo6pxp7LAbNWATEpCI=
::egkzugNsPRvcWATEpCI=
::dAsiuh18IRvcCxnZtBJQ
::cRYluBh/LU+EWAnk
::YxY4rhs+aU+JeA==
::cxY6rQJ7JhzQF1fEqQJQ
::ZQ05rAF9IBncCkqN+0xwdVs0
::ZQ05rAF9IAHYFVzEqQJQ
::eg0/rx1wNQPfEVWB+kM9LVsJDGQ=
::fBEirQZwNQPfEVWB+kM9LVsJDGQ=
::cRolqwZ3JBvQF1fEqQJQ
::dhA7uBVwLU+EWDk=
::YQ03rBFzNR3SWATElA==
::dhAmsQZ3MwfNWATElA==
::ZQ0/vhVqMQ3MEVWAtB9wSA==
::Zg8zqx1/OA3MEVWAtB9wSA==
::dhA7pRFwIByZRRnk
::Zh4grVQjdCyDJGyX8VAjFBdRQwqLAES0A5EO4f7+086IoVgQUewrd5zn6rGcM+8d60nbRYQi3H9ZjNgwLxRcdxysUT8mpmRHtXCWC+GOtgqsfUGF6gYVA2BmhGrDiTgHWdx9jtYB1m2a81rxk6oR1X3tEKwWEAM=
::YB416Ek+ZG8=
::
::
::978f952a14a936cc963da21a135fa983
@echo off
setlocal enabledelayedexpansion

echo Download YouTube audio?
echo [y/n]
set /p "input=> "
if /i not "%input%"=="y" goto last

:while
cls
echo Enter Link:
set /p "link=> "
if "%link%"=="" (
    echo No link entered. Try again.
    timeout /t 2 >nul
    goto while
)

yt-dlp -x --audio-format mp3 --audio-quality 0 ^
  -o "C:\Users\leoni\OneDrive\Leo_Sn\Music\Downloaded-Music\%%(title)s.%%(ext)s" "%link%"

echo.
echo Done!
echo Another link?
echo [y/n]
set /p "again=> "
if /i "%again%"=="y" goto while

:last
echo Open download directory?
echo [y/n]
set /p "ofile=> "
if /i not "%ofile%"=="y" (
    echo Exiting...
    timeout /t 2 /nobreak >nul
    exit /b
)

echo Opening file explorer...
start "" explorer "C:\Users\leoni\OneDrive\Leo_Sn\Music\Downloaded-Music\"
timeout /t 1 /nobreak >nul
echo Bye!
timeout /t 1 /nobreak >nul
exit /b
