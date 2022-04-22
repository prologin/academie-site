from django.contrib import admin
from submissions import models


@admin.register(models.ProblemSubmission)
class ProblemSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "problem",
        "validated",
    )

    readonly_fields = ("id",)

    search_fields = ("id", "user__username", "problem__slug")

    list_filter = ("validated",)


@admin.register(models.ProblemSubmissionCode)
class ProblemSubmissionCodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "submission",
    )

    search_fields = (
        "id",
        "submission__user__username",
    )

    list_filter = ("validated",)
