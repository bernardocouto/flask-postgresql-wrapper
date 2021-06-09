from setuptools import find_packages

import flask_postgresql_wrapper
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.abspath('README.md')) as file:
    long_description = file.read()

setup(
    author=flask_postgresql_wrapper.__author__,
    author_email=flask_postgresql_wrapper.__author_email__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Database'
    ],
    description='Flask PostgreSQL Wrapper is a simple adapter for PostgreSQL with connection pooling.',
    include_package_data=True,
    install_requires=[
        'dbutils',
        'psycopg2-binary',
        'pystache'
    ],
    keywords='flask postgresql',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='flask-postgresql-wrapper',
    packages=find_packages(),
    platforms='any',
    py_modules=['flask_postgresql_wrapper'],
    url='https://github.com/bernardocouto/flask-postgresql-wrapper',
    version=flask_postgresql_wrapper.__version__
)
