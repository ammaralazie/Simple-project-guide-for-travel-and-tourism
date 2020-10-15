from django.shortcuts import render,redirect,get_object_or_404
from .models import Contry
# Create your views here.
def all_contry(request):
    file=Contry.objects.all()
    context={'file':file}
    return render(request,'home.html',context)

def detail_contry(request,slug):
    file=get_object_or_404(Contry,slug=slug)
    context={'file':file}
    return render(request,'detail.html',context)
def image_contry(request,slug):
    imgs=get_object_or_404(Contry,slug=slug)
    context={'imgs':imgs}
    return render(request,'images.html',context)
def history_contry(request,slug):
    hi=get_object_or_404(Contry,slug=slug)
    context={'hi':hi}
    return render(request,'hestory.html',context)
def wather_geograohy(request,slug):
    wage=get_object_or_404(Contry,slug=slug)
    context={'wage':wage}
    return render(request,'wather.html',context)

def Image_food(request,slug):
    I=get_object_or_404(Contry,slug=slug)
    context={'I':I}
    return render(request,'Image_food.html',context)
