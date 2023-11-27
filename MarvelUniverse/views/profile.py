from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  # Import login_required
import json

from MarvelUniverse.models import UserData

@method_decorator(login_required(login_url='login'), name='dispatch')  # Apply login_required to all methods in the class
class ProfileView(View):
    template_name = 'MarvelUniverse/profile.html'

    def get(self, request):
        this_user = request.user
        user_data, created = UserData.objects.get_or_create(user=this_user)

        formatted_date_joined = naturaltime(this_user.date_joined)

        context = {
            'user': this_user,
            'user_data': user_data, 
            'profile_img_url': user_data.profile_img_url,
            'date_joined': formatted_date_joined,
        }

        return render(request, self.template_name, context=context)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfileImageView(View):
    @method_decorator(login_required(login_url='login'))  # Apply login_required only to the post method
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        avatar_url = data.get('avatarUrl', '')

        user_data = UserData.objects.get(user=request.user)
        user_data.profile_img_url = avatar_url
        user_data.save()

        return JsonResponse({'success': True})
