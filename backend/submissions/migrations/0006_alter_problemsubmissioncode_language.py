# Generated by Django 4.0.6 on 2022-07-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_alter_problemsubmissioncode_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemsubmissioncode',
            name='language',
            field=models.CharField(choices=[('ada', 'ada'), ('ruby', 'ruby'), ('javascript', 'javascript'), ('d', 'd'), ('java', 'java'), ('c++', 'c++'), ('c#', 'c#'), ('prolog', 'prolog'), ('pascal', 'pascal'), ('rust', 'rust'), ('python', 'python'), ('lua', 'lua'), ('haskell', 'haskell'), ('perl', 'perl'), ('scheme', 'scheme'), ('php', 'php'), ('go', 'go'), ('c', 'c'), ('ocaml', 'ocaml')], max_length=32),
        ),
    ]