from django.shortcuts import render
from django.http import HttpResponse
from djmaterial import forms as frm
from djmaterial import models as mod


def index(request):
    # form = frm.OrderForm()
    form = frm.LoginForm()
    context = {'form': form,}
    return render(request, 'index.html', context)


def checkout(request):
    # form = frm.OrderForm()
    form = frm.CheckoutForm()
    context = {'form': form,}
    return render(request, 'checkout.html', context)
