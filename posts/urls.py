from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path("", PostListView.as_view(), name="posts_list"),
    path("detailed/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("new/", PostCreateView.as_view(), name="post_new"),
    path("edit/<int:pk>", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete"),
]