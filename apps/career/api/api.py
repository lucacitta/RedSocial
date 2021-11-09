from rest_framework import generics

from apps.career.models import Career
from .serializers import Career_list_serializer, Career_detail_serializer

class Career_list_api_view(generics.ListAPIView):
    serializer_class = Career_list_serializer

    def get_queryset(self):
        self.get_serializer()
        return Career.objects.filter(carrer_isActive = True)

class Career_retrieve_api_view(generics.RetrieveAPIView):
    serializer_class = Career_detail_serializer

    def get_queryset(self, pk = None):
        return self.get_serializer().Meta.model.objects.filter(carrer_isActive = True)