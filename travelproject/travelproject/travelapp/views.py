from django.http import HttpResponse
from django.shortcuts import render
from.models import Place
from.models import Team

def demo(request):
    obj=Place.objects.all()
    objt=Team.objects.all()
    return render(request,"index.html",{'result':obj,'results':objt})
