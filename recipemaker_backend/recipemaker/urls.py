from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.get_recipe_recommendations, name='recipe-recommendations'),
]