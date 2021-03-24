from django.shortcuts import render, redirect
from .models import Dojo, Ninja
def index(request):
    context = {
        "all_ninjas": Ninja.objects.all(),
        "all_dojos" : Dojo.objects.all()
    }
    return render(request, "index.html", context) 

def processDojo(request):
    dojoname = request.POST['dojoName']
    city = request.POST['city']
    state = request.POST['state']
    
    new_dojo = Dojo.objects.create(name = dojoname, city = city, state = state)
    return redirect("/")
def processNinja(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    dojo = Dojo.objects.get(id=request.POST['dojos'])
    
    new_ninja = Ninja.objects.create(dojo = dojo, first_name = first_name, last_name = last_name)
    return redirect("/")
