from django.urls import path
from customer_service import views

urlpatterns = [
    path("", views.home, name='home')
]