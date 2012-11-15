#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version = __import__('dormeur').__version__

setup(
    name='Dormeur',
    version=version,
    license='MIT',
    description='Restful webservices creation library built on top of flask',

    author='Oleiade',
    author_email='tcrevon@gmail.com',
    url='http://github.com/oleiade/Dormeur',

    classifiers=[
        'Development Status :: 0.0.1',
        'Environment :: Unix-like Systems',
        'Programming Language :: Python',
        'Operating System :: Unix-like',
    ],
    keywords='api restful library flask',

    packages=[
        'dormeur',
    ],
    package_dir={'': '.'},
    zip_safe=True,

    install_requires=[
        'flask>=0.9'
    ]
)
