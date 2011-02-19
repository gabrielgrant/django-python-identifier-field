from setuptools import setup

setup(
    name='django-python-identifier-field',
    version='0.1.1dev',
    author='Gabriel Grant',
    packages=[
        'python_identifier_field',
        'python_identifier_field.db',
        'python_identifier_field.db.models',
    ],
    license='LGPL',
    long_description=open('README').read(),
)

