from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from misc.views import SchemaView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/activities/", include("activities.urls")),
    path("api/problems/", include("problems.urls")),
    path("api/submissions/", include("submissions.urls")),
    path("api/status/", include("status.urls")),
    path("auth/", include("authentification.urls")),
    path("reset_password/", include("reset.urls")),
    path(
        "swagger/",
        SchemaView.with_ui("swagger", cache_timeout=0),
        name="swagger",
    ),
    path(
        "redoc/",
        SchemaView.with_ui("redoc", cache_timeout=0),
        name="swagger",
    ),
] + static("uploads/", document_root="./uploads")
