from django.db import migrations

from libapi.helpers import create_super_user


def create_user(apps, schema_editor):
    create_super_user()


class Migration(migrations.Migration):

    dependencies = [
        ('api', 'import_authors'),
    ]

    operations = [
        migrations.RunPython(create_user)
    ]
