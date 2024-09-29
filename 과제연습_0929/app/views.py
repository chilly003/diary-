from django.shortcuts import render,redirect
from . models import APP
from . forms import APPFORM

# Create your views here.
def index(request):
    app = APP.objects.all()
    app = APP.objects.order_by('-name')
    context = {
        'apps' : app
    }
    return render(request, 'app/index.html', context)

def create(request):
    if request.method == 'POST':
        form = APPFORM(request.POST, request.FILES)
        if form.is_valid():
            app = form.save()
            return redirect('app:detail', app.pk) #이거 디테일일 때 필요한거임 기억
    form = APPFORM()
    context = {
        'form':form
    }
    return render(request, 'app/create.html', context)

def detail(request, pk):
    app = APP.objects.get(pk=pk)
    context = {
        'app':app
    }
    return render(request, 'app/detail.html', context)

def update(request, pk):
    app = APP.objects.get(pk=pk)
    if request.method == "POST":
        form = APPFORM(request.POST, request.FILES, instance=app)
        if form.is_valid():
            app = form.save()
            return redirect('app:detail', app.pk)
    form = APPFORM(instance=app) #수정하러 갈거니까 이전 내용만 필요
    context = {
        'form': form,
        'app':app,
    }
    return render(request, 'app/update.html', context)

def delete(request, pk):
    app = APP.objects.get(pk=pk)
    if request.method == "POST":
        app.delete()
        return redirect('app:index')
    
    return redirect('app:detail', app.pk)