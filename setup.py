#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='fenixedu_django',
		version='0.0.1',
		description='FenixEdu Django utilities',
		author='Samuel Coelho',
		author_email='samuelfcmc@gmail.com',
		url='https://github.com/samfcmc/fenixedu_django',
		install_requires=[],
		packages=['fenixedu.authentication']
		)