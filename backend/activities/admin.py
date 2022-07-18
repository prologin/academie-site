from django.contrib import admin

from activities import models

@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "version",
        "id",
    )

    readonly_fields = ("id",)

    search_fields = (
        "title",
        "version",
        "id",
    )

    list_filter = ("managers",)

    fieldsets = (
        (None, {"fields": ("id", "title", "image", "version", "problems")}),
        ("PROJECT DETAILS", {"fields": ("description", "difficulty", "author", "managers")}),
        ("DATES", {"fields": ("opening", "closing", "publication")}),
    )


"""
    inlines = (
#        ActivityManagerInlineAdmin,
        ActivityProblemInlineAdmin,
    )
    """
