from setuptools import setup, find_namespace_packages

setup(
    name='superfaktura_client',
    version='0.0.1',
    packages=find_namespace_packages(),
    url='https://github.com/eledio-helpers/superfaktura-client',
    license='',
    author='Richard Kubíček',
    author_email='kubicekr@eledio.com',
    install_requires=[
        "requests",
        "python-dotenv"
    ],
)
