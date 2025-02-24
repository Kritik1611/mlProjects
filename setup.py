from setuptools import find_packages, setup


def get_requirement(file_path):
    '''
    this fuction will return the requirments
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
        
        return requirements
    

setup(
name = 'mlproject',
version= '0.0.1',
author='Kritik',
author_email= 'www.kritikkumar@gmail.com',
packages= find_packages(),
install_requires = get_requirement('requirements.txt')
)