from django.shortcuts import render
from .forms import datosForm
from django.shortcuts import redirect
from fundacion.models import datos

def home(request):
    datoss= datos.objects.all()
    return render(request, "home.html", {"datoss":datoss})  

def registro(request):
     if request.method == 'POST': 
        form = datosForm(request.POST)
     
        if form.is_valid():
         form.save()
         return redirect("/")
     
     else: form = datosForm() 
     context = {'form': form}   
     return render(request, "register.html", context)
   

def nosotros(request):
    return render(request, "nosotros.html")

def date(request):
    return render(request, "index.html")   