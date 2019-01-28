#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# ___  ___                       _____           _______
# |  \/  |                      |_   _|         | | ___ \
# | .  . |_   _ ___  ___  ___     | | ___   ___ | | |_/ / _____  __
# | |\/| | | | / __|/ _ \/ _ \    | |/ _ \ / _ \| | ___ \/ _ \ \/ /
# | |  | | |_| \__ \  __/ (_) |   | | (_) | (_) | | |_/ / (_) >  <
# \_|  |_/\__,_|___/\___|\___/    \_/\___/ \___/|_\____/ \___/_/\_\
#
# @author:  Nicolas Karasiak
# @site:    www.karasiak.net
# @git:     www.github.com/lennepkade/MuseoToolBox
# =============================================================================
from __future__ import absolute_import
import re

__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    open('museotoolbox/__init__.py').read()).group(1)


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='museotoolbox',
    version=__version__,
    description='Raster and vector tools for Remote Sensing and Classification',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/lennepkade/MuseoToolBox',
    author='Nicolas Karasiak',
    author_email='karasiak.nicolas@gmail.com',
    license='GPLv3',
    install_requires=["numpy","scipy","matplotlib","scikit-learn"],
    packages=setuptools.find_packages(),
    classifiers=[
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: GIS",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 2",
            "Intended Audience :: Science/Research"],
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'mtb_sampleExtraction=museotoolbox.vectorTools.sampleExtraction:main',
            'mtb_modalClass=museotoolbox.stats.computeClassificationStability:modalClassCLI'
        ],
    }
 )
