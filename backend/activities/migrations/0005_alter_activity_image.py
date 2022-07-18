# Generated by Django 4.0.2 on 2022-06-15 08:46

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0004_alter_activity_image"),
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
                upload_to="./uploads/images/activities/",
            ),
        ),
    ]
