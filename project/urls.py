"""project URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #url(pattern, view), 
    url(r'^state_list/$', 'main.views.state_list'),
    url(r'^state_search/$', 'main.views.state_search'),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),

    url(r'^stateCapital_detail/(?P<pk>\d+)/$', 'main.views.stateCapital_detail'),
    url(r'^state_detail/(?P<pk>\d+)/$', 'main.views.state_detail'),
    url(r'^city_detail/(?P<pk>\d+)/$', 'main.views.city_search'),
]
