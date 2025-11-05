#!/usr/bin/env python3
import subprocess
import sys
import os

def run_tests():
    print("Starting Rapyuta QA Automation Test Suite...")
    
    # Create reports directory
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    try:
        # Run tests
        result = subprocess.run([
            'pytest', 'src/tests/', '-v', '-s',
            '--alluredir=reports/allure_results',
            '--html=reports/pytest_report.html',
            '--self-contained-html'
        ])
        
        print(f"Test execution completed. Exit code: {result.returncode}")
        return result.returncode
        
    except Exception as e:
        print(f" Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())