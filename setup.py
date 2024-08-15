## to install local package we use "setup.py" file.

## documentation related to setup.py file can be found at IPYNBrender 0.0.4

import setuptools 

__version__ = "0.1.0"

REPO_NAME = "CNNClassifier"
AUTHOR_NAME="RiH-137"
AUTHOR_EMAIL="101rishidsr@gmail.com"

SRC_REPO = "CNNClassifier"

## generating long description from the README.md file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A CNN Classifier",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https:github.com/{AUTHOR_NAME}/{REPO_NAME}",

    project_urls={
        "Bug Tracker": f"https:github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",    
    },
    package_dir={"": "src"}
    packages=setuptools.find_packages(where="src"), # find packages in the "src" directory
)












