# Generated by Django 3.0.6 on 2020-05-17 22:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0004_auto_20200517_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]