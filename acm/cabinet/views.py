from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from acm.cabinet.models import *

def order(request):
	items = Item.objects.all()
	return render_to_response('cabinet/order.html', {'items': items});

def add_credit(request):
	return render_to_response('cabinet/add_credit.html', {'message': 'matt'});

def suggest(request):
	return render_to_response('cabinet/suggest.html', {'message': 'matt'});

def checkout(request):
	return HttpResponse("HEY");
