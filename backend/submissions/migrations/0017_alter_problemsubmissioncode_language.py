# Generated by Django 4.0.6 on 2022-07-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0016_alter_problemsubmissioncode_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemsubmissioncode',
            name='language',
            field=models.CharField(choices=[('scheme', 'scheme'), ('java', 'java'), ('perl', 'perl'), ('ocaml', 'ocaml'), ('javascript', 'javascript'), ('haskell', 'haskell'), ('ada', 'ada'), ('c#', 'c#'), ('rust', 'rust'), ('d', 'd'), ('python', 'python'), ('pascal', 'pascal'), ('ruby', 'ruby'), ('c++', 'c++'), ('php', 'php'), ('go', 'go'), ('prolog', 'prolog'), ('c', 'c'), ('lua', 'lua')], max_length=32),
        ),
    ]
