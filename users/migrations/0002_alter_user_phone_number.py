# Generated by Django 4.2.7 on 2023-11-25 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.DecimalField(decimal_places=0, max_digits=11, unique=True),
        ),
    ]