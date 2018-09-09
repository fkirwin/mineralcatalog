from django.conf.urls import url


from . import views as mineral_views
from mineralcatalog import views as core_views


urlpatterns = [
    url(r'(?P<pk>\d+)/$', mineral_views.mineral_detail, name='detail'),
    url(r'^$', core_views.index, name='index'),
]
