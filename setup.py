#!/usr/bin/env python
# -*- coding: utf-8 -*-

# {# pkglts, pysetup.kwds
# format setup arguments

from setuptools import setup, find_packages


short_descr = "Example package for the SEE platform"
readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


# find version number in src/see_example/version.py
version = {}
with open("src/see_example/version.py") as fp:
    exec(fp.read(), version)


setup_kwds = dict(
    name='see_example',
    version=version["__version__"],
    description=short_descr,
    long_description=readme + '\n\n' + history,
    author="revesansparole, ",
    author_email="revesansparole@gmail.com, ",
    url='https://github.com/revesansparole/see_example',
    license='cecill-c',
    zip_safe=False,

    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        ],
    tests_require=[
        "mock",
        "nose",
        ],
    entry_points={},
    keywords='',
    test_suite='nose.collector',
)
# #}
# change setup_kwds below before the next pkglts tag

setup_kwds['entry_points']['wralea'] = ['see = see_example']

# do not change things below
# {# pkglts, pysetup.call
setup(**setup_kwds)
# #}
