#!/usr/bin/env python

import sys
from setuptools import setup, Command

REQUIREMENTS = []

TEST_REQUIREMENTS = [
    "pytest>=2.7.2",
]

class PyTest(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        sys.exit(pytest.main([]))

setup(
    name='ish',
    version="0.0.0",
    description="Make Python more like more sensible languages.",
    url="https://github.com/judy2k/ish",

    author="Mark Smith",
    author_email="<mark.smith@practicalpoetry.co.uk>",

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],

    py_modules=['ish'],
    install_requires=REQUIREMENTS,
    zip_safe=False,

    cmdclass={'test': PyTest},
    tests_require=TEST_REQUIREMENTS,
)
