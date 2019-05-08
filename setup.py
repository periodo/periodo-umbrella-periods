from setuptools import setup

import periodo_umbrella_periods_cli


def get_readme():
    with open('README.rst') as f:
        return f.read()


def get_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


setup(
    name=periodo_umbrella_periods_cli.__title__,
    version=periodo_umbrella_periods_cli.__version__,

    # TODO: Finish selecting the appropriate classifiers.

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    description=periodo_umbrella_periods_cli.__description__,
    long_description=get_readme(),
    url=periodo_umbrella_periods_cli.__url__,
    author=periodo_umbrella_periods_cli.__author__,
    author_email=periodo_umbrella_periods_cli.__author_email__,
    license=periodo_umbrella_periods_cli.__author_email__,
    packages=['periodo_umbrella_periods_cli'],
    install_requires=get_requirements(),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=get_requirements(),
    entry_points={
        'console_scripts': ['periodo-umbrellas=periodo_umbrella_periods_cli.cli:root'],
    }
)
