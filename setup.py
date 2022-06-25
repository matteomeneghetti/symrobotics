from setuptools import setup, find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="symrobotics",
    version="0.1.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["sympy"],
    python_requires='>=3.6',
    url="",
    license="MIT",
    author="Matteo Meneghetti",
    author_email="matteo@meneghetti.dev"
)
