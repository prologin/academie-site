from django.contrib import admin

from problems import models


@admin.register(models.Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
        "difficulty",
    )

    readonly_fields = ("id",)

    list_filter = ("difficulty",)

    search_fields = (
        "id",
        "title",
    )

    fieldsets = (
        (None, {"fields": ("id",)}),
        (
            "Definition",
            {"fields": ("title", "managers", "description", "subject", "difficulty")},
        ),
        ("Submission", {"fields": ("allowed_languages", "skeletons")}),
        (
            "Correction",
            {
                "fields": ("correction_templates", "tests"),
                "classes": ("collapse",),
            },
        ),
    )
