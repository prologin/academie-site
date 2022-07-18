from django.urls import path

from problems import views

from rest_framework.routers import DefaultRouter

app_name = "problems"

router = DefaultRouter()
router.register(r'', views.ProblemView, basename='problems')


urlpatterns = [
]

urlpatterns += router.urls