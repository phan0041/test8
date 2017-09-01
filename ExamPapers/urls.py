from django.conf.urls.defaults import patterns, include, url

import views
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()
from django.conf import settings


urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^bio/', include('bio.urls')), #can delete
    url(r'^', include('bio.urls')),

)

# This is needed to serve static files like images and css
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

