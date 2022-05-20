from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import User


# Create your views here.
def index(request):
    context = {'user': request.user}
    return render(request, 'index.html', context)


def analytics(request):
    context = {'user': request.user}
    return render(request, 'data/analytics.html', context)


def projects(request):
    context = {'user': request.user}
    return render(request, 'data/dashboard-projects.html', context)


def users(request):
    user_list = User.objects.filter(is_superuser=False).order_by('id')
    context = {'user_list': user_list,
               'user': request.user,
               }
    return render(request, 'users/users.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['re-password']

        user = User.objects.create_user(username, email, pass1)
        user.first_name = firstname
        user.last_name = lastname

        user.save()
        messages.success(request, "Your account has been successfully created.")
        return redirect('hyper:login')
    else:
        return render(request, 'users/users-registration-form.html')


def usr_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('hyper:users')
        else:
            messages.error(request, 'ID or Password was incorrect.')
            return redirect('hyper:login')
    else:
        return render(request, 'users/login.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully.")
    return redirect('hyper:home')