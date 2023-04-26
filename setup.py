from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirments(file_path: str) -> List[str]: 
    '''
    this function will return a list of requirements
    '''
    requiements=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requiements = [req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requiements:
            requiements.remove(HYPEN_E_DOT)

    return requiements

setup(

    name='mlproject',
    version='0.0.1',
    author='hiroshi',
    author_email='hiroshiperera007@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')

)