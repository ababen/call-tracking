# Messaging URLS

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    # Here we add our Twilio URLs
    url(r'^sms/$', 'views.sms'),
    # url(r'^ring/$', 'views.ring'),
)
