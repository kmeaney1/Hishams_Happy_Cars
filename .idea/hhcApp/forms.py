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

class SearchForm(forms.Form):
    vin = forms.IntegerField(label="VIN", required=False)
    make = forms.CharField(required=False)
    model = forms.CharField(required=False)
    year = forms.IntegerField(required=False)
    min_price = forms.IntegerField(label="Min price", required=False)
    max_price = forms.IntegerField(label="Max price", required=False)

class purchaseform(forms.Form):
    seller_id = forms.IntegerField(label="seller_id", required=True)
    car_vin = forms.IntegerField(label="VIN", required=True)
    customer_id = forms.IntegerField(label="customer_id", required=True)
    date = forms.DateField(label="date",required=True)

class wishListForm(forms.Form):
    user_id = forms.IntegerField(label="user_id", required=True)
    car_VIN = forms.IntegerField(label="car_VIN", required=True)
   

