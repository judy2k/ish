#!/usr/bin/env python

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

REQUIREMENTS = []

TEST_REQUIREMENTS = [
    "pytest>=2.7.2",
]

class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='ish',
    version="0.0.0",
    description="Make Python more like more sensible languages.",
    url="https://github.com/judy2k/fictionary",

    author="Mark Smith",
    author_email="<mark.smith@practicalpoetry.co.uk>",

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],

    py_modules=['ish'],
    install_requires=REQUIREMENTS,
    zip_safe=False,

    cmdclass={'test': PyTest},
    tests_require=TEST_REQUIREMENTS,
)
