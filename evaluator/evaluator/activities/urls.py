from django.urls import path
from activities import views
from rest_framework.routers import DefaultRouter

app_name = "activities"

router = DefaultRouter()
router.register(r'', views.ActivityView, basename="activities")
router.register(r'images', views.ActivityImageView, basename="activities_image")

urlpatterns = [
]

urlpatterns += router.urls