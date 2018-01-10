from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^entre/$', views.entre, name='entre'),
    url(r'^experience/$', views.experience, name='experience'),
    url(r'^volunteer/$', views.volunteer, name='volunteer'),
    url(r'^contact/$', views.contact, name='contact'),
	url(r'^story/$', views.story, name='story'),

]