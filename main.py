#!/usr/bin/env python3
"""
Main entry point for the project.
This script welcomes the user and asks which sub-project to run.
"""

import os
import sys

def main():
    """Main function to run the project selector."""
    print("=" * 50)
    print("Welcome to the Multi-Project Runner!")
    print("=" * 50)
    
    while True:
        print("\nPlease select a sub-project to run:")
        print("1. Sub-project 1")
        print("2. Sub-project 2")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\nStarting Sub-project 1...")
            # Run sub-project 1
            os.system(f"python {os.path.join('sub-project-1', 'main.py')}")
        elif choice == "2":
            print("\nStarting Sub-project 2...")
            # Run sub-project 2
            os.system(f"python {os.path.join('sub-project-2', 'main.py')}")
        elif choice == "3":
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()