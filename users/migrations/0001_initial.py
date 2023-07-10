# Generated by Django 4.2 on 2023-06-17 11:45

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0014_alter_car_license_plate'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(null=True, upload_to='drivers/avatars', verbose_name='Фотография водителя')),
                ('position', models.CharField(choices=[('ADMIN', 'Администратор'), ('MANAGER', 'Менеджер'), ('DRIVER', 'Водитель')], max_length=20, null=True, verbose_name='Позиция пользователя')),
                ('phone', models.CharField(max_length=50, null=True, verbose_name='Номер водителя')),
                ('address', models.CharField(max_length=256, null=True, verbose_name='Место проживания')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('rented_date', models.DateField(default=django.utils.timezone.now, verbose_name='Дата аренды')),
                ('license_category', models.CharField(max_length=10, null=True, verbose_name='Категория права')),
                ('driving_experience', models.CharField(max_length=20, null=True, verbose_name='Стаж вождения')),
                ('cash_verified', models.BooleanField(default=False, verbose_name='Верификация оплаты')),
                ('cash', models.IntegerField(default=0, verbose_name='Задолжность')),
                ('cash_prove', models.ImageField(null=True, upload_to='', verbose_name='Фотография последнего чека')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('rented_car', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.car', verbose_name='Арендованная машина')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
