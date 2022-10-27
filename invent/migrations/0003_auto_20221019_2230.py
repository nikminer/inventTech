# Generated by Django 3.2.16 on 2022-10-19 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invent', '0002_auto_20221019_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech',
            name='inventNumber',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='Инвентаризационный номер'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='serialNumber',
            field=models.CharField(max_length=100, verbose_name='Серийный номер'),
        ),
    ]
