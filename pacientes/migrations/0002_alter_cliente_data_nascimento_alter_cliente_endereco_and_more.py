# Generated by Django 5.1.2 on 2024-11-22 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinicas", "0001_initial"),
        ("pacientes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cliente",
            name="data_nascimento",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="endereco",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clinicas.endereco",
            ),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="historico_clinico",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="cliente",
            name="numero_residencial",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
