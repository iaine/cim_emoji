#!/usr/bin/env python

from distutils.core import setup

setup(name='cim_emoji',
      version='0.1',
      description='Exploring emojis and text',
      author='Iain Emsley',
      author_email='iain.emsley@warwick.ac.uk',
      url='',
      data_files=[('.', ['cim_emoji/codes.json'])],
      packages=['cim_emoji'],
      package_dir={'cim_emoji': 'cim_emoji'},
      package_data={'cim_emoji': ['*.json']},
     )