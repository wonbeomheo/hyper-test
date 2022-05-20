from django.urls import path

from . import views

app_name = 'hyper'
urlpatterns = [
    path('', views.index, name='home'),
    path('dashboard/analytics/', views.analytics, name='analytics'),
    path('dashboard/projects/', views.projects, name='projects'),
    path('users/', views.users, name='users'),
    path('user-registration/', views.register, name='register'),
    path('user-login/', views.usr_login, name='login'),
    path('signout/', views.signout, name='signout')
]