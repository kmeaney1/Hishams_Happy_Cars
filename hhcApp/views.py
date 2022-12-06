from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from .models import Car
from .forms import addCarForm
from .forms import signupForm


def index(request):
    return render(request, "index.html")


def add_car_form(request):
    if request.method == "POST":
        form = addCarForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = addCarForm()
    return render(request, "addCar-Form.html", {'form': form})


def get_car_info(request, car_vin):
    mydata = Car.objects.filter(vin=car_vin).values()
    template = loader.get_template("carProfile.html")
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def sign_up(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = signupForm()
    return render(request, "signUp-Form.html", {'signup': form})
