from django.urls import path
from .views.homepage import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
