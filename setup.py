from setuptools import find_packages,setup
from typing import List

# to define all the dependency in our project by the setup.py file.
requirement_filePath = 'requirements.txt'
editable_indiacator = '-e .'
def get_requirements()->list[str]:
    with open(requirement_filePath) as requirementFile:
        requirement_list = requirementFile.readlines()
    requirement_list = [requirement.replace("\n","") for requirement in requirement_list]
    # removing the editable_indicator from the requirements
    if editable_indiacator in requirement_list:
        requirement_list.remove(editable_indiacator)
    return requirement_list


setup(name='healthcare',
      version='0.0.2', # every time when you will release your next time your project u wil have to change the version.
      description='Healthcare.',
      author='Govind',
      author_email='kumawatritik54@gmail.com',    # mail must be associated with git
      packages=find_packages(),     # it will find all the packages from your project.
      install_requires =get_requirements()  # varaible assigned by itself. to give the idea about dependencies.
)
