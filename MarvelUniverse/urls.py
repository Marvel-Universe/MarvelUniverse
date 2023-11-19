from django.urls import path
from .views.homepage import HomePageView
from .views.about import AboutUsView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView
from .views.detail import CharactersDetailView, comic_detail_view, series_detail_view
from .views.favorites import toggle_favorite
from .views.favorites import FavoriteView


app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('characters/', AllCharactersView.as_view(), name="characters"),
    path('comics/', AllComicsView.as_view(), name="comics"),
    path('series/', AllSeriesView.as_view(), name="series"),
    path('characters/<int:character_pk>', CharactersDetailView.as_view(), name="characters-detail"),
    path('comics/<int:comic_pk>', comic_detail_view, name="comics-detail"),
    path('series/<int:series_pk>', series_detail_view, name="series-detail"),
    path('<str:model>s/<int:object_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', FavoriteView.as_view(), name='favorites'),
    path('about/', AboutUsView.as_view(), name='about')
]
