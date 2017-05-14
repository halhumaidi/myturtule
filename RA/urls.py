from django.conf.urls import url

from . import views

app_name = 'RA'

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^logout/$', views.logout_page, name='logout'),
    url(r'^choosingservice/$', views.chooseservice, name='choosingservice'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
    url(r'^instaauth/$', views.instaauth, name='instaauth'),
    url(r'^stuff/$', views.stuff, name='stuff'),
]