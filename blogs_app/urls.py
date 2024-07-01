from django.urls import path
from .views import HomeView, PostCreateAPIView, CommentCreateListAPIView

urlpatterns = [
    path('home', HomeView.as_view(), name='home'),
    path('posts', PostCreateAPIView.as_view(), name='post-create'),
    path('posts/<int:id>/comments', CommentCreateListAPIView.as_view(), name='comment-create-list'),
]
