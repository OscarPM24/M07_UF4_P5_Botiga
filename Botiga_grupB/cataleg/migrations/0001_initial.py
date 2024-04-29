# Generated by Django 5.0.3 on 2024-04-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('marca', models.CharField(max_length=30)),
                ('preu', models.FloatField(default=0)),
                ('estoc', models.IntegerField(default=0)),
                ('gama', models.CharField(max_length=30)),
                ('pes', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Cataleg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productes', models.ManyToManyField(to='cataleg.producte')),
            ],
        ),
    ]