from rest_framework import serializers

from apps.professor.models import Professor

class Professor_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['id','professor_name', 'professor_lastName', 'professor_rank']

class Professor_retrieve_serializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'