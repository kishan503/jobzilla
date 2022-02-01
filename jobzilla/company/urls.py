"""jobzilla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('company-signup/',views.company_signup,name="company-signup"),
    path('company-signin/',views.company_signin,name="company-signin"),
    
    path('company-profile/',views.company_profile,name="company-profile"),
    path('company-logout/',views.company_logout,name="company-logout"),
    
    path('forgotpassword/',views.forgot_password,name="forgotpassword"),
    path('send-otp/',views.send_otp,name="send-otp"),
    
    path('reset-password/',views.reset_password,name="reset-password"),
    path('companies/',views.companies,name="companies"),
    path('clients/',views.clients,name="clients"),
    
    path('company-profile-settings/',views.company_profile_settings,name="company-profile-settings"),
    
    path('upload-company-logo/',views.upload_company_logo,name="upload-company-logo"),
    
    path('client-signup/',views.client_signup,name="client-signup"),
    
    path('client-profile/',views.client_profile,name="client-profile"),
    path('client-logout/',views.client_logout,name="client-logout"),
    
    path('client-profile-settings/',views.client_profile_settings,name="client-profile-settings"),
    
    path('upload-client-logo/',views.upload_client_logo,name="upload-client-logo"),
    path('company-password-change/',views.company_password_change,name="company-password-change"),
    path('client-password-change/',views.client_password_change,name="client-password-change"),
    
    path('company-details/',views.company_details,name="company-details"),
    path('client-details/',views.client_details,name="client-details"),

    path('view-other-company-profile/<int:pk>/',views.view_other_company_profile,name="view-other-company-profile"),
    path('view-other-client-profile/<int:pk>/',views.view_other_client_profile,name="view-other-client-profile"),
    
    path('update-companyportfolio/',views.update_companyportfolio,name="update-companyportfolio"),
    path('update-clientportfolio/',views.update_clientportfolio,name="update-clientportfolio"),

    path('create-new-jobpost/',views.create_new_jobpost,name="create-new-jobpost"),
    
    path('like-jobpost/<int:pk>/',views.like_jobpost,name="like-jobpost"),
    path('post_likes/<int:pk>/',views.post_likes,name="post_likes"),
    
    path('follow/<int:pk>/',views.follow,name="follow"),

    path('delete-post/<int:pk>/',views.delete_post,name="delete-post"),
    path('close-post/<int:pk>/',views.close_post,name="close-post"),
    
]
