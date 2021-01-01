from setuptools import setup

with open ("README.md","r",encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='core',
    version='1.0',
    author = "Harsh Vardhan",
    author_email="harshfebruary@gmail.com",
    description = "Assingment Package",
    long_description = long_description ,
    long_description_content_type="text/markdown",
    script = ['core.py'],
    python_requires = '>=3.6',
)