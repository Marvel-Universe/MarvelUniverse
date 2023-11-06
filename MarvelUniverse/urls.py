from django.urls import path
from .views.homepage import HomePageView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView

app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('all-characters/', AllCharactersView.as_view(), name="all-characters"),
    path('all-comics/', AllComicsView.as_view(), name="all-comics"),
    path('all-series/', AllSeriesView.as_view(), name="all-series"),    
]
