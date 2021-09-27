from setuptools import setup, find_namespace_packages

setup(
    name="redondeo",
    version="0.2",
    package_dir={'redondeo': 'src/redondeo'},
    packages=find_namespace_packages('src')
)
