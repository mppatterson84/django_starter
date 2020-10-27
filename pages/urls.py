from django.urls import path

from .views import (
    HomePageView,
    PageDetailView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('<slug:slug>/', PageDetailView.as_view(), name='page-detail')
]
