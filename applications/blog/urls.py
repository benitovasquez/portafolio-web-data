from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.renderPosts, name="index"),  # Vista de lista de blogs
    path("<int:post_id>/", views.post_detail, name="post_detail"),  # Vista de detalle del blog
]

