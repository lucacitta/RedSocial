from django.urls import path

from .api import Professor_list_api_view, Profesor_retrieve_api_view


urlpatterns = [
    path('', Professor_list_api_view.as_view(), name='Professor_list_api_view'),
    path('<int:pk>/', Profesor_retrieve_api_view.as_view(), name='Profesor_retrieve_api_view'),
]
