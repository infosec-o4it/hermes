from django.conf.urls import patterns, include, url
from django.contrib import admin
import correo

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'hermes.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       # url(r'^admin/', include(admin.site.urls)),
                       url(r'^', include('correo.urls')),
                       url(r'^correo/', correo.views.hide, name='hide'),
                       )
