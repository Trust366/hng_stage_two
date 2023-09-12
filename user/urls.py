from django.urls import path
from . import apis as views

urlpatterns = [
    path("", views.UserCreateView.as_view()),
    path("<int:pk>/", views.UserDetailView.as_view()),
]