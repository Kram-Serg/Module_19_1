# Generated by Django 4.2.17 on 2025-01-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0011_alter_buyer_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='game',
            name='size',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
