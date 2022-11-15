from django import forms

from .models import Car


class addCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["vin", "make", "model", "year", "price",
                  "drivetrain", "body_style", "num_doors", "transmission",
                  "car_length", "car_width", "car_height", "engine_specs", "max_horsepower",
                  "avg_mpg", "city_mpg", "hwy_mpg", "seller_id"]
        labels = {'vin': "VIN", 'make': "Make", 'model': "Model", 'year': "Year", 'price': "Price",
                  'drivetrain': "Drivetrain", 'body_style': "Body Style", 'num_doors': "Number of Doors",
                  'transmission': "Transmission", 'car_length': "Length", 'car_width': "Width", 'car_height': "Height",
                  'engine_specs': "Engine Specifications", 'max_horsepower': "Max Horsepower",
                  'avg_mpg': "Average MPG", 'city_mpg': "City MPG", 'hwy_mpg': "Highway MPG",
                  'seller_id': "Your User ID"}
