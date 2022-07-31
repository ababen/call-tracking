from django.urls import include, re_path, path
from django.contrib import admin

from call_tracking.views import index, dashboard, login, logout
# from messaging.views import sms

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^dashboard$', dashboard, name='dashboard'),
    re_path(r'^call-tracking/', include('call_tracking.urls')),
    # re_path(r'^sms/', include('messaging.urls')),
    # re_path(r'^users/', include("users.urls")),

    # Include the Django admin
    re_path(r'^admin/', admin.site.urls),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
