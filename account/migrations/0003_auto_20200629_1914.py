# Generated by Django 3.0.7 on 2020-06-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200629_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseaccount',
            name='staff_id',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]