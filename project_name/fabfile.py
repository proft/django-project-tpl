import os
import sys

from fabric.contrib import django
from fabric.api import *
from fabric.colors import green

env.hosts = ['']
env.code_dir = '/home/www/{{ project_name }}/www'
env.tmp_dir = '/tmp'
env.db_name = '{{ project_name }}'


def remote_pull():
    print(green('PULLING ...'))
    with cd(env.code_dir):
        run('sudo -uwww git pull')


def remote_reload():
    print(green('RELOADING ...'))
    with cd(env.code_dir):
        run('sudo supervisorctl restart {{ project_name }}')


def manage_py(command):
    with cd(env.code_dir):
        run('python manage.py %s' % command)


def migrate(app=''):
    print(green('MIGRATING ...'))
    manage_py('migrate %s' % app)


def collect_static():
    print(green('COLLECTING STATIC ...'))
    local('python manage.py collectstatic --noinput')


def git_stage(message):
    print(green('STAGING ...'))
    local('git add .')
    local('git commit -a -m "%s"' % message)
    local('git push')


def git_stage_with_static(message):
    print(green('STAGING ...'))
    local('git add .')
    local('git add ../static/')
    local('git commit -a -m "%s"' % message)
    local('git push')

#########
# Deploy
#########


@task(alias='ird')
def import_remote_db():
    print(green('IMPORTING REMOTE DB ...'))

    sys.path.append(os.path.dirname(__file__))
    django.settings_module('{{ project_name }}.settings')
    from django.conf import settings

    engine = settings.DATABASES['default']['ENGINE'].split('.')[-1]

    if engine == 'mysql':
        with cd(env.tmp_dir):
            db_file = 'mysql-%s.gz' % env.db_name
            run('mysqldump -uadmin -p %s | gzip -9 > %s' % (env.db_name, db_file))
            get(db_file, '../')
            run('rm %s' % db_file)
            local('gunzip ../%s' % db_file)
            local('mysql -uroot -p %s < %s' % (env.db_name, '../%s' % db_file.replace('.gz', '')))
    elif engine == 'postgresql_psycopg2':
        with cd(env.tmp_dir):
            db_file = 'psql-%s.gz' % env.db_name
            run('pg_dump -O -F p -c -U postgres %s | gzip -9 > %s' % (env.db_name, db_file))
            get(db_file, '../../')
            run('rm %s' % db_file)
            local('gunzip ../../%s' % db_file)
            local('psql -U postgres -d %s -f %s' % (env.db_name, '../../%s' % db_file.replace('.gz', '')))


@task(alias='df')
def deploy_full(msg=""):
    collect_static()
    git_stage_with_static(msg)
    remote_pull()
    migrate()
    remote_reload()


@task(alias='ds')
def deploy_simple(msg=""):
    git_stage(msg)
    remote_pull()
    remote_reload()


@task(alias='dh')
def deploy_html(msg=""):
    collect_static()
    git_stage(msg)
    remote_pull()

