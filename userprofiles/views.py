from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from userprofiles.models import Userprofile
from django import forms

def signin(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)

            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/') 

    context = {}
    return render(request, 'sign/signin.html', context)

def signup(request):
    if request.user.is_authenticated():
        return redirect('/')
    else:
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        name = request.POST.get('name', None)
        lastname = request.POST.get('lastname', None)

        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        else:
            if request.method == 'POST':
                userprofile=Userprofile.objects.create_user(email=email,
                                                            name=name,
                                                            lastname=lastname,
                                                            password=password,)
                userprofile.save()
                user = authenticate(email=email, password=password)
                login(request, user)
                return redirect('/')
    context = {}
    return render(request, 'sign/signup.html', context)
