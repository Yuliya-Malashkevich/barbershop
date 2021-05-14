# Generated by Django 3.2.1 on 2021-05-07 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_servicesforchildren_servicesformen'),
    ]

    operations = [
        migrations.CreateModel(
            name='CosmetologyServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название услуги')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Цены',
            },
        ),
        migrations.CreateModel(
            name='ManicurePedicure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название услуги')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
            ],
            options={
                'verbose_name_plural': 'Цены',
            },
        ),
    ]