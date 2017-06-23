import setuptools

setuptools.setup(
    name="test_server_extension",
    version='0.0.1',
    url="https://github.com/ryanlovett/nbrsessionproxy",
    author="Ryan Lovett",
    description="Jupyter server test extensions response",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[ 'tornado', 'notebook' ],
    package_data={'src': ['static/*']},
)
