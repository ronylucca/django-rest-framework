# Generated by Django 2.1.2 on 2018-10-29 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181029_0302'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='prioridade',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]