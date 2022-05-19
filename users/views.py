from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout

from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def analytics(request):
    return render(request, 'data/analytics.html')


def projects(request):
    return render(request, 'data/dashboard-projects.html')


def users(request):
    user_list = User.objects.order_by('id')
    context = {'user_list': user_list}
    return render(request, 'users/users.html', context)


def register(request):
    return render(request, 'users/users-registration-form.html')


def usr_reg_progress(request):
    # Need to check if the user info is already in the database
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re-password']:
            user = User(first_name=request.POST['first-name'],
                        last_name=request.POST['last-name'],
                        username=request.POST['username'],
                        password=make_password(request.POST['password']),
                        email=request.POST['email'],
                        )
            user.save();
            return HttpResponseRedirect(reverse('hyper:users'))
        else:
            return HttpResponseRedirect(reverse('hyper:register'))


def usr_login(request):
    return render(request, 'users/login.html')


def usr_login_progress(request):
    if request.method == 'POST':
        users_list = User.objects.order_by('id')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('hyper:users'))
        else:
            return HttpResponseRedirect(reverse('hyper:login'))