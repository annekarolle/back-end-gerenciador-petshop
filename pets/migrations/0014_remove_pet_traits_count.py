# Generated by Django 4.1.3 on 2022-12-02 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0013_pet_traits_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pet",
            name="traits_count",
        ),
    ]
