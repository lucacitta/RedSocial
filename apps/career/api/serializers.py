from django.db.models import fields
from rest_framework import serializers

from apps.career.models import Career

class Career_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id','carrer_name','carrer_description','carrer_years','carrer_idSupervisor']

class Career_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'