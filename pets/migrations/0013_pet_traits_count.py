# Generated by Django 4.1.3 on 2022-12-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0012_alter_pet_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="traits_count",
            field=models.IntegerField(default=0),
        ),
    ]
