#!/usr/bin/env python3
"""
DemoQA Test Automation Framework

This script provides a simple interface to run tests for the DemoQA website.
The framework uses Selenium WebDriver and Python to automate testing.

Usage:
    python main.py                    # Run all tests
    python main.py --test elements    # Run elements page tests only
    python main.py --test textbox     # Run text box tests only
    python main.py --test form        # Run form tests only
    python main.py --test accordion   # Run accordion tests only
"""

import sys
import subprocess
import argparse


def run_tests(test_type=None):
    """Run the specified tests"""
    if test_type:
        print(f"Running {test_type} tests...")
        if test_type == "elements":
            subprocess.run(["pytest", "tests/test_go_to_page_elements.py", "-v"])
        elif test_type == "textbox":
            subprocess.run(["pytest", "tests/tests_hw/test_text_box.py", "-v"])
        elif test_type == "form":
            subprocess.run(["pytest", "tests/tests_hw/test_login_form_validate.py", "-v"])
        elif test_type == "accordion":
            subprocess.run(["pytest", "tests/tests_hw/test_visible_hw.py", "-v"])
    else:
        print("Running all tests...")
        subprocess.run(["pytest", "tests/", "-v"])


def main():
    """Main function to handle command line arguments and run tests"""
    parser = argparse.ArgumentParser(
        description="DemoQA Test Automation Framework"
    )
    parser.add_argument(
        "--test", 
        choices=["elements", "textbox", "form", "accordion"],
        help="Specify which test suite to run"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("DemoQA Test Automation Framework")
    print("=" * 60)
    print("Testing website: https://demoqa.com/")
    print("=" * 60)
    
    run_tests(args.test)
    
    print("=" * 60)
    print("Test execution completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
