from rest_framework import serializers
from status import models

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CeleryTaskStatus
        fields = (
           "id" ,
           "status",
           "info",
        )


class StatusFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CeleryTaskStatus
        fields = (
           "id" ,
           "model_id",
           "status",
           "info",
        )