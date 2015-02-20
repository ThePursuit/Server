__author__ = 'Andrea'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'The Pursuit',
    'author': 'Christofer Benett, Andrea Buchholz, Cenny Davidsson, Michael Tran ',
    'url': 'https://github.com/ThePursuit/Server',
    'author_email': 'My email.',
    'version': '0.1',
    'packages': ['The Pursuit'],
    'scripts': [],
    'name': 'The Pursuit'
}

setup(**config)