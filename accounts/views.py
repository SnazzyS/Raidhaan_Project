from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm


def dashboard(request):
    orders = Order.objects.all()

    context = {'orders':orders}

    return render(request, 'accounts/dashboard.html', context)


def orderform(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form':form}
    return render(request, 'accounts/add_order.html', context)

