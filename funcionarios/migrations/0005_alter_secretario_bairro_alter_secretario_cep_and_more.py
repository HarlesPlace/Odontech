# Generated by Django 5.1.2 on 2024-11-23 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinicas", "0004_clinica_estado"),
        ("funcionarios", "0004_alter_dentista_bairro_alter_dentista_cep_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="secretario",
            name="bairro",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="cep",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="cidade",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="clinica",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clinicas.clinica",
            ),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="cpf",
            field=models.CharField(max_length=14, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="data_contratacao",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="estado",
            field=models.CharField(
                choices=[
                    ("AC", "Acre"),
                    ("AL", "Alagoas"),
                    ("AP", "Amapá"),
                    ("AM", "Amazonas"),
                    ("BA", "Bahia"),
                    ("CE", "Ceará"),
                    ("DF", "Distrito Federal"),
                    ("ES", "Espírito Santo"),
                    ("GO", "Goiás"),
                    ("MA", "Maranhão"),
                    ("MT", "Mato Grosso"),
                    ("MS", "Mato Grosso do Sul"),
                    ("MG", "Minas Gerais"),
                    ("PA", "Pará"),
                    ("PB", "Paraíba"),
                    ("PR", "Paraná"),
                    ("PE", "Pernambuco"),
                    ("PI", "Piauí"),
                    ("RJ", "Rio de Janeiro"),
                    ("RN", "Rio Grande do Norte"),
                    ("RS", "Rio Grande do Sul"),
                    ("RO", "Rondônia"),
                    ("RR", "Roraima"),
                    ("SC", "Santa Catarina"),
                    ("SP", "São Paulo"),
                    ("SE", "Sergipe"),
                    ("TO", "Tocantins"),
                ],
                default="SP",
                max_length=2,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="numero_residencial",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="rua",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="salario",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name="secretario",
            name="telefone",
            field=models.CharField(max_length=15, null=True),
        ),
    ]