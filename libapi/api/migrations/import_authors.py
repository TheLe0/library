from django.db import migrations

from libapi.helpers import import_authors


def create_authors(apps, schema_editor):
    import_authors()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_authors)
    ]
