# Generated by Django 4.0.6 on 2022-07-22 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problem_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='published',
        ),
    ]
