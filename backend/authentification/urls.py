from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from authentification import views

urlpatterns = [
    path(
        "login/",
        views.ObtainTokenPairView.as_view(),
        name="ObtainTokenPairView",
    ),
    path(
        "login/refresh/", TokenRefreshView.as_view(), name="TokenRefereshView"
    ),
    path("register/", views.RegisterView.as_view(), name="RegisterView"),
    path(
        "profile/", views.UserProfileView().as_view(), name="UserProfileView"
    ),
]
