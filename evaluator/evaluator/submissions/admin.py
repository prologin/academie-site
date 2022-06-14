from django.contrib import admin
from submissions import models


def run_sub_in_camisole(model_admin, request, queryset):
    from submissions.tasks import run_code_submission
    for obj in queryset:
        print('START\n\n')
        run_code_submission(obj.id)
        #run_code_submission.apply_async(args=[obj.id])
        #run_code_submission.delay(args=[obj.id])

@admin.register(models.ProblemSubmission)
class ProblemSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "problem",
        "validated",
        "validated_by"
    )

    raw_id_fields= [
        "validated_by",
        "problem",
        "user"
    ]

    readonly_fields = ("id",)

    search_fields = ("id", "user__username", "problem__slug")

    list_filter = ("validated",)

@admin.register(models.ProblemSubmissionCode)
class ProblemSubmissionCodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "submission",
        "validated",
    )

    actions = [run_sub_in_camisole]

    search_fields = ("id", "submission__user__username",)

    list_filter = ("validated",)