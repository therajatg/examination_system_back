# Generated by Django 4.1.3 on 2022-11-27 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='Password',
            new_name='password',
        ),
    ]
