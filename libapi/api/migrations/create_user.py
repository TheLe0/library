from django.db import migrations, models
import django.db.models.deletion

from libapi.helpers import create_super_user

def create_user(apps, schema_editor):
    pass
	### create_super_user()


class Migration(migrations.Migration):

    dependencies = [
        ('api', 'import_authors'),
    ]

    operations = [
        migrations.RunPython(create_user)
    ]
