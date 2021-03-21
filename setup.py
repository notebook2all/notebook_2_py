from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=7", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="notebook_2_py",
    version="0.0.13",
    author="Sebastian Gonzalez-Tirado",
    author_email="sebgoti8@gmail.com",
    description="A package to convert your Jupyter Notebook",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/notebook2all/notebook_2_py/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
