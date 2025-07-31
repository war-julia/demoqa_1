#!/usr/bin/env python3
"""
Ломоносовская Гимназия Test Automation Framework

This script provides a simple interface to run tests for the Ломоносовская гимназия website.
The framework uses Selenium WebDriver and Python to automate testing of the school's website.

Usage:
    python main.py                    # Run all tests
    python main.py --test main       # Run main page tests only
    python main.py --test news       # Run news page tests only
    python main.py --test education  # Run education page tests only
    python main.py --test contacts   # Run contacts page tests only
"""

import sys
import subprocess
import argparse


def run_tests(test_type=None):
    """Run the specified tests"""
    if test_type:
        print(f"Running {test_type} page tests...")
        subprocess.run(["pytest", f"tests/test_{test_type}_page.py", "-v"])
    else:
        print("Running all tests...")
        subprocess.run(["pytest", "tests/", "-v"])


def main():
    """Main function to handle command line arguments and run tests"""
    parser = argparse.ArgumentParser(
        description="Ломоносовская Гимназия Test Automation Framework"
    )
    parser.add_argument(
        "--test", 
        choices=["main", "news", "education", "contacts"],
        help="Specify which test suite to run"
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Ломоносовская Гимназия Test Automation Framework")
    print("=" * 60)
    print("Testing website: https://ломоносовскаягимназия.рф/")
    print("=" * 60)
    
    run_tests(args.test)
    
    print("=" * 60)
    print("Test execution completed!")
    print("=" * 60)


if __name__ == '__main__':
    main()
