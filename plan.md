# Project Structure Plan

## Overview
This project will contain two sub-projects that can be run independently but share common utilities. A main script will welcome users and ask which sub-project they want to run.

## Directory Structure
```
project/
├── main.py                 # Main script to choose sub-project
├── sub-project-1/          # First sub-project
│   ├── main.py             # Entry point for sub-project 1
│   └── project1_utils.py   # Project-specific utilities
├── sub-project-2/          # Second sub-project
│   ├── main.py             # Entry point for sub-project 2
│   └── project2_utils.py   # Project-specific utilities
└── shared/                 # Shared utilities between projects
    ├── __init__.py         # Python package initializer
    └── common_utils.py     # Common utilities used by both projects
```

## Implementation Details

### Main Script (main.py)
- Welcome message
- Menu to choose which sub-project to run
- Execute the selected sub-project

### Sub-project 1
- Independent runnable project
- Can access shared utilities
- Can import and use functionality from sub-project 2
- Has its own project-specific utilities

### Sub-project 2
- Independent runnable project
- Can access shared utilities
- Can import and use functionality from sub-project 1
- Has its own project-specific utilities

### Shared Utilities
## Cross-Project Imports Implementation

To enable importing from one sub-project to another, we modify the Python path in each sub-project's main script:

```python
# Add sub-project-2 to the path so we can import its utilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'sub-project-2'))
```

This allows each sub-project to import functions and classes from the other sub-project.

## Best Practices Discussion

### Current Approach
The current implementation uses `sys.path.append()` to enable cross-project imports. While this works for this specific use case, it's not considered the most elegant solution for larger projects.

### Alternative Approaches
1. **Proper Python Package Structure**: Convert each sub-project into a proper Python package with `setup.py` files, then install them in development mode using `pip install -e`.

2. **Relative Imports**: If the projects were structured as a single Python package, relative imports could be used.

3. **PYTHONPATH Environment Variable**: Set the PYTHONPATH to include all necessary directories.

4. **Virtual Environment with Editable Installs**: Create a virtual environment and install each sub-project as an editable package.

### When to Use Each Approach
- **Current approach** (`sys.path.append`): Good for simple projects, prototypes, or when you need maximum flexibility without package installation.
- **Package structure with setup.py**: Better for larger projects, production code, or when you want to distribute your code.
- **Relative imports**: Best when all code is part of a single cohesive package.
- **PYTHONPATH**: Useful in development environments or Docker containers.

For this project structure, where we want independently runnable sub-projects that can also share code, the current approach provides a good balance of simplicity and functionality.
- Common functions that both sub-projects can use
- Located in a separate folder for easy access

## Execution Flow
```mermaid
graph TD
    A[Start main.py] --> B[Display welcome message]
    B --> C[Show sub-project options]
    C --> D{User choice}
    D -->|Sub-project 1| E[Run sub-project-1/main.py]
    D -->|Sub-project 2| F[Run sub-project-2/main.py]
    D -->|Exit| G[End program]