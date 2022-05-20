from django.urls import path
from status import views

app_name = "status"

urlpatterns = [
    path(
        "<uuid:id>/",
        views.StatusRetrieve.as_view(),
        name="StatusRetrieve"
    ),
]
