# Generated by Django 3.1.7 on 2021-03-09 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20210309_0856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='user',
            new_name='owner',
        ),
    ]
