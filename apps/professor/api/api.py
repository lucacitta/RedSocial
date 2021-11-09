from rest_framework import generics

from .serializers import Professor_list_serializer, Professor_retrieve_serializer

from apps.professor.models import Professor

class Professor_list_api_view(generics.ListAPIView):
    serializer_class = Professor_list_serializer

    def get_queryset(self):
        self.get_serializer()
        return Professor.objects.filter(professor_isActive = True)

class Profesor_retrieve_api_view(generics.RetrieveAPIView):
    serializer_class = Professor_retrieve_serializer

    def get_queryset(self, pk = None):
        return self.get_serializer().Meta.model.objects.filter(professor_isActive = True)