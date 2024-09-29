from django.shortcuts import render, redirect
from . models import APP
from . form import APPFORM

# Create your views here.

def index(request):
    app = APP.objects.all()
    context = {
        'apps' : app
    }
    return render(request, 'app/index.html', context)

def create(request):
    if request.method == "POST":
        form = APPFORM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    form = APPFORM()
    context = {
        'form' : form
    }
    return render(request, 'app/create.html', context)

def detail(request, pk):
    app = APP.objects.get(pk=pk)
    context = {
        'app':app,
    }
    return render(request, 'app/detail.html', context)

def update(request, pk):
    app = APP.objects.get(pk=pk)
    if request.method == "PSOT":
        form = APPFORM(request.POST, instance=app)
        if form.is_valid():
            app = form.save()
            return redirect('app:detail', app.pk)
    form = APPFORM(instance=app)
    context = {
        'form':form,
        'app': app,
    }
    return render(request, 'app/update.html', context)

def delete(request, pk):
    app = APP.objects.get(pk=pk)
    if request.method == "POST":
        app.delete()
        return redirect('app:index')
    else:
        return redirect('app:detail', app.pk)