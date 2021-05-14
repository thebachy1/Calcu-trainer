# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in calcu_trainer/__init__.py
from calcu_trainer import __version__ as version

setup(
	name='calcu_trainer',
	version=version,
	description='Calculo de nomina para entrenadores',
	author='thebachy1',
	author_email='manuel.curiel@veco.dev',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
