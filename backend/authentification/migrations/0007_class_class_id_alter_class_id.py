# Generated by Django 4.0.6 on 2022-07-27 11:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0006_rename_temp_id_class_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.RemoveField(
            model_name='class',
            name='id',
        ),
        migrations.AddField(
            model_name='class',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]