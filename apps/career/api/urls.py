from django.urls import path

from .api import Career_list_api_view, Career_retrieve_api_view

urlpatterns = [
    path('', Career_list_api_view.as_view(), name = 'List_carrer_api_view'),
    path('<int:pk>/',Career_retrieve_api_view.as_view(), name = 'Retrieve_carrer_api_view')
]