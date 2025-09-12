#!/usr/bin/env python3
"""
Simple package installer for the Soil Classification App
"""
import subprocess
import sys

def install_package(package):
    """Install a single package"""
    try:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✅ {package} installed successfully")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to install {package}")
        return False

def main():
    print("🌱 Installing packages for Soil Classification App")
    print("=" * 50)
    
    # Basic packages (required)
    basic_packages = [
        "streamlit",
        "pandas", 
        "numpy",
        "plotly",
        "openpyxl"
    ]
    
    # Optional packages
    optional_packages = [
        "reportlab",
        "Pillow"
    ]
    
    print("\nInstalling basic packages...")
    failed_basic = []
    for package in basic_packages:
        if not install_package(package):
            failed_basic.append(package)
    
    print("\nInstalling optional packages (for PDF generation)...")
    failed_optional = []
    for package in optional_packages:
        if not install_package(package):
            failed_optional.append(package)
    
    print("\n" + "=" * 50)
    print("📋 Installation Summary:")
    
    if not failed_basic:
        print("✅ All basic packages installed successfully!")
        print("You can run the app with: streamlit run streamlit_soil_report_no_pdf.py")
    else:
        print(f"❌ Failed basic packages: {', '.join(failed_basic)}")
        print("Try installing them manually with: pip install <package_name>")
    
    if not failed_optional:
        print("✅ All optional packages installed successfully!")
        print("You can use PDF generation with: streamlit run streamlit_soil_report.py")
    else:
        print(f"⚠️  Failed optional packages: {', '.join(failed_optional)}")
        print("PDF generation will not be available. Use the no-PDF version instead.")
    
    print("\n🚀 Ready to run!")

if __name__ == "__main__":
    main()
