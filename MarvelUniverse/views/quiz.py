from django.views import View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.http import HttpResponseRedirect
from random import sample, shuffle, choice
from django.urls import reverse
from ..models import CharacterQuestion, CharacterChoice, ComicChoice, ComicQuestion, SeriesQuestion, SeriesChoice
from django.contrib import messages
from ..models import UserData


class SelectQuizView(View):
    template_name = 'MarvelUniverse/quiz/select-quiz.html'

    def get(self, request):
        return render(request, self.template_name)


class CharacterInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/character-instruction.html'
    
    def get(self, request):
        context = {
            'random_pk': random_question(1, 188)
        }
        return render(request, self.template_name, context)
    

class ComicInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/comic-instruction.html'
    
    def get(self, request):
        context = {
            'random_pk': random_question(3, 102)
        }
        return render(request, self.template_name, context)
    

class SeriesInstructionView(View):
    template_name = 'MarvelUniverse/quiz/instruction/series-instruction.html'
    
    def get(self, request):
        context = {
            'random_pk': random_question(1, 100)
        }
        return render(request, self.template_name, context)
    

def random_quiz(request):
    quiz_views = ['MarvelUniverse:character-instruction', 'MarvelUniverse:comic-instruction', 'MarvelUniverse:series-instruction']
    random_quiz_view = choice(quiz_views)
    return HttpResponseRedirect(reverse(random_quiz_view))


def random_question(start_pk, end_pk):
    random_pks = sample(range(start_pk, end_pk+1), 1)
    return random_pks[0]


