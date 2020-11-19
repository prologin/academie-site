from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from . import views

app_name = "academy"

schema_view = get_schema_view(
    openapi.Info(
        title="Prologin Academy API",
        default_version="v1",
        description="Test description",
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    re_path(
        r"^doc(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^doc/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]

router = routers.DefaultRouter()
router.register("track", views.TrackInstanceViewSet, basename="track")
router.register("submission", views.SubmissionViewSet, basename="submission")
router.register("user", views.UserViewSet, basename="user")

track_subrouter = nested_routers.NestedSimpleRouter(
    router, "track", lookup="track"
)
track_subrouter.register(
    "problem", views.ProblemViewSet, basename="track-problems"
)

urlpatterns += router.urls
urlpatterns += track_subrouter.urls
