from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from acm.cabinet.models import *
from acm.cabinet.lib import get_profile, cart_total, make_purchase
import simplejson as json

def order(request):
	request.session.clear()
	if request.method == "GET":
		c = {}
		c['items'] = Item.objects.all()
		if "cart" in request.session:
			c['cart'] = json.dumps(request.session['cart'])
			c['total'] = request.session['total']
		return render_to_response('cabinet/order.html', c)
	elif request.method == "POST" and "data" in request.POST and "wnumber" in request.POST:
		wnumber = request.POST['wnumber']
		cart = json.loads(request.POST['data'])
		request.session.set_expiry(0)
		request.session['profile'] = get_profile(wnumber)
		request.session['cart'] = cart
		request.session['total'] = cart_total(cart)
		return redirect('acm.cabinet.views.checkout')
	else:
		raise Http404

def add_credit(request):
	return render_to_response('cabinet/add_credit.html')

def suggest(request):
	return render_to_response('cabinet/suggest.html')

def checkout(request):
	def buildContext():
		c = {}
		c['profile'] = request.session['profile']
		c['cart'] = request.session['cart']
		c['total'] = request.session['total']
		c['can_purchase'] = c['profile'].credit >= c['total']
		return c

	if not ("cart" in request.session and "profile" in request.session):
		raise Http404
	elif request.method == "GET":
		c = buildContext()
		return render_to_response('cabinet/checkout.html', c)
	else:
		profile = request.session['profile']
		cart = request.session['cart']
		password = request.session.get('password', '')
		if profile.user.has_usable_password() and (not profile.user.check_password(password)):
			print profile.user
			c = buildContext()
			c['error'] = "Incorrect password for this account"
			return render_to_response('cabinet/checkout.html', c)
		else:
			request.session.clear()
			request.session['receipt'] = make_purchase(profile, cart)
			return redirect('acm.cabinet.views.receipt')

def receipt(request):
	return HttpResponse("hey")
			
			
			

