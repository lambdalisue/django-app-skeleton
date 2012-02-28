# vim: set fileencoding=utf-8 :
from setuptools import setup, find_packages

version = '0.1.0'

def read(filename):
    import os.path
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name="django-app-skeleton",
    version=version,
    description = "A skeleton package for Django App",
    long_description=read('README.rst'),
    classifiers = [
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',

    ],
    keywords = "django app skeleton",
    author = "Alisue",
    author_email = "lambdalisue@hashnote.net",
    url=r"https://github.com/lambdalisue/django-app-skeleton",
    download_url = r"https://github.com/lambdalisue/django-app-skeleton/tarball/master",
    license = 'MIT',
    packages = find_packages(),
    include_package_data = True,
    install_requires=[
        'distribute',
        'django>=1.3',
        'setuptools-git',
    ],
    test_suite='runtests.runtests',
    tests_require=[
        'PyYAML',
    ],
)
