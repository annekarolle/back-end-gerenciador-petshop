# Generated by Django 4.1.3 on 2022-11-29 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_remove_group_pet_group_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='pet',
        ),
    ]
