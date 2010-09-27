from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from acm.cabinet.models import *
from decimal import *
import simplejson

def order(request):
	items = Item.objects.all()
	return render_to_response('cabinet/order.html', {'items': items});

def add_credit(request):
	return render_to_response('cabinet/add_credit.html', {'message': 'matt'});

def suggest(request):
	return render_to_response('cabinet/suggest.html', {'message': 'matt'});

def checkout(request):
	if request.method == "POST" and "data" in request.POST and "wnumber" in request.POST:
		c = {}
		wnumber = request.POST['wnumber']
		print wnumber
		try:
			c['profile'] = UserProfile.objects.get(user__username=wnumber)
		except UserProfile.DoesNotExist:
			u, created = User.objects.get_or_create(username=wnumber)
			c['profile'] = UserProfile.objects.create(user=u, credit=Decimal('0.00'))
		c['data'] = simplejson.loads(request.POST['data'])
		return render_to_response('cabinet/checkout.html', c)
	else:
		raise Http404
