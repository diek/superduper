from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^render_B/$', views.render_B, name='render_B'),
    url(r'^render_C/$', views.render_C, name='render_C')
]
