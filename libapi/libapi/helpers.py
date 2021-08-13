import csv
import os
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env()

from django.conf import settings
from django.contrib.auth.models import User

from api.models import Author

def create_super_user():
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = env('USERNAME')
    superuser.email = env('EMAIL')
    superuser.set_password(env('PASSWORD'))
    superuser.save()

def import_authors():

    with open(os.path.join(settings.BASE_DIR, '../data/authors.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            create_author(row['name'])


def create_author(name):
    author = Author()
    author.name = name
    author.save()
