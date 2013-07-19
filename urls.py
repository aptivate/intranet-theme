from __future__ import absolute_import

from django.conf.urls.defaults import patterns, url

import django.contrib.auth.views
from . import views

urlpatterns = patterns('',
    url(r'^profile$', views.UserProfileView.as_view(),
        name="user_profile"),
)
