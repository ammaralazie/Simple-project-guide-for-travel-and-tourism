from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Featuers
def all_fetuers(request):
    #return HttpResponse("<h1>hi</h1>")
    all_feat=Featuers.objects.all()
    context={'all_feat':all_feat}
    return render(request,'all_fetuers.html',context)
def all_detail(request,slug):
    fet1=get_object_or_404(Featuers,slug=slug)
    context={'fet1':fet1}
    return render(request,'detailfetuer.html',context)

# Create your views here.
