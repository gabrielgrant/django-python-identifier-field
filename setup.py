from setuptools import setup

setup(
    name='django-python-identifier-field',
    version='0.1.0dev',
    author='Gabriel Grant',
    packages=[
        'python_identifier_field',
        'python_identifier_field.db.models',
    ],
    license='LGPL',
    long_description=open('README').read(),
)

