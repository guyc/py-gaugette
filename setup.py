#!/usr/bin/env python

from distutils.core import setup

setup(name='gaugette',
      version='1.2',
      description='Python library for building embedded devices with the Raspberry Pi',
      author='Guy Carpenter',
      author_email='guy@clearwater.com.au',
      url='http://github.com/guyc/py-gaugette/',
      license = 'LICENSE.txt',
      long_description=open('README.txt').read(),
      packages=['gaugette', 'gaugette.fonts'],
)
