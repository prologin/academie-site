# Generated by Django 4.0.2 on 2022-05-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_alter_problem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='title',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
