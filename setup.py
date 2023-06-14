from setuptools import setup, find_packages

setup(
    name='re2shield',
    version='0.1.0',
    url='https://github.com/Npc-coder/re2shield',  # Replace with your own GitHub project URL
    author='mkCha',
    author_email='dxsaq0@gmail.com',
    description='A Python library that provides a convenient interface for compiling and matching regular expression patterns using the re2 library.',
    packages=find_packages(),    
    install_requires=['google-re2', 'pickle5'],  # List your package's dependencies
)
