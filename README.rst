hebrew_names
===============

Random Hebrew name generator


Installation
------------

The script is [`available on PyPI`](TODO).  To install with pip::

    pip install hebrew-names


Usage
-----

Hebrew Names can be used as a command line utility or imported as a Python package.

Command Line Usage
~~~~~~~~~~~~~~~~~~
To use the script from the command line:

.. code-block:: bash

    $ hebrew-names
    צבי כהן

Python Package Usage
~~~~~~~~~~~~~~~~~~~~
Here are examples of all current features:

.. code-block:: pycon

    >>> import hebrew_names
    >>> hebrew_names.get_first_name('jew', 'female')
    'יעל'
    >>> hebrew_names.get_first_name('jew', 'female')
    'תמר'
    >>> hebrew_names.get_first_name('jew', 'male')
    'אהרון'
    >>> hebrew_names.get_first_name()
    'מקסים'
    >>> hebrew_names.get_first_name()
    'נור'
    >>> hebrew_names.get_first_name('muslim', 'male')
    "מג'די"
    >>> hebrew_names.get_first_name('muslim', 'male')
    'מוחמד'
    >>> hebrew_names.get_first_name('druze', 'male')
    'ריאן'
    >>> hebrew_names.get_first_name('other', 'male')
    'אנטוני'


License
-------

This project is released under an [`MIT License`](http://th.mit-license.org/2013).

Data in the following files are public domain (derived from Israel's Central Bureau of Statistics 1948-2021 data):

- dist.jew.male.first
- dist.jew.female.first
- dist.jew.last
- dist.muslim.male.first
- dist.muslim.female.first
- dist.muslim.last
- dist.christian.male.first
- dist.christian.female.first
- dist.christian.last
- dist.druze.male.first
- dist.druze.female.first
- dist.druze.last
- dist.other.male.first
- dist.other.female.first
- dist.other.last
