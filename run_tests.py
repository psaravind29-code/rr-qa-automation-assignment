#!/usr/bin/env python3
import subprocess
import sys
import os

def run_tests():
    print(" Starting Rapyuta QA Automation Test Suite...")
    
    # Create reports directory
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    try:
        # Run tests using python module syntax (more reliable)
        print(" Installing dependencies...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
        
        print(" Running tests...")
        result = subprocess.run([
            sys.executable, '-m', 'pytest', 'src/tests/', '-v', '-s',
            '--alluredir=reports/allure_results',
            '--html=reports/pytest_report.html',
            '--self-contained-html'
        ], capture_output=False, text=True)
        
        print(f" Test execution completed. Exit code: {result.returncode}")
        return result.returncode
        
    except subprocess.CalledProcessError as e:
        print(f" Dependency installation failed: {e}")
        return 1
    except FileNotFoundError:
        print(" Python or pytest not found. Please ensure Python is installed and in your PATH.")
        return 1
    except Exception as e:
        print(f" Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())