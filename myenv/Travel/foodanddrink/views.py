from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Food
from .models import Drink

def all_food_and_drink(request):
    all_food=Food.objects.all()
    all_drink=Drink.objects.all()
    context={'all_food':all_food,'all_drink':all_drink}
    return render(request,'all_food.html',context)
##########################

def det_food(request,slug):
    if slug=='budapest-food-drink-guide-10-things-to-try-in-budapest' or slug=='merry-christmas' or slug=='home-food-tenerife-food-drink-guide-10-things-to-try-in-tenerife' or slug=='rome-food-and-drink-guide-10-things-to-try-in-rome-italy' or slug=='athens-food-drink-guide-10-things-to-try-in-athens-greece' :

        all_food=get_object_or_404(Food,slug=slug)
        context={'all_food':all_food}
    else:
        all_drink=get_object_or_404(Drink,slug=slug)
        context={'all_drink':all_drink}
    return render(request,'detail_food.html',context)

###################
