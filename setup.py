from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    """Return a list of package requirements, excluding editable installs like '-e .'."""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.strip().startswith("-e")]
    return requirements

setup(
    name="credit_risk_scoring", 
    version="0.1.0",
    author="Snehal Sreedhar",
    author_email="snehal.sreedhar@alumni.ashoka.edu.in",
    description="A package for credit risk scoring using machine learning techniques.",
    packages=find_packages(),
    install_requires = get_requirements(r"C:\Projects\credit_risk_scoring\requirements.txt")
) 
