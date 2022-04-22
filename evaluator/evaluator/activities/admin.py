from django.contrib import admin
from activities import models


class ActivityProblemInlineAdmin(admin.TabularInline):
    model = models.ActivityProblem
    fields = ("problem", "slug", "order")
    ordering = ("order",)
    raw_id_fields = ("problem",)
    extra = 0


class ActivityManagerInlineAdmin(admin.TabularInline):
    model = models.Activity.managers.through
    raw_id_fields = ("user",)
    extra = 0


@admin.register(models.Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "version",
        "id",
    )

    readonly_fields = ("id",)

    search_fields = (
        "title",
        "slug",
        "version",
        "id",
    )

    list_filter = ("managers",)

    fieldsets = (
        (None, {"fields": ("id", "slug", "version")}),
        ("PROJECT DETAILS", {"fields": ("title", "description")}),
        ("DATES", {"fields": ("opening", "closing", "publication")}),
    )

    inlines = (
        ActivityManagerInlineAdmin,
        ActivityProblemInlineAdmin,
    )
