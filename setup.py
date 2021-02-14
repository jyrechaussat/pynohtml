import setuptools
import unittest

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynohtml", # Replace with your own username
    version="0.0.21",
    author="grimnar",
    author_email="grimnar@gmail.com",
    description="framework to generate html/css/js",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grimnar/pynohtml",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
