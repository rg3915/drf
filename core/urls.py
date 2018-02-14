from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
