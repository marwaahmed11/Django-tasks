from django.shortcuts import render
from django.http import HttpResponse
from .models import Car 

# Create your views here.
def pagesIndex(request):
    return HttpResponse ("Hello from pages index")

def pagesAbout(request):
    return HttpResponse ("Hello from pages about")

def renderHtml(request):
    # dic ={"user":"marwa","name":"ahmed @@@@ ali","salary":100000}
    newdic =[{"user":"ahmed","salary":100000},{"user":"omar","salary":200000}]
    dic = {"users" : newdic}
    return render(request,'pages/index.html',dic)

def renderHtml2(request):
    dic = {"user" :"hello"}
    return render(request,'pages/about.html',dic)

def viewCars(request):
    # return render(request,'pages/cars.html',{"cars":Car.objects.all()}) #=> return all elements
    #  return render(request,'pages/cars.html', {"car":Car.objects.get(name ="bmw")})  #=> get return only one element
    # return render(request,'pages/cars.html', {"cars":Car.objects.filter(id = 2)})  #filter bt3ml loop 
       return render(request,'pages/cars.html', {"cars":Car.objects.all().order_by('model').exclude(name="lancer")})
 
def task1(request):
    newdic =[{"user":"ahmed","age":20,"salary":100000},{"user":"omar","age":21,"salary":200000},{"user":"alaa","age":21,"salary":200050}]
    dic = {"users" : newdic}
    return render(request,'pages/task1.html',dic)