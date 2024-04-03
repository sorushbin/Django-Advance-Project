from django.urls import path, include
from . import views


app_name = "blog"

urlpatterns = [
    # path('fbv-index', views.blog_view, name ='fbv-index'),
    path("cbv-index", views.BlogView.as_view(), name="cbv-index"),
    path(
        "go-to-varzesh",
        views.RedirectToVarzeshView.as_view(),
        name="redirect-to-varzesh",
    ),
    path("post/", views.PostListView.as_view(), name="home-blog"),
    path(
        "home-blog/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail",
    ),
    path("create-post/", views.PostCreateView.as_view(), name="create-post"),
    path(
        "home-blog/<int:pk>/edit/",
        views.PostEditView.as_view(),
        name="post-edit",
    ),
    path(
        "home-blog/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    path("api/v1/", include("blog.api.v1.urls")),
]
