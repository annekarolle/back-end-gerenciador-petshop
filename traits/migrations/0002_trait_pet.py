# Generated by Django 4.1.3 on 2022-11-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_remove_pet_traits"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="pet",
            field=models.ManyToManyField(to="pets.pet"),
        ),
    ]
