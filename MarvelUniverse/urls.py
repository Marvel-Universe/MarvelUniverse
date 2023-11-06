from django.urls import path
from .views.homepage import HomePageView
from .views.see_all import SeeAllCharactersView, SeeAllComicsView, SeeAllSeriesView

app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('all-characters/', SeeAllCharactersView.as_view(), name="all-characters"),
    path('all-comics/', SeeAllComicsView.as_view(), name="all-comics"),
    path('all-series/', SeeAllSeriesView.as_view(), name="all-series"),    
]
