# Generated by Django 2.1 on 2018-08-15 14:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('body', models.TextField(verbose_name='内容')),
                ('create_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='采访日期')),
            ],
            options={
                'verbose_name': '采访稿',
                'verbose_name_plural': '采访稿',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('vendor', models.CharField(max_length=32, verbose_name='厂商')),
                ('description', models.TextField(verbose_name='描述')),
                ('link', models.URLField(verbose_name='链接')),
            ],
            options={
                'verbose_name': '物品',
                'verbose_name_plural': '物品',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='称谓')),
                ('title', models.CharField(blank=True, max_length=32, verbose_name='头衔')),
                ('avatar', models.ImageField(upload_to='avatars', verbose_name='头像')),
                ('company', models.CharField(blank=True, max_length=32, verbose_name='服务处所')),
                ('education', models.CharField(blank=True, max_length=32, verbose_name='毕业院校')),
            ],
            options={
                'verbose_name': '人物',
                'verbose_name_plural': '人物',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='interview',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Person', verbose_name='人物'),
        ),
        migrations.AddField(
            model_name='interview',
            name='tags',
            field=models.ManyToManyField(to='interview.Tag', verbose_name='标签'),
        ),
    ]
