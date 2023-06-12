#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='my_scripts',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'hello-world = scripts.hello_world:main', 
            'another-message = scripts.another_message:main'
        ]
    }
)