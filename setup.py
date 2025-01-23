from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path='requirements.txt') -> List[str]:
    '''
    Read requirements from file
    '''
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='1.0',
    author='Uriel Zaed',
    author_email='urielzaed33@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
