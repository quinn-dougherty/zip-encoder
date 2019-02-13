#!/usr/bin/env python
''' package setup/installation and metadata for zip-encoder ''' 

import setuptools

REQUIRED = [
        'numpy', 
        'pandas', 
        'altair'
        ]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
        name="zip-encoder", 
        version="0.0.0", 
        author="quinndougherty", 
        description="data cleaning and feature-engineering with latitude and longitude", 
        long_description=LONG_DESCRIPTION, 
        long_description_content_type="text/markdown",
        url = "https://github.com/quinndougherty/zip-encoder",
        packages=setuptools.find_packages(),
        python_requires=">=3.5",
        install_requires=REQUIRED,
        classifiers=[
		"Programming Language :: Python :: 3",
        	"Operating System :: OS Independent"
		]
        )
