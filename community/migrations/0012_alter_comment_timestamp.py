# Generated by Django 4.1 on 2022-10-31 17:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0011_alter_comment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 17, 30, 35, 484606, tzinfo=datetime.timezone.utc)),
        ),
    ]