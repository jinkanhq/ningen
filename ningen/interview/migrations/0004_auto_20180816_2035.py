# Generated by Django 2.1 on 2018-08-16 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0003_auto_20180816_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='邮件地址'),
        ),
    ]
