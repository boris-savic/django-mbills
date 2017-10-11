import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mbills',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='Django implementation of the Hal MBills APIs.',
    url='https://github.com/boris-savic/django-mbills',
    author='Boris Savic',
    author_email='boris70@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
