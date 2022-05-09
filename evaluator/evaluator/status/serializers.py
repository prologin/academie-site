from rest_framework import serializers
from status import models

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.CeleryTaskStatusModel
        fields = (
           "id" ,
           "status",
           "info",
        )