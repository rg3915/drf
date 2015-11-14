from django.conf.urls import url
from core import views

urlpatterns = [
    url(r'^persons/$', views.person_list),
    url(r'^persons/(?P<pk>[0-9]+)/$', views.person_detail),
]
