#!/usr/bin/env python
from setuptools import setup

setup(
    name='mplstyle',
    version='0.1.0',
    description='A simple API for setting matplotlib styles in matplotlib.',
    long_description=open('README.md').read(),
    author='Jeremy Singer-Vine',
    author_email='jsvine@gmail.com',
    url='https://github.com/jsvine/mplstyle',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    packages=[
        'mplstyle', 
        'mplstyle.styles'
    ]
)
