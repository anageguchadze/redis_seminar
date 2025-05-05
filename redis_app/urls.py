from django.urls import path, include
from .views import AnimalList, AnimalDetail, CategoryList, CategoryDetail

urlpatterns = [
    path('categoies/', CategoryList.as_view()),
    path('categoies/<int:pk>/', CategoryDetail.as_view()),
    path('animals/', AnimalList.as_view()),
    path('animals/<int:pk>/', AnimalDetail.as_view()),
]