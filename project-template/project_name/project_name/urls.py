from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Core URLs
urlpatterns = patterns('',
  (r'^admin/',        include(admin.site.urls)),
)

# Static URLs
urlpatterns += staticfiles_urlpatterns()
