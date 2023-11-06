from django.urls import path
from .views.homepage import HomePageView
from .views.see_all import SeeAllCharactersView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('all-characters/', SeeAllCharactersView.as_view(), name="all-characters"),
    path('all-comics/', SeeAllCharactersView.as_view(), name="all-characters"),
    path('all-series', SeeAllCharactersView.as_view(), name="all-characters"),    
]
