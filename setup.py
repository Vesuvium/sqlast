#!/usr/bin/env python
import io
import os
import sys

from setuptools import find_packages, setup

from sqlast.Version import version


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


readme = io.open('README.md', 'r', encoding='utf-8').read()

setup(
    name='sqlast',
    description='An SQL parser that uses LALR for sql parsing',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/Vesuvium/sqlast',
    author='Jacopo Cascioli',
    author_email='noreply@jacopocascioli.com',
    version=version,
    license='MIT',
    packages=find_packages() + ['grammar'],
    include_package_data=True,
    tests_require=[
        'coverage>=4.5.1',
        'pytest>=3.6.0',
        'pytest-mock>=1.10.0'
    ],
    setup_requires=[],
    install_requires=[
        'click>=6.7',
        'lark-parser>=0.6.4'
    ],
    classifiers=[],
    entry_points={
        'console_scripts': ['sqlast=sqlast.Cli:Cli.main']
    }
)
