My django project template + Bootstrap 3.

Working Environment

    $ mkvirtualenv project_name

Installing Django

    $ pip install django

Creating project

    $ django-admin.py startproject --template=https://github.com/proft/django-project-tpl/archive/master.tar.gz --extension=py,html,tpl --name=.venv project_name

Installation of dependencies for development:

    $ pip install -r requirements/local.txt

Installation of dependencies for production:

    $ pip install -r requirements.txt
