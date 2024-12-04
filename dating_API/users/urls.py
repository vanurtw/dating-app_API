from rest_framework.urls import path
from .views import TestAPIView, FormAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
    path('get-form/', FormAPIView.as_view())
]
