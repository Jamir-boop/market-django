# Generated by Django 3.2.5 on 2021-08-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_nombre', models.CharField(max_length=500)),
                ('prod_codigo', models.CharField(max_length=6)),
                ('prod_categoria', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario_nombre', models.CharField(max_length=250)),
                ('usuario_estado', models.BooleanField()),
                ('usuario_correo', models.CharField(max_length=250)),
                ('usuario_clave', models.CharField(max_length=250)),
                ('usuario_fecha', models.DateField()),
            ],
        ),
    ]