@login_required(login_url='login')
def character_quiz_view(request, question_pk):
    try:
        question = get_object_or_404(CharacterQuestion, pk=question_pk)
        all_choices = CharacterChoice.objects.filter(question=question)
        correct_choices = all_choices.filter(is_correct=True)
        incorrect_choices = all_choices.filter(is_correct=False)
        choices_list = sample(list(correct_choices), 1) + sample(list(incorrect_choices), 3)
        shuffle(choices_list)
    except CharacterQuestion.DoesNotExist:
        messages.error(request, "Question not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:select-quiz')) 
    except CharacterChoice.DoesNotExist:
        messages.error(request, "Choice not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:character-quiz', args=(question_pk,)))

    question_counter = request.session.get('question_counter', 0)
    scores_per_game = request.session.get('scores_per_game', 0)

    if request.method == 'POST':
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(CharacterChoice, pk=choice_id)

        if choice.is_correct:
            scores_per_game += 50
            messages.success(request, 'Correct! earn +10 points.')
        else:
            scores_per_game -= 10
            messages.success(request, 'Incorrect, -5 points try again!')

        question_counter += 1
        request.session['question_counter'] = question_counter
        request.session['scores_per_game'] = scores_per_game

        if question_counter >= 10:
            messages.info(request, 'This is the last question!')
            request.session['question_counter'] = 0
            request.session['scores_per_game'] = scores_per_game
            return HttpResponseRedirect(reverse('MarvelUniverse:leaderboard'))

        random_pk = random_question(1, 188)
        return HttpResponseRedirect(reverse('MarvelUniverse:character-quiz', args=(random_pk,)))

    context = {
        'question': question,
        'choices': choices_list,
        'question_number': question_counter + 1, 
        'scores_per_game': scores_per_game
    }
    return render(request, 'MarvelUniverse/quiz/character-quiz.html', context)


@login_required(login_url='login')
def comic_quiz_view(request, question_pk):
    try:
        question = get_object_or_404(ComicQuestion, pk=question_pk)
        all_choices = ComicChoice.objects.filter(question=question)
        correct_choices = all_choices.filter(is_correct=True)
        incorrect_choices = all_choices.filter(is_correct=False)
        choices_list = sample(list(correct_choices), 1) + sample(list(incorrect_choices), 3)
        shuffle(choices_list)
    except ComicQuestion.DoesNotExist:
        messages.error(request, "Question not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:select-quiz')) 
    except ComicChoice.DoesNotExist:
        messages.error(request, "Choice not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:comic-quiz', args=(question_pk,)))

    question_counter = request.session.get('question_counter', 0)
    scores_per_game = request.session.get('scores_per_game', 0)

    if request.method == 'POST':
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(ComicChoice, pk=choice_id)

        if choice.is_correct:
            scores_per_game += 50
            messages.success(request, 'Correct! earn +10 points.')
        else:
            scores_per_game -= 10
            messages.success(request, 'Incorrect, -5 points try again!')

        question_counter += 1
        request.session['question_counter'] = question_counter
        request.session['scores_per_game'] = scores_per_game

        if question_counter >= 10:
            messages.info(request, 'This is the last question!')
            request.session['question_counter'] = 0
            request.session['scores_per_game'] = scores_per_game
            return HttpResponseRedirect(reverse('MarvelUniverse:leaderboard'))

        random_pk = random_question(2, 102)
        return HttpResponseRedirect(reverse('MarvelUniverse:comic-quiz', args=(random_pk,)))

    context = {
        'question': question,
        'choices': choices_list,
        'question_number': question_counter + 1, 
        'scores_per_game': scores_per_game
    }
    return render(request, 'MarvelUniverse/quiz/comic-quiz.html', context)


@login_required(login_url='login')
def series_quiz_view(request, question_pk):
    try:
        question = get_object_or_404(SeriesQuestion, pk=question_pk)
        all_choices = SeriesChoice.objects.filter(question=question)
        correct_choices = all_choices.filter(is_correct=True)
        incorrect_choices = all_choices.filter(is_correct=False)
        choices_list = sample(list(correct_choices), 1) + sample(list(incorrect_choices), 3)
        shuffle(choices_list)
    except SeriesQuestion.DoesNotExist:
        messages.error(request, "Question not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:select-quiz')) 
    except SeriesChoice.DoesNotExist:
        messages.error(request, "Choice not found")
        return HttpResponseRedirect(reverse('MarvelUniverse:series-quiz', args=(question_pk,)))

    question_counter = request.session.get('question_counter', 0)
    scores_per_game = request.session.get('scores_per_game', 0)

    if request.method == 'POST':
        choice_id = request.POST.get('choice_id')
        choice = get_object_or_404(SeriesChoice, pk=choice_id)

        if choice.is_correct:
            scores_per_game += 50
            messages.success(request, 'Correct! earn +10 points.')
        else:
            scores_per_game -= 10
            messages.success(request, 'Incorrect, -5 points try again!')

        question_counter += 1
        request.session['question_counter'] = question_counter

        if question_counter >= 10:
            messages.info(request, 'This is the last question!')
            request.session['question_counter'] = 0
            request.session['scores_per_game'] = scores_per_game
            return HttpResponseRedirect(reverse('MarvelUniverse:leaderboard'))

        random_pk = random_question(1, 100)
        return HttpResponseRedirect(reverse('MarvelUniverse:series-quiz', args=(random_pk,)))

    context = {
        'question': question,
        'choices': choices_list
    }
    return render(request, 'MarvelUniverse/quiz/series-quiz.html', context)


@login_required(login_url='login')
def leaderboard(request):
    this_user = request.user
    this_user_data, created = UserData.objects.get_or_create(user=this_user)
    users_data = UserData.objects.all()
    if 'scores_per_game' in request.session:
        scores = request.session['scores_per_game']
        del request.session['scores_per_game']
        this_user_data.scores += scores
        this_user_data.save()
    else:
        scores = 0
    context = {
        'user_scores': this_user_data.scores,
        'top3_users_data': users_data.order_by('-scores')[0:3],
        'other_users_data': users_data.order_by('-scores')[3:]
    }
    return render(request, 'MarvelUniverse/quiz/leaderboard.html',  context)
