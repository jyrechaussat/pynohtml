import setuptools
import unittest

def pynohtml_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('pynohtml.tests', pattern='test_*.py')
    return test_suite

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pynohtml", # Replace with your own username
    version="0.0.2",
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
    test_suite="setup.pynohtml_test_suite",    
    include_package_data=True,
)
