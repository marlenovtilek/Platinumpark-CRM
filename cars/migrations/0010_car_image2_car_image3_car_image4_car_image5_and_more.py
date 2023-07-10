# Generated by Django 4.2 on 2023-06-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_car_image10_remove_car_image2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='cars/images', verbose_name='Фотография автомобиля с левой стороны'),
        ),
        migrations.AddField(
            model_name='car',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='cars/images', verbose_name='Фотография автомобиля с задней стороны'),
        ),
        migrations.AddField(
            model_name='car',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='cars/images', verbose_name='Фотография автомобиля с передней стороны'),
        ),
        migrations.AddField(
            model_name='car',
            name='image5',
            field=models.ImageField(blank=True, upload_to='cars/images', verbose_name='Фотография автомобиля изнутри(необязательно)'),
        ),
        migrations.AddField(
            model_name='car',
            name='image6',
            field=models.ImageField(blank=True, upload_to='cars/images', verbose_name='Фотография автомобиля изнутри(необязательно)'),
        ),
        migrations.AddField(
            model_name='car',
            name='is_busy',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='last_checking',
            field=models.DateField(blank=True, null=True, verbose_name='Последний технический осмотр'),
        ),
        migrations.AddField(
            model_name='car',
            name='passport_image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/passport_images', verbose_name='Фотография Техпаспорта'),
        ),
        migrations.AddField(
            model_name='car',
            name='price_by_day',
            field=models.CharField(max_length=20, null=True, verbose_name='Цена по суточной оплаты'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='cars/images', verbose_name='Фотография автомобиля с правой стороны'),
        ),
    ]
