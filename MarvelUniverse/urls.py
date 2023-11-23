from django.urls import path
from .views.homepage import HomePageView
from .views.about import AboutUsView
from .views.see_all import AllCharactersView, AllComicsView, AllSeriesView
from .views.detail import character_detail_view, comic_detail_view, series_detail_view
from .views.favorites import toggle_favorite
from .views.favorites import FavoriteView
from .views.quiz import SelectQuizView, CharacterInstructionView, ComicInstructionView, SeriesInstructionView, random_quiz, character_quiz_view, comic_quiz_view, series_quiz_view, quiz_results


app_name = "MarvelUniverse"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('characters/', AllCharactersView.as_view(), name="characters"),
    path('comics/', AllComicsView.as_view(), name="comics"),
    path('series/', AllSeriesView.as_view(), name="series"),
    path('<str:model>/<int:object_id>/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path('favorites/', FavoriteView.as_view(), name='favorites'),
    path('characters/<int:character_pk>', character_detail_view, name="characters-detail"),
    path('comics/<int:comic_pk>', comic_detail_view, name="comics-detail"),
    path('series/<int:series_pk>', series_detail_view, name="series-detail"),
    path('about/', AboutUsView.as_view(), name='about'),
    # quiz url
    path('quiz/', SelectQuizView.as_view(), name='select-quiz'),
    # quiz instruction
    path('quiz/random-quiz/', random_quiz, name='random-quiz'),
    path('quiz/character-instruction/', CharacterInstructionView.as_view(), name='character-instruction'),
    path('quiz/comic-instruction/', ComicInstructionView.as_view(), name='comic-instruction'),
    path('quiz/series-instruction/', SeriesInstructionView.as_view(), name='series-instruction'),
    
    # path('quiz/character-quiz/', random_character_question, name='random-character-question'),
    # path('quiz/comic-quiz/', random_comic_question, name='random-comic-question'),
    # path('quiz/series-quiz/', random_series_question, name='random-series-question'),

    path('quiz/character-quiz/<int:question_pk>', character_quiz_view, name='character-quiz'),
    path('quiz/comic-quiz/<int:question_pk>', comic_quiz_view, name='comic-quiz'),
    path('quiz/series-quiz/<int:question_pk>', series_quiz_view, name='series-quiz'),

    path('quiz/results', quiz_results, name='quiz-results'),
]
