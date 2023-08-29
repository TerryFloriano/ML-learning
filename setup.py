from setuptools import find_packages, setup

from typing import List 

HYPHEN_E_DOT = "-e ."
def get_requirements(filepath: str) -> List[str]:
    """This function returns a list of requirements

    Args:
        filepath (str): Path for the requirements file

    Returns:
        List[str]: List of requirements
    """
    requiremnts = []
    with open(filepath) as f:
        requirements = f.readlines()
        requirements = [req.replace('\n', ' ') for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        

setup(
    name= "ML-learning", 
    version="0.0.1",
    author="TerryFloriano",
    author_email="ratombosoaterryfloriano86@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
)