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

class SubmissionSerializer(serializers.ModelSerializer):
    class TrackSelectField(serializers.PrimaryKeyRelatedField):
        def get_queryset(self):
            if self.context['request'].user.is_staff:
                return models.TrackInstance.objects.all()
            return models.TrackInstance.objects.filter(public=True)
    
    track = TrackSelectField()

    class Meta:
        model = models.Submission
        fields = (
            'track',
            'problem_id',
            'code',
            'id',
            'author',
            'submission_date',
            'correction_date',
            'submission_count',
            'passed',
            'correction_data',
        )
        read_only_fields = (
            'id',
            'author',
            'submission_date',
            'correction_date',
            'submission_count',
            'passed',
            'correction_data',
        )