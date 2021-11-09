from rest_framework import generics


from .serializers import Courses_list_serializer, Courses_retrieve_serializer

from apps.courses.models import Course

class Course_list_api_view(generics.ListAPIView):
    serializer_class = Courses_list_serializer

    def get_queryset(self):
        self.get_serializer()
        return Course.objects.filter(course_isActive = True)

class Course_retrieve_api_view(generics.RetrieveAPIView):
    serializer_class = Courses_retrieve_serializer

    def get_queryset(self, pk = None):
        return self.get_serializer().Meta.model.objects.all().filter(course_isActive = True)