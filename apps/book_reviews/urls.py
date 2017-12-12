from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.show),
    url(r'^showBook$', views.showBook),
    url(r'^/(?P<id>[0-9])$', views.addBook),
]