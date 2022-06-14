from django.urls import path

from problems import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.ProblemView)

app_name = "problems"

urlpatterns = [

]

urlpatterns += router.urls