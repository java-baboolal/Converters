# Generated by Django 3.2.22 on 2023-10-18 09:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurbArea',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('coordinates', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('published_date', models.DateTimeField()),
                ('last_updated_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'area',
            },
        ),
    ]
