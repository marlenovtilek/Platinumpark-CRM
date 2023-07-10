# Generated by Django 4.2 on 2023-06-12 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка автомобиля')),
                ('model', models.CharField(max_length=50, verbose_name='Модель автомобиля')),
                ('license_plate', models.CharField(blank=True, max_length=10, null=True, verbose_name='Государственный номер автомобиля')),
                ('type', models.CharField(max_length=20, verbose_name='Тип кузова')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
    ]