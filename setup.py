from distutils.core import setup
from setuptools import find_packages

setup(
    name='mandrill-send',
    version='0.1',
    author="Jessie Frazelle",
    author_email="jessie@yhathq.com",
    url="https://github.com/yhat/mandrill-send",
    packages=find_packages(),
    description="Send mandrill templates from the command line.",
    license='BSD',
    long_description=open('README.rst').read(),
    scripts=['bin/mandrill_send'],
    install_requires=[
        "colorama==0.2.5",
        "prettytable==0.7.2"
    ],
    keywords=['mandrill', 'mailchimp', 'email', 'templates', 'send'],
)