from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^customer/detail$', views.detail, name='detail'),
]
