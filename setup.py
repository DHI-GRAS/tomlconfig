from setuptools import setup, find_packages

setup(
    name='tomlconfig',
    version='0.2',
    description='TOML config file parsing',
    author='Jonas Solvsteen',
    author_email='josl@dhi-gras.com',
    packages=find_packages(),
    install_requires=['toml'])
