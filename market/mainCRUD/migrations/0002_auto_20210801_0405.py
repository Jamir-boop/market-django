# Generated by Django 3.2.5 on 2021-08-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCRUD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='prod_codigo',
        ),
        migrations.AddField(
            model_name='producto',
            name='prod_precio',
            field=models.FloatField(default=0.0),
        ),
    ]