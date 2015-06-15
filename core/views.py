from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect


def index(request):
  return render(request, 'core/index.html', {}) 


def contactus(request):
	return render(request, 'core/contactus.html', {})	

def products(request):
	return render(request,'core/products.html',{})
def product_detail(request):
	return render(request,'core/product_detail.html',{})	

# Create your views here.
