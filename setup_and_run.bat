@echo off
REM ===================================================================
REM Water Governance Dashboard - Complete Setup Script for Windows
REM ===================================================================
REM This script will:
REM 1. Install all dependencies
REM 2. Verify system setup
REM 3. Generate ML models
REM 4. Launch the dashboard
REM ===================================================================

echo.
echo ========================================================================
echo   Water Governance Dashboard - Complete Setup
echo ========================================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Step 1: Install dependencies
echo ========================================================================
echo Step 1: Installing dependencies...
echo ========================================================================
echo.

pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo ✅ Dependencies installed successfully
echo.

REM Step 2: Verify setup
echo ========================================================================
echo Step 2: Verifying setup...
echo ========================================================================
echo.

python verify_setup.py
if errorlevel 1 (
    echo.
    echo ⚠️  Some checks failed. Please fix the issues above.
    pause
    exit /b 1
)

echo.

REM Step 3: Generate models
echo ========================================================================
echo Step 3: Generating ML models...
echo ========================================================================
echo.

if exist "random_forest.pkl" (
    echo ℹ️  Models already exist, skipping generation...
) else (
    echo Generating new models...
    python generate_models.py
    if errorlevel 1 (
        echo ❌ Failed to generate models
        pause
        exit /b 1
    )
)

echo.
echo ✅ Models ready
echo.

REM Step 4: Launch dashboard
echo ========================================================================
echo Step 4: Launching dashboard...
echo ========================================================================
echo.

echo 🚀 Starting Streamlit application...
echo.
echo    Dashboard will open at: http://localhost:8501
echo    Press Ctrl+C to stop the server
echo.
echo ========================================================================
echo.

timeout /t 2

streamlit run app.py

pause
