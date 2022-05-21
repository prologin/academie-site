from django.contrib import admin
from activities import models

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "version",
        "id",
    )

    readonly_fields = ("id", "problems")

    search_fields = (
        "title",
        "version",
        "id",
    )

    list_filter = ("managers",)

    fieldsets = (
        (
            None, 
            {
                "fields": ("id", "title", "version", "problems")
            }
        ),
        (
            "PROJECT DETAILS", 
            {
                "fields": ("description", "author", "managers")
            }
        ),
        (
            "DATES",
            {
                "fields": ("opening", "closing", "publication")
            }
        ),
    )
"""
    inlines = (
#        ActivityManagerInlineAdmin,
        ActivityProblemInlineAdmin,
    )
    """
