from django.urls import path, include
from .views import show_catalog

urlpatterns = [
    path('', show_catalog, name='show_catalog'),
]