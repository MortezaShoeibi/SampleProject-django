# Generated by Django 4.0.5 on 2022-06-16 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_aboutme_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AboutMe',
            new_name='Foreword',
        ),
    ]