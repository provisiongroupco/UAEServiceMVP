#!/bin/bash

echo "Setting up Halton KSA Service Reports MVP..."
echo ""

# Check if Python 3.12 is installed
if command -v python3.12 &> /dev/null; then
    PYTHON_CMD="python3.12"
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    echo "Warning: Python 3.12 not found, using default python3"
else
    echo "Error: Python 3 is not installed. Please install Python 3.12."
    exit 1
fi

echo "Python found: $($PYTHON_CMD --version)"
echo ""

# Remove existing virtual environment if it exists
if [ -d "venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf venv
fi

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON_CMD -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo ""
echo "Setup complete! To run the application:"
echo "1. Run: ./run.sh"
echo "   OR"
echo "2. Activate the virtual environment: source venv/bin/activate"
echo "3. Run the application: streamlit run app.py"
echo ""
echo "The application will open in your default browser."