from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='re2shield',
    version='0.1.1',
    url='https://github.com/Npc-coder/re2shield',  # Replace with your own GitHub project URL
    author='mkCha',
    author_email='dxsaq0@gmail.com',
    description='A Python library that provides a convenient interface for compiling and matching regular expression patterns using the re2 library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),    
    install_requires=['google-re2', 'pickle5'],  # List your package's dependencies
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
    ],
)
