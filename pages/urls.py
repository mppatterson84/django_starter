from django.urls import path

from .views import (
    HomePageView,
    PageDetailView,
    BrowserPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('media/browser/', BrowserPageView.as_view(), name='media-browser'),
    path('<slug:slug>/', PageDetailView.as_view(), name='page-detail'),
]
