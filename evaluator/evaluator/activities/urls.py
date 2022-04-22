from django.urls import path
from activities import views

app_name = "activities"

urlpatterns = [
    path("", views.PublishedActivityList.as_view(), name="activity-list"),
    path(
        "<uuid:pk>/",
        views.PublishedActivityDetail.as_view(),
        name="activity-detil",
    ),
]
