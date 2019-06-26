from setuptools import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name="Json2PascalVoc",
	version='1.0.2',
	author='Caner Karagüler',
	author_email='caner.karaguler@gmail.com',
	long_description = long_description,
	long_description_content_type="text/markdown",
	description = 'Package To Convert Json Files To PascalVOC XML files',
	py_modules=["Converter"],
	package_dir={'':'Json2PascalVoc'},
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

	)