from django.urls import path
from .views.homepage import HomePageView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView
from .views.detail import CharactersDetailView, ComicsDetailView, SeriesDetailView

app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('all-characters/', AllCharactersView.as_view(), name="all-characters"),
    path('all-comics/', AllComicsView.as_view(), name="all-comics"),
    path('all-series/', AllSeriesView.as_view(), name="all-series"),   
    path('characters/<int:pk>', CharactersDetailView.as_view(), name="characters-detail"),        
    path('comics/<int:pk>', ComicsDetailView.as_view(), name="comics-detail"),        
    path('series/<int:pk>', SeriesDetailView.as_view(), name="series-detail"),        
]
