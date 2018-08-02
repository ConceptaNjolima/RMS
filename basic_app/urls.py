from django.conf.urls import url, include
from . import views


app_name = 'basic_app'
urlpatterns = [

    url(r'^index',views.index,name='index'),
    url(r'^login/',views.user_login,name='login'),
    url(r'^register/', views.register, name='register'),
    url(r'tenant',views.tenantView, name='tenantView'),
    url(r'^managerLogin',views.manager_login,name='managerLogin'),
    url(r'^manager',views.manager,name='manager'),
    url(r'^welcomeManager',views.welcomeManager,name='welcomeManager'),
    # url(r'^delete/(?P<username>[A-Za-z]+)$', views.delete_tenant, name='delete'),
]
