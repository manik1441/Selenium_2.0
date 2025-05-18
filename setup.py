import os
import subprocess
import sys

venv_dir = "venv"

# Create virtual environment
if os.path.isdir(venv_dir):
    print(f"Virtual environment already exists in .\\{venv_dir}.")
else:
    subprocess.check_call([sys.executable, "-m", "venv", venv_dir])
    print(f"Virtual environment created in .\\{venv_dir} and requirements installed.")

# Determine pip path
if os.name == "nt":
    pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
else:
    pip_path = os.path.join(venv_dir, "bin", "pip")

# Install requirements
subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])

print(f"To activate the virtual environment, run:\n{venv_dir}/bin/activate")