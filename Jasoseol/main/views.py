from django.shortcuts import render, redirect
from .forms import JssForm
from .models import Jasoseol

# Create your views here.

def index(request) : 
    all_jss = Jasoseol.objects.all()
    return render(request, 'index.html', {'all_jss':all_jss})

def create(request) :
    if request.method == "POST" :
        fileed_form = JssForm(request.POST)
        if fileed_form.is_valid():
            fileed_form.save()
            return redirect('index')
    jss_form = JssForm()
    return render(request, 'create.html', {'jss_form':jss_form})