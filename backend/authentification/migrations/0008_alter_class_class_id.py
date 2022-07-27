# Generated by Django 4.0.6 on 2022-07-27 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0007_class_class_id_alter_class_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='class_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
