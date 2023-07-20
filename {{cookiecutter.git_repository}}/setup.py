# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="{{cookiecutter.python_package}}",
    version="1.0.0",
    author="{{cookiecutter.author}}",
    packages=find_packages(include=["{{cookiecutter.python_package}}", "{{cookiecutter.python_package}}.*"]),
)
