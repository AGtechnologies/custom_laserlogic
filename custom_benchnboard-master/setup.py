# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='custom_benchnboard',
    version=version,
    description='Customisation for Bench and Board Pte Ltd',
    author='AG Technologies Pte Ltd',
    author_email='info@agtech.com.sg',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
