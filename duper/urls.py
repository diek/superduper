from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^no_super/$', views.no_super, name='no_super'),
    url(r'^super/$', views.super, name='super')
]
