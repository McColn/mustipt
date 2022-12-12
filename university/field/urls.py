
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('base/', views.base,name='base'),
    path('apply/', views.apply,name='apply'),
    path('selected/', views.selected,name='selected'),
    path('team/', views.team,name='team'),
    path('applied/', views.applied,name='applied'),
    path('signin/', views.signin,name='signin'),
    path('signup/', views.signup,name='signup'),
    path('signout/', views.signout,name='signout'),
    path('profile/', views.profile,name='profile'),
]