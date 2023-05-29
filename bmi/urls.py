from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('bmi/', views.home, name='home'),
    path('bmi/details/<int:id>', views.detail, name='detail'),
    path('bmi/update/<int:id>', views.update, name='update'),
]
