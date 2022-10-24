import hebrew_names
from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as changes_file:
    changes = changes_file.read()

with open('CONTRIBUTING.rst') as contributing_file:
    contributing = contributing_file.read()


setup(
    name=hebrew_names.__title__,
    version=hebrew_names.__version__,
    author=hebrew_names.__author__,
    url="https://github.com/alumag/hebrew-hebrew_names",
    description="Generate random Hebrew hebrew_names",
    long_description='\n\n'.join((
        readme,
        changes,
        contributing,
    )),
    license=hebrew_names.__license__,
    packages=find_packages(),
    package_data={'hebrew_names': ['dist.*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hebrew_names = hebrew_names.main:main',
        ],
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='test_names',
)
