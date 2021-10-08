from webdev.consultas.forms import ConsultaNewForm
from webdev.consultas.models import Consulta
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ConsultaNewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('consultas:home'))
        else:
           return render(request, 'consultas:home.html',{'form':form}, status=400)
    return render(request, 'consultas/home.html')