# Generated by Django 4.2.4 on 2023-09-15 18:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]