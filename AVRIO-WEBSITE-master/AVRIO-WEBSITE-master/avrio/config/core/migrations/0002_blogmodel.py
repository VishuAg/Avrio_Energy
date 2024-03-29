# Generated by Django 2.2.1 on 2019-07-05 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogmodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('paragraph', models.CharField(max_length=2000)),
                ('url', models.URLField(unique=True)),
                ('date', models.CharField(max_length=50)),
                ('button', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
