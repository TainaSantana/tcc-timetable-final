# Generated by Django 3.0.8 on 2021-02-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professores', '0002_auto_20210204_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Ativo'), ('2', 'Inativo')], default=1, max_length=1),
        ),
    ]
