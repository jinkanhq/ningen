# Generated by Django 2.1 on 2018-08-16 12:35

from django.db import migrations
import uuid


def fill_fake_email(apps, schema_editor):
    Person = apps.get_model('interview', 'Person')
    for person in Person.objects.all():
        person.email = str(uuid.uuid4()) + '@example.com'
        person.save(update_fields=['email'])


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20180816_2032'),
    ]

    operations = [
        migrations.RunPython(fill_fake_email, reverse_code=migrations.RunPython.noop)
    ]
