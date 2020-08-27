#file for getting JSON data.
from rest_framework import serializers
from rest_framework import fields
from .models import sciencehistory

class sciencehistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = sciencehistory
        fields = '__all__'
