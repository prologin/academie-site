# Generated by Django 4.0.2 on 2022-07-12 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0007_alter_activity_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="difficulty",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (0, "trivial"),
                    (1, "easy"),
                    (2, "medium"),
                    (3, "hard"),
                    (4, "very_hard"),
                ],
                default=4,
            ),
            preserve_default=False,
        ),
    ]
