from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
	name="JsonToPascalVoc",
	version='0.0.2',
	author='Caner Karagüler',
	author_email='caner.karaguler@gmail.com',
	long_description = long_description,
	long_description_content_type="text/markdown",
	description = 'Package To Convert Json Files To PascalVOC XML files',
	py_modules=["Converter"],
	package_dir={'':'JsonToPascalVoc'},
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

	)