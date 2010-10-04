from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from acm.membership.models import *
from acm.membership.lib import *


def register(request):
	request.session.clear()
	if request.method == "POST":
		#match re patterns with form fields
		pattern_names = [
			(r'[wW]{0,1}\d{8}', ['username']),
			(r'[a-zA-Z\s]+', ['fname', 'lname']),
			(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}', ['email']),
		]

		#validate form using mapping above
		errors = validate(request.POST, pattern_names)

		#make sure user doesn't exist
		if len(Member.objects.filter(user__username=request.POST['username'])) > 0:
			errors['error_message'] = "This WNumber is already registered."

		#dict holding current POST values
		c = build_context(request.POST, ['username', 'fname', 'lname', 'email'])
		
		if errors != {}:
			#inject errors into context and return to form
			c.update(errors)
			if 'error_message' not in c:
				c['error_message'] = "There seems to be any error in a field below, please try again."
			return render_page(request, 'membership/register.html', c)
		else:
			#store form values in session and continue to payment page
			request.session.update(c)
			return redirect('acm.membership.views.payment')
	else:
		#get request
		return render_page(request, 'membership/register.html')

def payment(request):
	return HttpResponse("hey")

@login_required
def account(request):
    return HttpResponse("Account page")

def login(request):
	c = {}
	#set next url if available
	if "next" in request.REQUEST:
		c["next"] = request.REQUEST["next"]
	
	#try to authenticate if user/password in POST
	if request.method == "POST" and "username" in request.POST and "password" in request.POST:
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(username=username, password=password)
		if user is not None:
			auth_login(request, user)
			if "next" in c:
				return redirect(c["next"])
			else:
				return redirect("acm.membership.views.account")
		else:
			c['username'] = username
			c['error'] = "Invalid wnumber/password combo, please try again"
			return render_page(request, "membership/login.html", c)
	#anything else should return login page
	else:
		return render_page(request, "membership/login.html", c)

def logout(request):
	auth_logout(request)
	return render_page(request, "membership/logout.html")
