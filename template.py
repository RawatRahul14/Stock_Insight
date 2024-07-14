import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[%(asctime)s]: %(message)s:")

project_name = "FinancProject"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research.trails.ipynb",
    "templates/index.html"
]

# Looping through all the names of the files in the list
for filepath in list_of_files:
    # Taking their Path
    filepath = Path(filepath)
    # Splitting the directory name and filename
    filedir, filename = os.path.split(filepath)

    # If the file_directory is not empty
    if filedir != "":

        # Making a directory
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating Directory: {filedir} for the file: {filename}")

    # If the filepath doesn't exist or the size of the file is 0
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # Create a new file 
        with open(filepath, "w") as f:
            pass
            logging.info(f"creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists.")