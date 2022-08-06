"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('about/',views.about,name='aboutus'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('change-password/',views.change_password,name='change-password'),
    path('change-details/',views.change_details,name='change-details'),
    path('change-details-member/',views.change_details_member,name='change-details-member'),
    path('change-details-watchman/',views.change_details_watchman,name='change-details-watchman'),
    path('add-notice/',views.add_notice,name="add-notice"),
    path('all-notice/',views.all_notice,name="all-notice"),
    path('add-member/',views.add_member,name="add-member"),
    path('all-member/',views.all_member,name='all-member'),
    path('add-event/',views.add_event,name="add-event"),
    path('all-event/',views.all_event,name="all-event"),
    path("update-password/",views.update_password,name="update-password"),
    path('add-watchman/',views.add_watchman,name="add-watchman"),
    path('all-watchman/',views.all_watchman,name="all-watchman"),
    path('add-visitor/',views.add_visitor,name="add-visitor"),
    path('all-visitor/',views.all_visitor,name="all-visitor"),
    path('reset-password/',views.reset_password,name='reset-password'),
    path('update-forgot-password/',views.update_forgot_password,name='update-forgot-password'),
  
]
