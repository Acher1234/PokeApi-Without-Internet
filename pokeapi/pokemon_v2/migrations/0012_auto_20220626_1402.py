# Generated by Django 2.1.15 on 2022-06-26 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pokemon_v2", "0011_typeefficacypast"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemsprites",
            name="sprites",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="pokemonformsprites",
            name="sprites",
            field=models.CharField(max_length=1000),
        ),
    ]
