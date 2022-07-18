from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SchemaView = get_schema_view(
    openapi.Info(
        title="Academie Prologin API",
        default_version="v1",
        description="Academie Prologin API",
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)
