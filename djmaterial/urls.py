from django.conf.urls import patterns, url

from . import views

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^time_ajax/$', views.time_ajax, name='time_ajax'),
# ]

urlpatterns = patterns('djmaterial.views',
    url(r'^$', 'index', name='index'),
    url(r'^checkout/', 'checkout', name='checkout'),
)
