#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = ['pandas>=1.1.0', 'numpy>=1.19.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="10academy-Group3",
    email="",
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: 10 Academy',
        'Natural Language :: English',
      
        'Programming Language :: Python :: 3.8',
    ],
    description="Amharic Speech Recognition",
    install_requires=requirements,
    long_description=readme,
    include_package_data=True,
    keywords='scripts',
    name='scripts',
    packages=find_packages(include=['scripts', 'scripts.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/10acad-group3/speech_recognition.git',
    version='0.1.0',
    zip_safe=False,
)
