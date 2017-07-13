from django.conf.urls import url
from . import views

app_name = 'cars'

urlpatterns = [
    # /cars/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /cars/4/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]