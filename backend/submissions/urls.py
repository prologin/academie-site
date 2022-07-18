from django.urls import path

from submissions import views

from rest_framework.routers import DefaultRouter

app_name = "submissions"

router = DefaultRouter()
router.register(r'', views.SubmissionView, basename="submissions")

urlpatterns = [
]

urlpatterns += router.urls