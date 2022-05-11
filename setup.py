from setuptools import setup, find_packages

setup(
    name='Gollum',
    version='0.1',
    author="bitex47",
    author_email="xyjy5247@gmail.com",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'paramiko >= 2.10.1',
    ],
)
