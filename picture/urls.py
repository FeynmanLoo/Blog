from django.conf.urls import url

from . import views

app_name = 'picture'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
]