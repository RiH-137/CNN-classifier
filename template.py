import os
import sys

from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s")

# Package name
package_name = "CNNClassifier"

# List of files to create inside the package
list_of_files = [
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "dvc.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb",
]

for filepath in list_of_files:
    # Convert path to Path object for easier manipulation
    filepath = Path(filepath)

    # Separate directory and filename
    filedir, filename = filepath.parent, filepath.name  # Using Path object methods

    # Create directory if it doesn't exist (handling potential errors)
    try:
        os.makedirs(filedir, exist_ok=True)  # Create nested directories if needed
        logging.info(f"Creating directory: {filedir}")
    except OSError as e:
        logging.error(f"Error creating directory: {e}")

    # Check if file exists and create it if necessary
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating file: {filename}")
    else:
        logging.info(f"File already exists: {filename}")