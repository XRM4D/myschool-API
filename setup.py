#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: XRM4D
:license: GNU General Public License v3.0, see license file
:copyright: (c) 2023 XRM4D
"""

version = '0.1'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='myschool-API',
    url='https://github.com/XRM4D/myschool-API',
    version=version,

    author='XRM4D',
    author_email='me@xrmfourd.ru',

    description=(
        u'API for the electronic diary system "My School"'
    ),
    long_description=long_description,
    long_description_content_type = 'text/markdown',

    license='GNU General Public License v3.0',

    packages=['myschool-API'],
    install_requires=[],

    classifiers=[
        'License :: OSI Approved :: GNU General Public License',
        'Operating System :: OS Independent',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
