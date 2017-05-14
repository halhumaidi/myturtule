from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# from django.contrib.sites import requests

from django.shortcuts import render, redirect

from RA.admin import *

import requests

from RA.forms import SigninForm


def signin(request):

    if request.method == 'GET':
        form = SigninForm()
        context = { 'form' : form }
        return render(request, "RA/signin.html", context)
    else:
        form = SigninForm(request.POST)
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, "Invalid form data, try again")
            context = {'form': form}
            return render(request, "RA/signin.html", context)
        # form is valid, so, proceed
        phone_number = form.data.get("phone_number")
        password = form.data.get("password")
        user = authenticate(phone_number=phone_number, password=password)
        if user is None:
            messages.add_message(request, messages.WARNING, "Invalid userid/password")
            context = {'form': form}
            return render(request, "RA/signin.html", context)
        # user is authenticated
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "You are now logged in")
        return redirect("RA:choosingservice")

def logout_page(request):

    logout(request)
    return redirect("RA:register")
#
def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {'form': form}
        return render(request,"RA/register.html", context)
    else:
        form = UserCreationForm(request.POST)
        context = {'form': form}
        if not form.is_valid():
            messages.add_message(request, messages.WARNING, "something went wrong")
            return render(request,"RA/register.html", context)
        password = form.data.get("password")
        user = form.save()
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "user created")
        return redirect("RA:signin")

def chooseservice(request):

    context={}

    return render(request, "RA/choosingservice.html", context)

def stuff(request):
    return render(request,"RA/stuff.html", {})

def instaauth(request):
    code = request.GET.get("code")
    url = "https://api.instagram.com/oauth/access_token"
    r = requests.post(url, data={
        'client_id': '3583383ebc454b5e85351dd20c7d3ade',
        'client_secret': 'd0c0eef4e2eb408d8d7afe006c310904',
        'grant_type': 'authorization_code',
        'redirect_uri': 'http://localhost:8000/RA/instaauth/',
        'code': code
    })

    # print("code is: " + code)
    # print (r.json())
    return render(request, "RA/st.html",
                  {"code": code, "r": r, "u": r.json()})

def about(request):

    return render(request,"RA/about.html", {})

def services(request):

    service = Service.objects.all()
    context = {
        'service': service,
    }

    return render(request,"RA/services.html", context)