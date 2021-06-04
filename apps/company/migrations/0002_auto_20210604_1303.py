# Generated by Django 3.2.4 on 2021-06-04 16:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='data_cadastro',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.BooleanField(choices=[(0, 'Inativo'), (1, 'Ativo')], default=1),
        ),
    ]