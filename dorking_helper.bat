@echo off
:: GitHub Dorking Helper Script for Windows

setlocal enabledelayedexpansion

echo GitHub Dorking Helper
echo ====================
echo.

if not exist "GitHub Dorking.txt" (
    echo Error: GitHub Dorking.txt file not found!
    echo Please ensure you're running this script from the correct directory.
    pause
    exit /b 1
)

echo Select an option:
echo 1. List all dorks
echo 2. Search for dorks containing a keyword
echo 3. Show dork categories
echo 4. Count total dorks
echo 5. Open GitHub Dorking.txt in notepad
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" (
    echo.
    echo All GitHub Dorking Patterns:
    echo ==========================
    type "GitHub Dorking.txt"
) else if "%choice%"=="2" (
    set /p keyword="Enter keyword to search for: "
    echo.
    echo Dorks containing "%keyword%":
    echo ========================
    findstr /i "%keyword%" "GitHub Dorking.txt"
) else if "%choice%"=="3" (
    echo.
    echo Dork Categories:
    echo ===============
    echo API Keys and Secrets
    echo Authentication Credentials
    echo Configuration Files
    echo Database Connections
    echo Cloud Services
    echo Communication Services
    echo Development Tools
    echo Financial Services
    echo Social Media
    echo File Types
    echo Filename Based
    echo Path Based
    echo Content Based
    echo Framework Specific
) else if "%choice%"=="4" (
    echo.
    echo Counting dorks...
    for /f %%i in ('type "GitHub Dorking.txt" ^| find /c /v ""') do set count=%%i
    echo Total dorks: !count!
) else if "%choice%"=="5" (
    notepad "GitHub Dorking.txt"
) else (
    echo Invalid choice. Please run the script again and select 1-5.
)

echo.
pause