#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys
import os

readme = open("README.md", "r").read()

history = open("HISTORY.md").read()

requirements = ["dominate==2.4.0"]

metadata = {}
version_filename = os.path.join(os.path.dirname(__file__), "cccp", "__version__.py")
exec(open(version_filename).read(), None, metadata)

setup(
    name="cccp",
    version=metadata["__version__"],
    description="semi server side rendered html and javascript",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    author=metadata["__author__"],
    author_email=metadata["__email__"],
    url="https://github.com/sloev/cccp",
    packages=["cccp"],
    package_dir={"cccp": "cccp"},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="cccp serverside server side rendering",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
