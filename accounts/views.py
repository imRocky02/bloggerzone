from tkinter.tix import Form
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from  django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have been registered successfully")
            return redirect('home')
    else:
        form = UserCreationForm()
    data = {
        "title": "Register User",
        'form': form,

    }
    return render(request, "accounts/register.html", data)

def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            credentials = form.cleaned_data
            user = authenticate(
                username = credentials.get('email'),
                password = credentials.get('password')
            )

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))

    data={
        "title": "Login",
        "form": form
    }
    return render(request, "accounts/login.html", data) 

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))
