# Generated by Django 4.1.3 on 2022-12-10 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hhcApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlist',
            old_name='car_vin',
            new_name='car_VIN',
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('user_id', 'car_VIN')},
        ),
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['make', 'model', 'year'], name='car_make_aa1680_idx'),
        ),
    ]
