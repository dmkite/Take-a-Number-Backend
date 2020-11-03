# setup.py
from setuptools import setup, find_packages

requires = [
    'tornado',
    'tornado-sqlalchemy',
    'psycopg2',
]

setup(
    name='tornado_todo',
    version='0.0',
    description='A To-Do List built with Tornado',
    author='Dylan Kite',
    author_email='kite.d92@gmail.com',
    keywords='web tornado',
    packages=find_packages(),
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'serve_app = todo:main',
        ],
    },
)
