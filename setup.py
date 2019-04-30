## =========================================================
## Copyright 2019 Dietrich Bollmann
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##      http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## ---------------------------------------------------------

"""setup.py:

Setup file for the NewSkyLabs Python project nslgo.

"""

import setuptools 
import codecs
import os

## =========================================================
## Setup utilities
## ---------------------------------------------------------

def read_file(*parts):
    """
    Read a file and return its content
    """
    package_dir = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(package_dir, *parts), 'r') as fp:
        return fp.read()

def find_packages(namespace):
    """
    Return a list of all Python packages defined in the 'namespace'
    directory
    """
    return [
        '{}.{}'.format(namespace, package) 
        for package in setuptools.PackageFinder.find(where=namespace)
    ]

def find_scripts(dir):
    """
    Return the list of scripts defined in 'dir'
    """
    package_dir = os.path.abspath(os.path.dirname(__file__))
    script_dir = os.path.join(package_dir, dir)
    scripts = [os.path.join(dir, script)
               for script in os.listdir(script_dir) 
               if os.path.isfile(os.path.join(script_dir, script))]
    return scripts

## =========================================================
## Setup
## ---------------------------------------------------------

namespace    = 'nsl'
subnamespace = 'go'

# Load the package metadata 
exec(read_file(namespace, subnamespace, '__about__.py'))

# Read the long description
long_description = read_file('README.md')

# List of packages
packages = find_packages(namespace)

# List of scripts
scripts = find_scripts('scripts')

# Setup package
setuptools.setup(
    name=__package_name__,
    version=__version__,
    description=__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__email__,
    license=__license__,
    url=__url__,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    platforms=['Posix', 'Unix', 'Linux', 'MacOS X', 'Windows'],
    packages=packages,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'nslgo = nsl.go.__main__:cli',
        ]
    },
    scripts=scripts,
)

## =========================================================
## =========================================================

## fin.
