from rest_framework.urls import path
from .views import TestAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
]
