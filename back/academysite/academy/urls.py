from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'academy'

schema_view = get_schema_view(
   openapi.Info(
      title="Prologin Academy API",
      default_version='v1',
      description="Test description",
   ),
   public=False,
   permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    re_path(r'^doc(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^doc/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include('academy.api.routes')),
]