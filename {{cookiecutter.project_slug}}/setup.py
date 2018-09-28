#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""{{ cookiecutter.project_slug }} setup script."""

from codecs import open
from setuptools import setup, find_packages
import os


project_slug = '{{ cookiecutter.project_slug }}'
root_path = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(root_path, 'README.rst')) as readme_file:
    readme = readme_file.read()
with open(os.path.join(root_path, 'HISTORY.rst')) as history_file:
    history = history_file.read()

requirements = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0',{%- endif %} ]

setup_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-runner',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest',{%- endif %} ]

dev_requirements = [
    'Sphinx',
    'bumpversion',
    'check-manifest',
    'flake8',
    'pip',
    {% if cookiecutter.use_pytest == 'y' -%}
    'pytest',
    'pytest-cov',{% endif %}
    'readme_renderer',
    'wheel',
    'watchdog',
    'tox',
    'twine',
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="{{ cookiecutter.project_short_description }}",
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={
        'console_scripts': [
            '{0}={0}.__main__:main'.format(project_slug),
        ],
    },
    {%- endif %}
    extras_require={
        'dev': dev_requirements,
    },
    install_requires=requirements,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
{%- endif %}
    long_description='{0}\n\n{1}'.format(readme, history),
    include_package_data=True,
    keywords='{{ cookiecutter.project_slug }}',
    name=project_slug,
    packages=find_packages(include=[project_slug]),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/{{ cookiecutter.github_username }}/{0}'.format(project_slug),
    version='{{ cookiecutter.version }}',
    zip_safe=False,
)
