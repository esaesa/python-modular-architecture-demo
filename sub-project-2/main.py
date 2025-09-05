#!/usr/bin/env python3
"""
Main entry point for Sub-project 2.
"""

import sys
import os

# Add the shared directory to the path so we can import shared utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

# Add sub-project-1 to the path so we can import its utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sub-project-1'))

try:
    from common_utils import greet_user
    shared_utils_available = True
except ImportError:
    shared_utils_available = False
    print("Warning: Could not import shared utilities")

try:
    from project1_utils import project1_function, calculate_square
    project1_utils_available = True
except ImportError:
    project1_utils_available = False
    print("Warning: Could not import sub-project 1 utilities")

def main():
    """Main function for Sub-project 2."""
    print("=" * 40)
    print("Sub-project 2 is running!")
    print("=" * 40)
    
    if shared_utils_available:
        greet_user("Sub-project 2")
        print("Successfully used shared utility function!")
    else:
        print("Running without shared utilities")
    
    if project1_utils_available:
        print(f"\nImported from Sub-project 1: {project1_function()}")
        print(f"Using Sub-project 1's square function: 4^2 = {calculate_square(4)}")
        print("Successfully used sub-project 1 utility functions!")
    else:
        print("Could not use sub-project 1 utilities")
    
    print("\nThis is a simple demonstration of Sub-project 2.")
    print("In a real project, this would contain the actual functionality.")

if __name__ == "__main__":
    main()