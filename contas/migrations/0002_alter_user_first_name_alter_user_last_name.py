# Generated by Django 5.1.2 on 2024-11-22 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contas", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=150),
        ),
    ]