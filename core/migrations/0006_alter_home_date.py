# Generated by Django 4.2.1 on 2023-07-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_account_date_home_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
