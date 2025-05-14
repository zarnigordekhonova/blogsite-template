from django.urls import path
from apps.blog.views import (PostCreateView, PostUpdateView, PostDetailView,
                             PostDeleteView)

app_name = "blog"

urlpatterns = [
    path("create-post/", PostCreateView.as_view(), name='create_post'),
    path("update-post/<int:pk>/", PostUpdateView.as_view(), name='update_post'),
    path("detail-post/<str:slug>/", PostDetailView.as_view(), name='detail_post'),
    path("delete-post/<int:pk>/", PostDeleteView.as_view(), name='delete_post'),
]