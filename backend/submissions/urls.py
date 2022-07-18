from django.urls import path
from rest_framework.routers import DefaultRouter

from submissions import views

app_name = "submissions"

router = DefaultRouter()
router.register(r"", views.SubmissionView, basename="submissions")

urlpatterns = []

urlpatterns += router.urls
