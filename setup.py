"""
Flask-PyFCM
-------------

Flask extension for PyFCM - Python client for FCM
"""
from setuptools import setup


setup(
    name='Flask-PyFCM',
    version='0.1.1',
    url='https://github.com/rstit/flask-pyfcm/',
    license='BSD',
    author='RST-IT',
    author_email='piotr.poteralski@rst-it.com',
    description='Flask extension for PyFCM',
    long_description=__doc__,
    py_modules=['flask_pyfcm'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask', 'PyFCM'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)