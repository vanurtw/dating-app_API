from rest_framework.urls import path
from .views import FormAPIView, LikeAPIView, MyMatchesAPIView, MyProfileAPIView, CitiesAPIView

urlpatterns = [
    path('get-form/', FormAPIView.as_view()),
    path('like/', LikeAPIView.as_view()),
    path('my-matches/', MyMatchesAPIView.as_view()),
    path('my-profile/', MyProfileAPIView.as_view()),
    path('cities/', CitiesAPIView.as_view()),

]
