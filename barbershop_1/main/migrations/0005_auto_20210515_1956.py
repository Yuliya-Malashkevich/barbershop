# Generated by Django 3.2.1 on 2021-05-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_cosmetologyservices_manicurepedicure'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCertificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название услуги')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cosmetologyservices',
            options={'verbose_name_plural': 'Косметологические услуги'},
        ),
        migrations.AlterModelOptions(
            name='manicurepedicure',
            options={'verbose_name_plural': 'Маникюр-Педикюр'},
        ),
        migrations.AlterModelOptions(
            name='servicesforchildren',
            options={'verbose_name_plural': 'Услуги для детей '},
        ),
        migrations.AlterModelOptions(
            name='servicesformen',
            options={'verbose_name_plural': 'Услуги для мужчин'},
        ),
        migrations.AlterModelOptions(
            name='servicesforwomen',
            options={'verbose_name_plural': 'Услуги для женщин'},
        ),
    ]