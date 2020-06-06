from django.urls import path
from . import views

urlpatterns = [
    path("", views.recipe_index, name="recipe_index"),
    path("entry/", views.recipe_entry, name="recipe_entry"),
    path("<int:pk>/", views.recipe_detail, name="recipe_detail"),
]