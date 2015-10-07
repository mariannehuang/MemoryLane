"""memorylane URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^settings/', TemplateView.as_view(template_name='settings.html'), name="settings"),
    url(r'^signup/', TemplateView.as_view(template_name='signup.html'), name="signup"),
    url(r'^post/', TemplateView.as_view(template_name='post.html'), name="post"),
    url(r'^passwordreset/', TemplateView.as_view(template_name='password-reset.html'), name="passwordreset"),
    url(r'^login/', TemplateView.as_view(template_name='login.html'), name="login"),
    url(r'^friends/', TemplateView.as_view(template_name='friends.html'), name="friends"),
    url(r'^profiletest/(?P<user_id>[0-9]+)/$', views.profiletest, name='profiletest'),
    url(r'^userlist/$', views.userlist, name='userlist'),
    
    
]
