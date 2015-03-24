from django.conf.urls import patterns, url
from do2things.views import (HomePageView)

urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='do2things-home'),
)
