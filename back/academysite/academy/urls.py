from django.urls import path, include

app_name = 'academy'

urlpatterns = [
    path('', include('academy.api.routes')),
]