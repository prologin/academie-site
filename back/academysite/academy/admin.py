from django.contrib import admin
from . import models

@admin.register(models.Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'track',
        'problem_id',
        'submission_date',
        'passed',
    )
    search_fields = (
        'problem_id',
        'author__username',
        'track__name',
    )
    list_filter = (
        'problem_id',
        'track',
        'passed',
    )

@admin.register(models.TrackInstance)
class TrackInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'track_id',
        'public',
        'archived'
    )
    search_fields = (
        'name',
        'track_id',
    )
    list_filter = (
        'track_id',
        'public',
        'archived',
    )