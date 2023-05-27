from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def registration_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
            else:
                messages.error(request, 'Password or username is incorrect')
        context = {
            'form': form
        }
        return render(request, 'registrationPage.html', context)


@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Password or username is incorrect')
        context = {}
        return render(request, 'loginPage.html', context)


@login_required
def logout_page(request):
    logout(request)
    return redirect('/')
