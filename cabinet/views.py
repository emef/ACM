from django.core.context_processors import csrf
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from acm.cabinet.models import *
from acm.cabinet.lib import *
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
	#bad request...
	if not ("cart" in request.session and "profile" in request.session):
		raise Http404
	#redirected from 'order', should have order info in session
	elif request.method == "GET":
		c = build_checkout_context(request)
		return render_to_response('cabinet/checkout.html', c)
	#post request, do some validation and finalize the purchase
	else:
		profile = request.session['profile']
		cart = request.session['cart']
		password = request.POST.get('password', '')
		#user has a password setup, and it did not match
		if profile.user.has_usable_password() and not profile.user.password == password:
			c = build_checkout_context(request)
			c['error'] = "Incorrect password for this account"
			return render_to_response('cabinet/checkout.html', c)
		#successful order, call make_purchase
		else:
			request.session.clear()
			request.session['receipt'] = make_purchase(profile, cart)
			return redirect('acm.cabinet.views.receipt')

def receipt(request):
	#just came from checkout, display receipt information and blow up the reciept
	if request.method == 'GET' and 'receipt' in request.session:
		receipt = request.session['receipt']
		request.session.clear()
		return render_to_response('cabinet/receipt.html', { 'receipt': receipt })
	#why the hell are you here?
	else:
		raise Http404
			
			

