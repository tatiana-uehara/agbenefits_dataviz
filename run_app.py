#!/usr/bin/env python3
"""
Launcher script for the Soil Classification Streamlit App
"""
import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required packages"""
    requirements_file = Path(__file__).parent / "requirements.txt"
    minimal_requirements = Path(__file__).parent / "requirements_minimal.txt"
    
    try:
        if requirements_file.exists():
            print("Installing requirements from requirements.txt...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(requirements_file)])
        elif minimal_requirements.exists():
            print("Installing minimal requirements...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(minimal_requirements)])
        else:
            print("Requirements files not found. Installing basic packages...")
            packages = ["streamlit", "pandas", "plotly", "openpyxl", "reportlab", "Pillow"]
            for package in packages:
                print(f"Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except subprocess.CalledProcessError as e:
        print(f"Error installing requirements: {e}")
        print("Trying to install packages individually...")
        packages = ["streamlit", "pandas", "plotly", "openpyxl", "reportlab", "Pillow"]
        for package in packages:
            try:
                print(f"Installing {package}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}, continuing...")

def run_streamlit():
    """Run the Streamlit app"""
    app_file = Path(__file__).parent / "streamlit_soil_report.py"
    if not app_file.exists():
        print(f"Error: {app_file} not found!")
        sys.exit(1)
    
    print("Starting Streamlit app...")
    os.system(f"streamlit run {app_file}")

if __name__ == "__main__":
    print("🌱 Soil Classification Report Generator")
    print("=" * 50)
    
    try:
        # Check if requirements are met, install if needed
        try:
            import streamlit
            import pandas
            import plotly
            import reportlab
        except ImportError:
            print("Missing dependencies. Installing...")
            install_requirements()
        
        # Run the app
        run_streamlit()
        
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
