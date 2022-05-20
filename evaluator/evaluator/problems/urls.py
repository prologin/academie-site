from django.urls import path
from problems import views

app_name = "problems"

urlpatterns = [
    path(
        "<slug:title>/",
        views.ProblemCreateView.as_view(),
        name="ProblemCreateView",
    )
]
