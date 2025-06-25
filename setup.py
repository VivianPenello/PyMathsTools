# setup.py

from setuptools import setup, find_packages

setup(
    name="pymathstools",
    version="0.1.0",
    author="Vivian Penello",
    description="A modular Python library for a wide range of mathematical operations.",
    packages=find_packages(),
    python_requires=">=3.7",
    include_package_data=True,
)
