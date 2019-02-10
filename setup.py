'''Build script for this package

'''

import setuptools

with open("README", 'r') as fh:
    long_description = fh.read()
    
setuptools.setup(
    name = "wh40k8edutils",
    version = "0.1",
    author = "David Taylor",
    author_email = "dmtaylor2011@gmail.com",
    description = "Utilities for Warhammer 40k 8ed",
    long_description = long_description,
    long_desctiption_type = "text/plain",
    url = "https://github.com/dmtaylor/wh40k8edutils",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Other Audience",
        "Operating System :: OS Independent",
        "Topic :: Games/Entertainment :: Board Games"
    ],
)
