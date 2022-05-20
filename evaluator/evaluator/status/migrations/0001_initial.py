# Generated by Django 4.0.2 on 2022-05-18 21:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryTaskStatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('model_type', models.CharField(choices=[('ACTIVITY', 'Activity'), ('SUBMISSION', 'Submission'), ('PROBLEM', 'Problem')], max_length=64)),
                ('model_id', models.UUIDField()),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('DONE', 'Done'), ('ERROR', 'Error')], default='PENDING', max_length=64)),
                ('info', models.TextField(blank=True, default='')),
            ],
            options={
                'managed': False,
            },
        ),
    ]