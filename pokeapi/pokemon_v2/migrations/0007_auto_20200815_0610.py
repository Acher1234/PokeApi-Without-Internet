# Generated by Django 2.1.11 on 2020-08-15 05:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0006_auto_20200725_2205"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonspecies",
            name="is_legendary",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="pokemonspecies",
            name="is_mythical",
            field=models.BooleanField(default=False),
        ),
    ]
