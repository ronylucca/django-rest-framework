# Generated by Django 2.1.2 on 2018-10-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181029_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horariofuncionamento',
            name='dia_da_semana',
            field=models.IntegerField(choices=[(1, 'Segunda'), (2, 'Terça'), (3, 'Quarta'), (4, 'Quinta'), (5, 'Sexta'), (6, 'Sábado'), (7, 'Domingo')]),
        ),
    ]
