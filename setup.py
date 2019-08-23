from setuptools import find_packages, setup

setup(
    name='selenium-design-patterns-playground',
    version='0.1',
    description='Package for demonstrating how you can use the selenium-design-patterns python package.',
    license='MIT',
    install_requires=[
        'selenium',
    ],
    packages=find_packages()
)
