#!/usr/bin/env python3
import subprocess
import sys
import os

def run_tests():
    """Main function to execute the test suite"""
    print("🚀 Starting Rapyuta QA Automation Test Suite...")
    print("📋 This may take a few minutes...")
    
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    try:
        # Run tests with Allure reporting
        print("  Running tests...")
        result = subprocess.run([
            'python3', '-m', 'pytest', 'src/tests/', '-v', '-s',
            '--alluredir=reports/allure_results'
        ], capture_output=False, text=True)
        
        if result.returncode == 0:
            print(" All tests passed!")
        else:
            print(f" Some tests failed. Exit code: {result.returncode}")
        
        print(f" Test execution completed.")
        return result.returncode
        
    except Exception as e:
        print(f" Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())