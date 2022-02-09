# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst', encoding='utf_8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf_8') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='',
    long_description=readme,
    author='',
    author_email='',
    url='https://github.com/Toughee/PyPw',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)