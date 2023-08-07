Introduction
============


.. image:: https://readthedocs.org/projects/micropython-lis3mdl/badge/?version=latest
    :target: https://micropython-lis3mdl.readthedocs.io/en/latest/
    :alt: Documentation Status


.. image:: https://img.shields.io/badge/micropython-Ok-purple.svg
    :target: https://micropython.org
    :alt: micropython

.. image:: https://img.shields.io/pypi/v/micropython-lis3mdl.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/micropython-lis3mdl

.. image:: https://static.pepy.tech/personalized-badge/micropython-lis3mdl?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/micropython-lis3mdl

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

MicroPython Driver for the ST LIS3MDL magnetometer


Installing with mip
====================
To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_LIS3MDL

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_LIS3MDL")


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_LIS3MDL/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_LIS3MDL/examples.json")


Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-lis3mdl/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-lis3mdl

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-lis3mdl

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-lis3mdl


Usage Example
=============

Take a look at the examples directory

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://micropython-lis3mdl.readthedocs.io/en/latest/>`_.
