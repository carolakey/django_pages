# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('key/', AboutPageView.as_view(), name='key'),
    path('', HomePageView.as_view(), name='carol'),
]
