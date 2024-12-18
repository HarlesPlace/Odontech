# Generated by Django 5.1.2 on 2024-11-21 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("consultas", "0001_initial"),
        ("funcionarios", "0001_initial"),
        ("pacientes", "0001_initial"),
        ("procedimentos", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="consulta",
            name="dentista",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="funcionarios.dentista"
            ),
        ),
        migrations.AddField(
            model_name="consulta",
            name="paciente",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="pacientes.cliente"
            ),
        ),
        migrations.AddField(
            model_name="consulta",
            name="procedimentos",
            field=models.ManyToManyField(to="procedimentos.procedimento"),
        ),
        migrations.AddField(
            model_name="restricao",
            name="dentista",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="funcionarios.dentista"
            ),
        ),
    ]
