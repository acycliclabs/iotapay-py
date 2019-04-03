from distutils.core import setup
import os, re

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
            filepaths.extend([os.path.join(base, filename)
                              for filename in filenames])
    return {package: filepaths}


setup(
    name = 'iotapay',
    packages = ['iotapay'],
    package_data = get_package_data('iotapay'),
    python_requires = ">=3.6",
    version = get_version('iotapay'),
    description = 'Pay using IOTA',
    long_description=long_description,
    long_description_content_type='text/markdown'
    author = 'Kumar Anirudha',
    author_email = 'anirudhastark@yahoo.com',
    url = 'https://github.com/acycliclabs/iotapay-py',
    keywords = ['iotapay','payment', 'anistark', 'python', 'acyclic', 'tangle'],
    install_requires = ['PyOTA==2.0.5'],
    dependency_links = [],
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Utilities",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
