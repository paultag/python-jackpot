#!/usr/bin/env python
from setuptools import setup, find_packages
from jackpot import __version__

long_description = ''

setup(name='jackpot',
      version=__version__,
      packages=find_packages(),
      description='',
      long_description=long_description,
      platforms=['any'],
      install_requires=[
          'jsonschema==2.6.0',
      ],
      extras_require={},
  )
