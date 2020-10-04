from django.db import migrations
import uuid


def gen_uuid(apps, schema_editor):
    Spaceship = apps.get_model('space_rangers', 'Spaceship')
    for row in Spaceship.objects.all():
        row.description = str(uuid.uuid4())
        row.save()


class Migration(migrations.Migration):

    dependencies = [
        ('space_rangers', '0002_spaceship_description'),
    ]

    operations = [
        migrations.RunPython(gen_uuid),
    ]
