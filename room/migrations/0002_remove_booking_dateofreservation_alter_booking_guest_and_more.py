# Generated by Django 5.0.6 on 2024-06-13 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_guest_phonenumber'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='dateOfReservation',
        ),
        migrations.AlterField(
            model_name='booking',
            name='guest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.guest'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='roomNumber',
            field=models.CharField(max_length=20),
        ),
    ]
