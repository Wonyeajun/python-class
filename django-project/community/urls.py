from django.urls import path

from .views import post_list, post_create, post_detail, comment_create, post_like


urlpatterns = [
    path("", post_list, name="post_list"),
    path("create/", post_create, name="post_create"),
    path("<int:pk>/", post_detail, name="post_detail"),
    path("<int:pk>/comment/", comment_create, name="comment_create"),
    path("<int:pk>/like/", post_like, name="post_like"),
]