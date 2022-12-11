from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.http import HttpResponse
from django.db import connection

from .models import Car, Sales, WishList, User
from .forms import addCarForm, SearchForm, purchaseform, wishListForm, signupForm, signinForm


def index(request):
    return render(request, "index.html")

def sign_in_page(request):
    return render(request, "signInPage.html")


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


def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            qs = Car.objects

            if form.cleaned_data['vin']:
                qs = qs.filter(vin=form.cleaned_data['vin'])
            if form.cleaned_data['make']:
                qs = qs.filter(make__icontains=form.cleaned_data['make']) 

            if form.cleaned_data['min_price']:
                qs = qs.filter(price__gt=form.cleaned_data['min_price'])
            
            qs = qs.all()
            print("qs count {}".format(len(qs)))
            return render(request, "search.html", {'form':form, 'cars':qs})
    else:
        form = SearchForm()

    return render(request, "search.html", {'form': form})

def purchase(request):
    if request.method == "POST":
        form = purchaseform(request.POST)
        if form.is_valid():
            car_VIN = form.cleaned_data['car_vin']
            Sales.objects.create(
                seller_id = form.cleaned_data['seller_id'],
                car_vin = form.cleaned_data['car_vin'],
                customer_id = form.cleaned_data['customer_id'],
                date = form.cleaned_data['date']

            )
            with connection.cursor() as c:
                
        
                procedure = f"""
                CALL hhc.rmWish({car_VIN})
                """
                c.execute(procedure)
    else:
        form = purchaseform()

    return render(request, "purchase-form.html", {'form': form})

def wishlist(request):
    if request.method == "POST":
        form = wishListForm(request.POST)
        if form.is_valid():
            WishList.objects.create(
                user_id = form.cleaned_data['user_id'],
                car_VIN = form.cleaned_data['car_VIN'],

            )
    else:
        form = wishListForm()

    return render(request, "wishlist-form.html", {'form': form})

def signUp(request):
    if request.method == "POST":
        form = signupForm(request.POST)
        if form.is_valid():

            form.save()
    else:
        form = signupForm()
    return render(request, "signUp-Form.html", {'form': form})

def signIn(request):
    if request.method == "POST":
        form = signinForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = signinForm()
    return render(request, "signIn-Form.html", {'form': form})