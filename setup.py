from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of individual libraries from requirements.txt
    '''
    requirements = []
    with open(file_path, 'r') as file:
        file_content = file.readlines()
        requirements = [requirement.replace('\n', '') for requirement in file_content]
    
    print(requirements)
    
    return requirements

# used command 'pip install -e .' for installing dependencies 

setup (
    name = "MLProject",
    version = "0.0.1",
    author = "Tanya",
    author_email = "sharma.tanya151002@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)
