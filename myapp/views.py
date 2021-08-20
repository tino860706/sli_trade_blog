from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .models import Vehicle
from .forms import MyForm


# Create your views here.
@login_required
def index(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is '':
        cars = Vehicle.objects.all()
    elif q is not None:
        cars = Vehicle.objects.filter(title__contains=q)
    context = {'cars': cars}
    return render(request, 'myapp/index.html', context)


def detail(request, slug=None):
    car = get_object_or_404(Vehicle, slug=slug)
    context = {'car': car}
    return render(request, 'myapp/detail.html', context)


def tags(request, slug=None):
    cars = Vehicle.objects.filter(tags__slug=slug)
    context = {'cars': cars}
    return render(request, 'myapp/index.html', context)


@permission_required('myapp.add_car')
def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['title'])
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    context = {'form': form}
    return render(request, 'myapp/edit.html', context)


@permission_required('myapp.change_car')
def edit(request, pk=None):
    car = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = MyForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=car)
    context = {'form': form}
    return render(request, 'myapp/edit.html', context)


@permission_required('myapp.delete_car')
def delete(request, pk=None):
    car = get_object_or_404(Vehicle, pk=pk)
    car.delete()
    return render(request, 'myapp/index.html')
