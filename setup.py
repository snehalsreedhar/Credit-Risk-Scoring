from setuptools import setup, find_packages
import os

def get_requirements(file_path: str) -> list[str]:
    """Return a list of package requirements, excluding editable installs like '-e .'."""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        return [req.strip() for req in requirements if req.strip() and not req.strip().startswith("-e")]

# Automatically find the path to requirements.txt relative to this file
current_dir = os.path.dirname(__file__)
requirements_path = os.path.join(current_dir, "requirements.txt")

setup(
    name="credit_risk_scoring", 
    version="0.1.0",
    author="Snehal Sreedhar",
    author_email="snehal.sreedhar@alumni.ashoka.edu.in",
    description="A package for credit risk scoring using machine learning techniques.",
    packages=find_packages(),
    install_requires=get_requirements(requirements_path)
)
