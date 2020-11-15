from rest_framework import serializers
from django.urls import reverse
from academy import models

class TrackInstanceStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TrackInstance
        fields = '__all__'

class TrackInstanceSerializer(TrackInstanceStaffSerializer):
    class Meta:
        model = models.TrackInstance
        fields = ('name', 'id', 'public',)