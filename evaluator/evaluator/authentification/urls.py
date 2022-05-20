from django.urls import path
from authentification import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', views.ObtainTokenPairView.as_view(), name='ObtainTokenPairView'),
    path('login/refresh/', TokenRefreshView.as_view(), name='TokenRefereshView'),
    path('register/', views.RegisterView.as_view(), name='RegisterView'),
]