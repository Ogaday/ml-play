try:
    from setuptools import setup
except InputError:
    from distutils.core import setup

requirements = ['nose']

config = {
    'description' : 'Package providing classes for machine learning data structures and algorithms',
    'author' : 'Ogaday',
    'url' : 'www.github.com/Ogaday/ml-play',
    'download_url' : '',
    'author_email' : 'W.Ogaday@gmail.com',
    'version' : '0.0',
    'install_requires' : requirements,
    'packages' : ['ann'],
    'scripts' : [],
    'name' : 'ml-play'
}


setup(**config)
