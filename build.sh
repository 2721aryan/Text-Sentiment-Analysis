#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Download NLTK data
python download_nltk.py

# Create directory for Flask sessions
mkdir -p flask_session 