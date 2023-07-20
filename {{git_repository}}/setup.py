# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

setup(
    name="{{python_package}}",
    version="1.0.0",
    author="{{author}}",
    packages=find_packages(include=["{{python_package}}", "{{python_package}}.*"]),
)
