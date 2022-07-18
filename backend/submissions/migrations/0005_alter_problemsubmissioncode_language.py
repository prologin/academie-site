# Generated by Django 4.0.2 on 2022-07-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("submissions", "0004_alter_problemsubmissioncode_language"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problemsubmissioncode",
            name="language",
            field=models.CharField(
                choices=[
                    ("lua", "lua"),
                    ("ruby", "ruby"),
                    ("perl", "perl"),
                    ("ada", "ada"),
                    ("scheme", "scheme"),
                    ("pascal", "pascal"),
                    ("c#", "c#"),
                    ("c++", "c++"),
                    ("javascript", "javascript"),
                    ("prolog", "prolog"),
                    ("haskell", "haskell"),
                    ("rust", "rust"),
                    ("d", "d"),
                    ("go", "go"),
                    ("java", "java"),
                    ("ocaml", "ocaml"),
                    ("php", "php"),
                    ("c", "c"),
                    ("python", "python"),
                ],
                max_length=32,
            ),
        ),
    ]
