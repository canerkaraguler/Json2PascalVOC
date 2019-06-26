from setuptools import setup


setup(
	name="JsonToPascalVoc",
	version='0.0.2',
	author='Caner Karagüler',
	author_email='caner.karaguler@gmail.com',
	long_description = 'JsonToPascalVoc is a Python library for converting some special Json strings to PascalVOC format XML files.',
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