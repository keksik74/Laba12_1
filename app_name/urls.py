from . import views
from django.urls import path, include
from .api import PostViewSet
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

router = DefaultRouter()
router.register("posts", PostViewSet)


urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("register/", views.register_view, name="register"),
    path("", views.post_list, name="post_list"),
    path("create/", views.post_create, name="post_create"),
    path("edit/<int:pk>/", views.post_edit, name="post_edit"),
    path("delete/<int:pk>/", views.post_delete, name="post_delete"),
    path("", include(router.urls)),
]