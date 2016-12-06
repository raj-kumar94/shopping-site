from django.conf.urls import url
from . import views

app_name = 'shopping'

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^car/$', views.car,name='car'),
    url(r'^laptop/$', views.laptop,name='laptop'),
    url(r'^men/$', views.men,name='men'),
    url(r'^mobile/$', views.mobile,name='mobile'),
    url(r'^netbank/$', views.netbank,name='netbank'),
    url(r'^register/$', views.register,name='register'),
    url(r'^watches/$', views.watches,name='watches'),
    url(r'^welcome/$', views.welcome,name='welcome'),
    url(r'^women/$', views.women,name='women'),
    url(r'^login/$', views.auth_login,name='login'),
    url(r'^logout/$', views.logout_view,name='logout'),
    url(r'^logme/$', views.logme,name='logme'),
    url(r'^profile/$', views.profile,name='profile'),
    url(r'^profile_edited/$', views.profile_edited,name='profile_edited'),
    url(r'^delete_cart/$', views.delete_cart, name='delete_cart'),


]
