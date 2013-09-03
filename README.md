My django project template + Bootstrap 3

Working Environment with virtualenv
===================================

    $ mkvirtualenv project_name

Installing Django
=================

    $ pip install django

Creating project
================

    $ django-admin.py startproject --template=https://github.com/proft/django-project-tpl/archive/master.tar.gz --extension=py,html --name=.venv project_name

Installation of Dependencies
=============================

In development::

    $ pip install -r requirements/local.txt

For production::

    $ pip install -r requirements.txt
