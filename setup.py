from setuptools import setup
import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
	name="Json2PascalVoc",
	version='1.0.4',
	author='Caner Karagüler',
	author_email='caner.karaguler@gmail.com',
	long_description = long_description,
	long_description_content_type="text/markdown",
	description = 'Package To Convert Json Files To PascalVOC XML files',
	py_modules=["Converter"],
	packages=setuptools.find_packages(),
	url="https://github.com/canerkaraguler/Json2PascalVOC",
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

	)