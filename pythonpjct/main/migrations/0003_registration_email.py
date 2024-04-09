# Generated by Django 5.0.3 on 2024-04-07 14:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]