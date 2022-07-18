from django.urls import path
from rest_framework.routers import DefaultRouter

from status import views

app_name = "status"

router = DefaultRouter()
router.register(r"", views.StatusView, basename="status")

urlpatterns = []

urlpatterns += router.urls
