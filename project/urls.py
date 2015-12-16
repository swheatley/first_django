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
from django.conf import settings  
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views
from main import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vote/(?P<pk>\d+)/$', 'main.views.vote'),

    url(r'^api_state_list/$', 'main.views.api_state_list'),
    url(r'^ajax_state_list/$', 'main.views.ajax_state_list'),

    url(r'^api_city_list/$', 'main.views.api_city_list'),
    url(r'^ajax_city_list/$', 'main.views.ajax_city_list'),

    
    url(r'^$', 'main.views.state_list'),
    url(r'^state_list/$', 'main.views.state_list'),
    url(r'^state_search/$', 'main.views.state_search'),
    url(r'^state_create/$', 'main.views.state_create'),
    url(r'^state_detail/(?P<pk>\d+)/$', 'main.views.state_detail'),
    #url(r'^state_edit/$', 'main.views.state_edit'),
    #url(r'^state_delete/$', 'main.views.state_delete'),


    url(r'^city_list/$', 'main.views.city_list'),
    url(r'^city_search/(?P<pk>\d+)/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^city_detail/(?P<pk>\d+)/$', 'main.views.city_detail'),
    url(r'^city_edit/(?P<pk>\d+)/$', 'main.views.city_edit'),
    #url(r'^city_delete/$'.'main.views.city_delete'),


    url(r'^StateCapital_list/$' ,  'main.views.stateCapital_list'),
    #url(r'^StateCapital_search/$', 'main.views.stateCapital_search'),
    url(r'^StateCapital_detail/(?P<pk>\d+)/$', 'main.views.stateCapital_detail'),
    #url(r'^StateCapital_create/$', 'main.views.stateCapital_create'),
    #url(r'^StateCapital_edit/$'), 'main.views.stateCapital_edit'),
    #url(r'StateCapital_delete/$). 'main.views.stateCapital_delete'),
    
    
    url(r'^contact_view/$', 'main.views.contact_view'),
    # url(r'^signup/$', 'main.views.signup'),
    # url(r'^login/$', 'main.views.login_view'),
    # url(r'^logout_view/$', 'main.views.logout_view'),
    # #url(r'^register/$', CreateView)
   
    #url(r'^blog/$', 'main.views.blog.html'),
    #url(r'^base/$', 'main.views.base.html'),

    url(r'^ajax_search/$', 'main.views.ajaxot_search'),
    url(r'^ajax_vote/$', 'main.views.ajax_ve'),
    url(r'^json_response/$', 'main.views.json_response'),

    url(r'^city_cas_list/$', 'main.views.city_list_cas'),


    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
