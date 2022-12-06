# Generated by Django 4.1.3 on 2022-11-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField()),
                ('email_addr', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('car_vin', models.IntegerField(db_column='car_VIN')),
            ],
            options={
                'db_table': 'wish_list',
                'managed': True,
                'unique_together': {('user_id', 'car_vin')},
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('seller_id', models.IntegerField(primary_key=True, serialize=False)),
                ('car_vin', models.IntegerField(db_column='car_VIN')),
                ('customer_id', models.IntegerField()),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sales',
                'managed': True,
                'unique_together': {('seller_id', 'car_vin', 'customer_id')},
            },
        ),
        migrations.CreateModel(
            name='Recalls',
            fields=[
                ('car_make', models.IntegerField(primary_key=True, serialize=False)),
                ('car_model', models.IntegerField()),
                ('car_year', models.IntegerField()),
                ('date', models.DateField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('is_fixed', models.IntegerField()),
            ],
            options={
                'db_table': 'recalls',
                'managed': True,
                'unique_together': {('car_make', 'car_model', 'car_year', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vin', models.IntegerField(db_column='VIN', primary_key=True, serialize=False)),
                ('make', models.CharField(blank=True, max_length=50, null=True)),
                ('model', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('drivetrain', models.CharField(blank=True, max_length=50, null=True)),
                ('body_style', models.CharField(blank=True, max_length=50, null=True)),
                ('num_doors', models.IntegerField(blank=True, null=True)),
                ('transmission', models.CharField(blank=True, max_length=50, null=True)),
                ('car_length', models.IntegerField(blank=True, null=True)),
                ('car_width', models.IntegerField(blank=True, null=True)),
                ('car_height', models.IntegerField(blank=True, null=True)),
                ('engine_specs', models.CharField(blank=True, max_length=200, null=True)),
                ('max_horsepower', models.IntegerField(blank=True, null=True)),
                ('avg_mpg', models.IntegerField(blank=True, null=True)),
                ('city_mpg', models.IntegerField(blank=True, null=True)),
                ('hwy_mpg', models.IntegerField(blank=True, null=True)),
                ('seller_id', models.IntegerField()),
            ],
            options={
                'db_table': 'car',
                'managed': True,
                'unique_together': {('vin', 'seller_id')},
            },
        ),
    ]
