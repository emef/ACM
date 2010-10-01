from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from acm.membership.models import *
from acm.membership.lib import *

def register(request):
    return render_to_response('membership/register.html')

def account(request):
    return HttpResponse("Account page")
