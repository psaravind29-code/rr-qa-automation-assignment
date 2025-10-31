#!/usr/bin/env python3
import subprocess
import sys
import os

def run_tests():
    """Main function to execute the test suite"""
    print(" Starting Rapyuta QA Automation Test Suite...")
    print(" This may take a few minutes...")
    
    # Create reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Check if tests directory exists
    test_paths = [
        'src/tests/',
        'tests/',
        './'
    ]
    
    actual_test_path = None
    for path in test_paths:
        if os.path.exists(path):
            # Check if there are any Python files in the directory
            py_files = [f for f in os.listdir(path) if f.endswith('.py') and (f.startswith('test_') or f.endswith('_test.py'))]
            if py_files:
                actual_test_path = path
                print(f" Found tests in: {path}")
                break
    
    if not actual_test_path:
        print(" ERROR: No test directory or test files found!")
        print(" Looking for:")
        for path in test_paths:
            exists = "exists" if os.path.exists(path) else "missing"
            print(f"  - {path} ({exists})")
        
        # List what Python files we can find
        print("\n Available Python files:")
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.py'):
                    print(f"  - {os.path.join(root, file)}")
        return 1
    
    try:
        # Run tests with Allure reporting
        print("  Running tests...")
        result = subprocess.run([
            'python3', '-m', 'pytest', actual_test_path, '-v', '-s',
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