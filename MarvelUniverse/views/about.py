from django.views import View
from django.shortcuts import render

class AboutUsView(View):
    template_name = 'MarvelUniverse/about.html'

    def get(self, request):
        return render(request, self.template_name)