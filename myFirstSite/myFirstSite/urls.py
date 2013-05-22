from django.conf.urls import (
    patterns,
    include,
    url
)
# The patterns function gets passed only a single argument- the empty string
#       (The string can be used to supply a common prefix for view functions)
from myFirstSite.views import (
    hello,
    current_datetime,
    hours_ahead
)
# urls.py: The URLs for this Django project. Think of this
# as the "table of contents" of your Django-powered site.

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    # Regex: ^ = require that the pattern matches the start of the string
    # Regex: $ = require that the pattern matches the end of the string
    # Regex: \d{1,2} means require atleast 1 or 2 digits, i.e. 1-99
    # Examples:
    # url(r'^$', 'myFirstSite.views.home', name='home'),
    # url(r'^myFirstSite/', include('myFirstSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
