from django.urls import path
from rest_framework.routers import DefaultRouter

from problems import views

app_name = "problems"

router = DefaultRouter()
router.register(r"", views.ProblemView, basename="problems")


urlpatterns = []

urlpatterns += router.urls
