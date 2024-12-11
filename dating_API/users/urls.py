from rest_framework.urls import path
from .views import TestAPIView, FormAPIView, LikeAPIView, MyMatchesAPIView, MyProfileAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
    path('get-form/', FormAPIView.as_view()),
    path('like/', LikeAPIView.as_view()),
    path('my-matches/', MyMatchesAPIView.as_view()),
    path('my-profile/', MyProfileAPIView.as_view()),
]
