# Generated by Django 5.0.3 on 2024-04-09 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_payments_rename_type_subscription_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='active',
            field=models.CharField(default='True', max_length=50),
        ),
        migrations.AddField(
            model_name='registration',
            name='admin',
            field=models.CharField(default='False', max_length=50),
        ),
    ]