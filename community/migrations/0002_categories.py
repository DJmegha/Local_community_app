# Generated by Django 4.1 on 2022-10-29 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200)),
                ('Service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.services')),
            ],
        ),
    ]
