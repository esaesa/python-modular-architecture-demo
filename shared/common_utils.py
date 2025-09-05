#!/usr/bin/env python3
"""
Common utilities that can be shared between sub-projects.
"""

def greet_user(project_name):
    """Greet the user with the project name."""
    print(f"Hello from {project_name}!")
    return f"Greeting sent from {project_name}"

def format_shared_output(text):
    """Format text with shared styling."""
    return f"[Shared Utility] {text}"

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers together."""
    return a * b