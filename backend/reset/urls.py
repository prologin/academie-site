from django.urls import include, path

from reset import views

urlpatterns = [
    path("", views.PasswordResetView.as_view(), name="password_reset"),
    path(
        "<uuid:id>/",
        views.PasswordResetIdView.as_view(),
        name="password_reset_id",
    ),
]
