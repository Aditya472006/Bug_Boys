#!/bin/bash

# ===================================================================
# Water Governance Dashboard - Complete Setup Script for Linux/Mac
# ===================================================================
# This script will:
# 1. Install all dependencies
# 2. Verify system setup
# 3. Generate ML models
# 4. Launch the dashboard
# ===================================================================

echo ""
echo "========================================================================"
echo "  Water Governance Dashboard - Complete Setup"
echo "========================================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ ERROR: Python3 is not installed"
    echo ""
    echo "Please install Python 3.8+ using:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-pip"
    echo "  Mac: brew install python3"
    exit 1
fi

echo "✅ Python found"
python3 --version
echo ""

# Step 1: Install dependencies
echo "========================================================================"
echo "Step 1: Installing dependencies..."
echo "========================================================================"
echo ""

pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""
echo "✅ Dependencies installed successfully"
echo ""

# Step 2: Verify setup
echo "========================================================================"
echo "Step 2: Verifying setup..."
echo "========================================================================"
echo ""

python3 verify_setup.py
if [ $? -ne 0 ]; then
    echo ""
    echo "⚠️  Some checks failed. Please fix the issues above."
    exit 1
fi

echo ""

# Step 3: Generate models
echo "========================================================================"
echo "Step 3: Generating ML models..."
echo "========================================================================"
echo ""

if [ -f "random_forest.pkl" ]; then
    echo "ℹ️  Models already exist, skipping generation..."
else
    echo "Generating new models..."
    python3 generate_models.py
    if [ $? -ne 0 ]; then
        echo "❌ Failed to generate models"
        exit 1
    fi
fi

echo ""
echo "✅ Models ready"
echo ""

# Step 4: Launch dashboard
echo "========================================================================"
echo "Step 4: Launching dashboard..."
echo "========================================================================"
echo ""

echo "🚀 Starting Streamlit application..."
echo ""
echo "    Dashboard will open at: http://localhost:8501"
echo "    Press Ctrl+C to stop the server"
echo ""
echo "========================================================================"
echo ""

sleep 2

streamlit run app.py
