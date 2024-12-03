from rest_framework.urls import path
from .views import TestAPIView, SearchAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
    path('search/', SearchAPIView.as_view())
]
