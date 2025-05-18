## Setup

1. Run the setup script to create a virtual environment and install dependencies:
   ```bash
   python setup.py
   ```
2. To activate the virtual environment, run:
   ```bash
   venv\Scripts\activate
   ```
3. To set the interpreter Go to:
    - File → Settings → Project: <your_project> → Python Interpreter -> Add Interpreter -> Select Existing
    - browse the python path and select Python executable - 'venv\Scripts\python.exe'.

# UI Testing Framework
## Overview
This framework provides a modular structure to test UIs using `Python` `pytest`,`selenium`. It includes:
- Based on Page Object Model (POM) design pattern.
- Logging and custom HTML reporting using `pytest-html`.
- csv/DB based for data configuration.
- Utility scripts for common actions.

# API Testing Framework

## Overview
This framework provides a modular structure to test APIs using `Python` `pytest` `request`. It includes:
- YAML-based configuration for API details.
- Utility scripts for common actions like authentication.
- HTML and custom report generation.