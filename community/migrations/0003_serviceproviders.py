# Generated by Django 4.1 on 2022-10-29 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceProviders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_provider', models.CharField(max_length=200)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Contact_no', models.CharField(max_length=15)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='community.categories')),
            ],
        ),
    ]
