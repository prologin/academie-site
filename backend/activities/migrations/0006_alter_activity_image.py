# Generated by Django 4.0.2 on 2022-06-15 08:57

import django_resized.forms
from django.db import migrations

import activities.models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0005_alter_activity_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="image",
            field=django_resized.forms.ResizedImageField(
                crop=["middle", "center"],
                force_format="JPEG",
                keep_meta=False,
                quality=75,
                size=[600, 400],
                upload_to=activities.models.upload_image,
            ),
        ),
    ]
