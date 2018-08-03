# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
import MySQLdb
from django.http import HttpResponseRedirect


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ntu(request):
    param={}
    url='/static/ntu/login/index.html'
    return HttpResponseRedirect(url)


def home(request):
    param={}
    return render_to_response('home.html',param)

def entre(request):
    param={}
    return render_to_response('web-project.html',param)

def experience(request):
    param={}
    return render_to_response('experience.html',param)

def volunteer(request):
    param={}
    return render_to_response('volunteer.html',param)

def contact(request):
    param={}
    return render_to_response('contact.html',param)

def story(request):
    param={}
    return render_to_response('story.html',param)

def profile(request):
    param={}
    return redirect('https://www.linkedin.com/in/dan-phan-1349307b/')
