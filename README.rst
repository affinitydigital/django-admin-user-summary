=============================
Django Admin User Summary
=============================

.. image:: https://badge.fury.io/py/django-admin-user-summary.svg
    :target: https://badge.fury.io/py/django-admin-user-summary

.. image:: https://travis-ci.org/affinitydigital/django-admin-user-summary.svg?branch=master
    :target: https://travis-ci.org/affinitydigital/django-admin-user-summary

.. image:: https://codecov.io/gh/affinitydigital/django-admin-user-summary/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/affinitydigital/django-admin-user-summary

Pluggable Django admin app shows user registration summary.

Documentation
-------------

The full documentation is at https://django-admin-user-summary.readthedocs.io.

Quickstart
----------

Install Django Admin User Summary::

    pip install django-admin-user-summary

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_admin_user_summary',
        ...
    )


Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
