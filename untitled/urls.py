"""untitled URL Configuration


The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from deneme.views import index,register ,detail ,like_place,new_review,profile

urlpatterns = [

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^index$',index, name='index'),
    url(r'^register/$',register,name='register'),
    url(r'^konu/(?P<id>\d+)$', detail, name='konu_detail'),
    url(r'^konu/(?P<konu_id>\d+)/like$', like_place, name='like_place'),
    url(r'^konu/(?P<konu_id>\d+)/new_review$', new_review, name='new_review'),
    url(r'^profile/(?P<id>\d+)$', profile, name='profile'),

]
