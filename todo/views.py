from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    template_name = 'todo/index.html'
    http_method_names = ['get']

    def get(self, request):
        return render(request, self.template_name)