# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in colombian_localization/__init__.py
from colombian_localization import __version__ as version

setup(
	name='colombian_localization',
	version=version,
	description='localizacion colombiana',
	author='erpnextteam',
	author_email='erpnextteam@latinux.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
