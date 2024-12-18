# Generated by Django 5.1.2 on 2024-12-01 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultas", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="status",
            field=models.CharField(
                choices=[
                    ("agendada", "Agendada"),
                    ("suspensa", "Suspensa"),
                    ("concluída", "Concluída"),
                ],
                default="agendada",
                max_length=20,
            ),
        ),
    ]
