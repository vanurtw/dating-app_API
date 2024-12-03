from rest_framework.urls import path
from .views import LoginAPIView


urlpatterns = [
    path('login/', LoginAPIView.as_view()),
]