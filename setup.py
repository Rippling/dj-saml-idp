# -*- coding: utf-8 -*-
from setuptools import setup
import saml2idp


with open('README.rst') as readme:
    description = readme.read()


with open('HISTORY.rst') as history:
    changelog = history.read()


setup(
    name='dj-saml-idp',
    version=saml2idp.__version__,
    author='Sebastian Vetter',
    author_email='sebastian@mobify.com',
    description='SAML 2.0 IdP for Django',
    long_description='\n\n'.join([description, changelog]),
    install_requires=[
        'Django>=1.4',
        # We have to pin M2Crypto to version 0.22.3 because more recent
        # versions are failing due to issues with finding openssl libs.
        'M2Crypto==0.22.3',
        'BeautifulSoup>=3.2.0',
        'structlog'],
    license='MIT',
    packages=['saml2idp'],
    url='http://github.com/mobify/dj-saml-idp',
    zip_safe=False,
    include_package_data=True,
)
