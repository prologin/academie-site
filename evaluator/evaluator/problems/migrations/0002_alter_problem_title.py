# Generated by Django 4.0.2 on 2022-05-20 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
