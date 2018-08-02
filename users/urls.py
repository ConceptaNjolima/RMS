

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from basic_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^basic_app/', include('basic_app.urls', namespace='basic_app')),
    url(r'^$', views.index, name='home'),
    url(r'^special', views.special, name='special'),
    url(r'^logout',views.user_logout, name='logout'),



]

