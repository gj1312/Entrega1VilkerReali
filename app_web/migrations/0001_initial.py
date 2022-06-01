# Generated by Django 4.0.4 on 2022-06-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('obra_social', models.IntegerField()),
                ('codigo_os', models.IntegerField()),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Obra_social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('codigo_os', models.IntegerField()),
                ('nombre_prod', models.CharField(max_length=40)),
                ('codigo_prod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prod', models.CharField(max_length=40)),
                ('codigo_prod', models.IntegerField()),
            ],
        ),
    ]
