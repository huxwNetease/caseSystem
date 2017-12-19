from django.conf.urls import url
from django.urls import path, include

from login import views

urlpatterns = [
    url(r'^index/',views.index),
    url(r'^land/',views.land),
]