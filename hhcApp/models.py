from django.db import models

# Create your models here.


class Car(models.Model):
    vin = models.IntegerField(db_column='VIN', primary_key=True)  # Field name made lowercase.
    make = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    drivetrain = models.CharField(max_length=50, blank=True, null=True)
    body_style = models.CharField(max_length=50, blank=True, null=True)
    num_doors = models.IntegerField(blank=True, null=True)
    transmission = models.CharField(max_length=50, blank=True, null=True)
    car_length = models.IntegerField(blank=True, null=True)
    car_width = models.IntegerField(blank=True, null=True)
    car_height = models.IntegerField(blank=True, null=True)
    engine_specs = models.CharField(max_length=200, blank=True, null=True)
    max_horsepower = models.IntegerField(blank=True, null=True)
    avg_mpg = models.IntegerField(blank=True, null=True)
    city_mpg = models.IntegerField(blank=True, null=True)
    hwy_mpg = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'car'


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email_addr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'customer'


class Recalls(models.Model):
    car_make = models.IntegerField(primary_key=True)
    car_model = models.IntegerField()
    car_year = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=200, blank=True, null=True)
    is_fixed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'recalls'
        unique_together = (('car_make', 'car_model', 'car_year', 'date'),)


class Sales(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    car_vin = models.IntegerField(db_column='car_VIN')  # Field name made lowercase.
    customer_id = models.IntegerField()
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'
        unique_together = (('seller_id', 'car_vin', 'customer_id'),)


class Seller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email_addr = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'seller'


class WishList(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    car_vin = models.IntegerField(db_column='car_VIN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wish_list'
        unique_together = (('customer_id', 'car_vin'),)

