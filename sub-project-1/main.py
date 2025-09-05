#!/usr/bin/env python3
"""
Main entry point for Sub-project 1.
"""

import sys
import os

# Add the shared directory to the path so we can import shared utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'shared'))

# Add sub-project-2 to the path so we can import its utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sub-project-2'))

try:
    from common_utils import greet_user
    shared_utils_available = True
except ImportError:
    shared_utils_available = False
    print("Warning: Could not import shared utilities")

try:
    from project2_utils import project2_function, calculate_cube
    project2_utils_available = True
except ImportError:
    project2_utils_available = False
    print("Warning: Could not import sub-project 2 utilities")

def main():
    """Main function for Sub-project 1."""
    print("=" * 40)
    print("Sub-project 1 is running!")
    print("=" * 40)
    
    if shared_utils_available:
        greet_user("Sub-project 1")
        print("Successfully used shared utility function!")
    else:
        print("Running without shared utilities")
    
    if project2_utils_available:
        print(f"\nImported from Sub-project 2: {project2_function()}")
        print(f"Using Sub-project 2's cube function: 3^3 = {calculate_cube(3)}")
        print("Successfully used sub-project 2 utility functions!")
    else:
        print("Could not use sub-project 2 utilities")
    
    print("\nThis is a simple demonstration of Sub-project 1.")
    print("In a real project, this would contain the actual functionality.")

if __name__ == "__main__":
    main()