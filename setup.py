from setuptools import setup, find_packages

def get_requirments(file_path: str) -> list[str]:
  
    """ This function will return the list of requirements
    """  
    HYPHEN_E_DOT = "-e ."
    requirements = []
    with open(file_path) as file_obj: 
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_E_DOT in requirements: 
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="credit_risk_scoring", 
    version="0.1.0",
    author="Snehal Sreedhar",
    author_email="snehal.sreedhar@alumni.ashoka.edu.in",
    description="A package for credit risk scoring using machine learning techniques.",
    packages=find_packages(),
    install_requires = get_requirments("requirements.txt")

)