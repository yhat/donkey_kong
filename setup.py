from distutils.core import setup
from setuptools import find_packages

setup(
    name='donkey_kong',
    version='0.3',
    author="Jessie Frazelle",
    author_email="jessie@yhathq.com",
    url="https://github.com/yhat/donkey_kong",
    packages=find_packages(),
    description="Send mandrill templates from the command line.",
    license='BSD',
    long_description=open('README.rst').read(),
    scripts=['bin/donkey_kong'],
    install_requires=[
        "colorama==0.2.5",
        "prettytable==0.7.2",
        "mandrill==1.0.53"
    ],
    keywords=['mandrill', 'mailchimp', 'email', 'templates', 'send'],
)