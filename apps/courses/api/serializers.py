
from django.db.models import fields
from rest_framework import serializers

from apps.courses.models import Course

class Courses_list_serializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id','course_name', 'course_description', 'course_yearInCareer']


class Courses_retrieve_serializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'