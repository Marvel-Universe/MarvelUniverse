from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
import random
from random import choice, sample
from django.urls import reverse
from ..models import CharacterQuestion, CharacterChoice
from django.contrib import messages


class SelectQuizView(View):
    template_name = 'MarvelUniverse/quiz/select-quiz.html'

    def get(self, request):
        return render(request, self.template_name)


class CharacterInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/character-instruction.html'
    
    def get(self, request):
        return render(request, self.template_name)
    

class ComicInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/comic-instruction.html'
    
    def get(self, request):
        return render(request, self.template_name)
    

class SeriesInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/series-instruction.html'
    
    def get(self, request):
        return render(request, self.template_name)


def random_quiz(request):
    quiz_views = ['MarvelUniverse:character-instruction', 'MarvelUniverse:comic-instruction', 'MarvelUniverse:series-instruction']
    random_quiz_view = random.choice(quiz_views)
    return HttpResponseRedirect(reverse(random_quiz_view))
