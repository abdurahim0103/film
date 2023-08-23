from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("films", views.FilmViewset, basename= "films")
router.register("actors", views.ActorViewset, basename= "actor")


urlpatterns = [
    path("category/",views.GetCategory.as_view() ),
] + router.urls
