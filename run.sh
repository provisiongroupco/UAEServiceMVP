#!/bin/bash

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Please run setup.sh first."
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Run the Streamlit app
echo "Starting Halton KSA Service Reports application..."
echo "Using virtual environment at: $(which python)"
streamlit run app.py