import os
from setuptools import setup

if os.path.isfile('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = 'See http://pypi.python.org/pypi/mailjet/'

setup(
    name='mailjet',
    version='1.4',
    author='Rick van Hattem',
    author_email='Rick.van.Hattem@Fawo.nl',
    description='''mailjet is a django app to implement the mailjet v3 REST
        API''',
    url='https://github.com/WoLpH/mailjet',
    license='BSD',
    packages=['mailjet'],
    long_description=long_description,
    install_requires=['requests',],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'License :: OSI Approved :: BSD License',
    ],
    data_files=[('', ['LICENSE'])],
)

