from rest_framework.urls import path
from .views import TestAPIView, FormAPIView, LikeAPIView, MyLikesAPIView, MyProfileAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view()),
    path('get-form/', FormAPIView.as_view()),
    path('like/', LikeAPIView.as_view()),
    path('my-likes/', MyLikesAPIView.as_view()),
    path('my-profile/', MyProfileAPIView.as_view()),
]
