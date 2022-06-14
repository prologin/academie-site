from django.urls import path

from status import views

from rest_framework.routers import DefaultRouter

app_name = "status"

router = DefaultRouter()
router.register(r'', views.StatusView, basename="status")

urlpatterns = [
]

urlpatterns += router.urls