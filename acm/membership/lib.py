from acm.membership.models import *
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
import re

def render_page(request, template, context=None):
	if context is None:
		context = {}
	context.update(csrf(request))
	if request.user.is_authenticated():
		context['user'] = request.user
	elif "user" in context:
		del context['user']
	return render_to_response(template, context)

def validate(form, patterns_names):
	errors = {}
	for p, names in patterns_names:
		p = re.compile(p)
		for name in names:
			if name not in form or p.match(form[name]) is None:
				errors[name+'_error'] = 'validation_error'
	return errors

def build_context(form, names):
	c = {}
	for name in names:
		if name in form:
			c[name] = form[name]
	return c

#assumes form info has been validated
def register(form):
	username = re.match(r"[wW]{0,1}(\d{8})", form['username']).group(1)
	fname = form['fname']
	lname = form['lname']
	email = form['email']
	try:
		user = User.objects.get(username=username)
		member = Member.objects.get(user__username=username)
	except User.DoesNotExist:
		pass
	except Member.DoesNotExist:
		pass
