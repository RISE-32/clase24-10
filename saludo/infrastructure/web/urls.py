from django.urls import path
from saludo.infrastructure.web import views

urlpatterns = [
    path('saludar/', views.saludar_view, name='saludar'),
]