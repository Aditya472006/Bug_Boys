"""
System Verification Script
Checks all prerequisites and files before running the dashboard

Usage: python verify_setup.py
"""

import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} (need 3.8+)")
        return False

def check_required_packages():
    """Check if all required packages are installed"""
    print("\n📦 Checking required packages...")
    
    required_packages = {
        'streamlit': 'Streamlit',
        'pandas': 'Pandas',
        'numpy': 'NumPy',
        'sklearn': 'Scikit-learn',
        'folium': 'Folium',
        'streamlit_folium': 'Streamlit-Folium'
    }
    
    all_installed = True
    
    for package, name in required_packages.items():
        try:
            __import__(package)
            print(f"   ✅ {name}")
        except ImportError:
            print(f"   ❌ {name} (not installed)")
            all_installed = False
    
    return all_installed

def check_data_files():
    """Check if required data files exist"""
    print("\n📁 Checking data files...")
    
    files_to_check = {
        'dataset.csv': 'Village dataset',
        'app.py': 'Main application',
        'requirements.txt': 'Dependencies file',
        'generate_models.py': 'Model generation script',
    }
    
    all_exist = True
    
    for filename, description in files_to_check.items():
        if os.path.exists(filename):
            file_size = os.path.getsize(filename) / 1024  # KB
            print(f"   ✅ {filename} ({file_size:.1f} KB) - {description}")
        else:
            print(f"   ❌ {filename} - {description} (missing)")
            all_exist = False
    
    return all_exist

def check_model_files():
    """Check if trained model files exist"""
    print("\n🤖 Checking ML model files...")
    
    model_files = {
        'random_forest.pkl': 'Random Forest Model',
        'scaler.pkl': 'Feature Scaler'
    }
    
    all_exist = True
    
    for filename, description in model_files.items():
        if os.path.exists(filename):
            file_size = os.path.getsize(filename) / 1024  # KB
            print(f"   ✅ {filename} ({file_size:.1f} KB) - {description}")
        else:
            print(f"   ⚠️  {filename} - {description} (missing)")
            print(f"      → Run: python generate_models.py")
            all_exist = False
    
    return all_exist

def check_dataset_integrity():
    """Check if dataset has correct structure"""
    print("\n📊 Checking dataset integrity...")
    
    try:
        import pandas as pd
        df = pd.read_csv('dataset.csv')
        
        expected_columns = [
            'village_name', 'rainfall_current', 'rainfall_average',
            'groundwater_depth', 'population', 'storage_capacity',
            'current_storage', 'latitude', 'longitude',
            'historical_rainfall', 'historical_groundwater'
        ]
        
        print(f"   📈 Shape: {df.shape[0]} rows × {df.shape[1]} columns")
        
        # Check columns
        missing_cols = set(expected_columns) - set(df.columns)
        if missing_cols:
            print(f"   ❌ Missing columns: {missing_cols}")
            return False
        else:
            print(f"   ✅ All columns present")
        
        # Check for missing values
        missing_values = df.isnull().sum().sum()
        if missing_values > 0:
            print(f"   ⚠️  {missing_values} missing values found")
        else:
            print(f"   ✅ No missing values")
        
        # Check data types
        numeric_cols = df[['population', 'rainfall_current', 'groundwater_depth']].select_dtypes(
            include=['number']
        )
        if len(numeric_cols.columns) == 3:
            print(f"   ✅ Numeric columns properly typed")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error reading dataset: {e}")
        return False

def check_port_availability():
    """Check if Streamlit default port is available"""
    print("\n🔌 Checking port availability...")
    
    import socket
    port = 8501
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', port))
    sock.close()
    
    if result == 0:
        print(f"   ⚠️  Port {port} is in use")
        print(f"      → Use: streamlit run app.py --server.port 8502")
    else:
        print(f"   ✅ Port {port} is available")
    
    return result != 0

def test_imports():
    """Test if critical imports work"""
    print("\n🧪 Testing imports...")
    
    try:
        import streamlit as st
        print(f"   ✅ Streamlit {st.__version__}")
    except Exception as e:
        print(f"   ❌ Streamlit import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print(f"   ✅ Pandas {pd.__version__}")
    except Exception as e:
        print(f"   ❌ Pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print(f"   ✅ NumPy {np.__version__}")
    except Exception as e:
        print(f"   ❌ NumPy import failed: {e}")
        return False
    
    try:
        import sklearn
        print(f"   ✅ Scikit-learn {sklearn.__version__}")
    except Exception as e:
        print(f"   ❌ Scikit-learn import failed: {e}")
        return False
    
    try:
        import folium
        print(f"   ✅ Folium {folium.__version__}")
    except Exception as e:
        print(f"   ❌ Folium import failed: {e}")
        return False
    
    return True

def generate_report():
    """Generate comprehensive verification report"""
    print("\n" + "=" * 70)
    print("WATER GOVERNANCE DASHBOARD - SYSTEM VERIFICATION REPORT")
    print("=" * 70)
    
    results = {
        'Python Version': check_python_version(),
        'Required Packages': check_required_packages(),
        'Data Files': check_data_files(),
        'Model Files': check_model_files(),
        'Dataset Integrity': check_dataset_integrity(),
        'Import Tests': test_imports(),
    }
    
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    for check_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{check_name}: {status}")
    
    print("\n" + "=" * 70)
    
    # Overall assessment
    all_passed = all(results.values())
    
    if all_passed:
        print("✅ ALL CHECKS PASSED!")
        print("\n🚀 You're ready to launch the dashboard:")
        print("   streamlit run app.py")
        return 0
    else:
        failed_checks = [name for name, result in results.items() if not result]
        print("❌ SOME CHECKS FAILED:")
        for check in failed_checks:
            print(f"   • {check}")
        
        print("\n📋 NEXT STEPS:")
        
        if not results['Required Packages']:
            print("   1. Install missing packages:")
            print("      pip install -r requirements.txt")
        
        if not results['Model Files']:
            print("   2. Generate ML models:")
            print("      python generate_models.py")
        
        if not results['Data Files']:
            print("   3. Ensure all required files exist in current directory")
        
        print("\n   Then run verify_setup.py again to confirm")
        return 1

if __name__ == "__main__":
    try:
        exit_code = generate_report()
        sys.exit(exit_code)
    except Exception as e:
        print(f"\n❌ Verification failed with error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
