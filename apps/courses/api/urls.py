from django.urls import path

from .api import Course_list_api_view, Course_retrieve_api_view


urlpatterns = [
    path('',Course_list_api_view.as_view(), name= 'Course_list_api_view'),
    path('<int:pk>/',Course_retrieve_api_view.as_view(), name= 'Course_retrieve_api_view'),
]