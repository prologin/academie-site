# Generated by Django 4.0.6 on 2022-07-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0008_alter_problemsubmissioncode_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemsubmissioncode',
            name='language',
            field=models.CharField(choices=[('pascal', 'pascal'), ('ruby', 'ruby'), ('ada', 'ada'), ('javascript', 'javascript'), ('ocaml', 'ocaml'), ('java', 'java'), ('c', 'c'), ('perl', 'perl'), ('rust', 'rust'), ('python', 'python'), ('php', 'php'), ('go', 'go'), ('c#', 'c#'), ('c++', 'c++'), ('d', 'd'), ('lua', 'lua'), ('prolog', 'prolog'), ('haskell', 'haskell'), ('scheme', 'scheme')], max_length=32),
        ),
    ]
