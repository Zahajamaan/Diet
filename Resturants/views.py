from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from Resturants.models import DietType

# Create your views here.
def home_view(request):
    print (request.user)
    return HttpResponse("<h1>Welcome</h1>")
def about_view (request):
    print(request.user)
    return HttpResponse("<h1>About Us</h1>")


def index_view(request):
    items_list = DietType.objects.all()
    return render(request,'DietType/index.html',{'items':items_list})


def contact_us(request):
    print(request.user)
    return HttpResponse("<h1>Contact US</h1>")