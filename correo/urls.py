from django.conf.urls import patterns, url

from correo import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )
