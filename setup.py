# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst', encoding='utf_8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf_8') as f:
    license = f.read()

setup(
    name='PyPw',
    version='0.5.0',
    description='Password generator app',
    long_description=readme,
    author='Toughee',
    author_email='Trimmask@protonmail.com',
    url='https://github.com/Toughee/PyPw',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)