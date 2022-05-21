from django.urls import path
from activities import views

app_name = "activities"

urlpatterns = [
    path("", views.PublishedActivityList.as_view(), name="activity-list"),
    path(
        "<uuid:id>/",
        views.ActivityDetail.as_view(),
        name="activity-detail",
    ),
    path(
        "<slug:title>/",
        views.CreateUpdateActivity.as_view(),
        name="CreateUpdateActivity"
    )
]


